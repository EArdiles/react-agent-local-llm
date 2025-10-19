

from langchain_ollama import OllamaLLM
from tools import tools 
from prompt_template import prompt_template
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
import re


llm = OllamaLLM(model="llama3.2")
tool_descriptions = "\n".join([f"{name}: {tool.description}" for name, tool in tools.items()])

# ----------------------------
# LangGraph Nodes
# ----------------------------

def call_llm(state: dict) -> dict:
    input_text = state.get("input", "")
    scratchpad = state.get("scratchpad", "")
    prompt = prompt_template.format(
        input=input_text,
        agent_scratchpad=scratchpad,
        tool_descriptions=tool_descriptions
    )
    response = llm.invoke(prompt)
    print("\nLLM Output:\n", response)  # Debug output
    state["llm_output"] = response
    return state

def parse_output(state: dict) -> dict:
    output = state["llm_output"]
    state.setdefault("steps", []).append(output)

    if "Final Answer:" in output:
        final_answer = output.split("Final Answer:")[-1].strip()
        state["final_answer"] = final_answer
        return {"finish": state}

    action_match = re.search(r"Action: (.*)", output)
    input_match = re.search(r"Action Input: (.*)", output)
    if action_match and input_match:
        state["action"] = action_match.group(1).strip()
        state["action_input"] = input_match.group(1).strip()
        return {"tool": state}
    else:
        state["final_answer"] = "Could not parse action."
        return {"finish": state}

def call_tool(state: dict) -> dict:
    action = state.get("action")
    action_input = state.get("action_input")
    tool = tools.get(action)
    result = tool.invoke(action_input) if tool else f"Unknown tool: {action}"

    scratchpad = state.get("scratchpad", "")
    scratchpad += f"\nThought: {state['llm_output'].split('Thought:')[-1].strip()}"
    scratchpad += f"\nAction: {action}\nAction Input: {action_input}\nObservation: {result}"
    state["scratchpad"] = scratchpad
    return state

# ----------------------------
# Build LangGraph
# ----------------------------

workflow = StateGraph(dict)
workflow.add_node("llm", RunnableLambda(call_llm))
workflow.add_node("parser", RunnableLambda(parse_output))
workflow.add_node("tool", RunnableLambda(call_tool))

workflow.set_entry_point("llm")
workflow.add_edge("llm", "parser")
workflow.add_conditional_edges("parser", lambda x: list(x.keys())[0], {
    "tool": "tool",
    "finish": END
})
workflow.add_edge("tool", "llm")

app = workflow.compile()
