from langchain_core.prompts import PromptTemplate

# ----------------------------
# Prompt template with few-shot example
# ----------------------------

prompt_template = PromptTemplate.from_template("""
You are a helpful assistant that uses tools to answer questions step-by-step.

Available tools:
{tool_descriptions}

Use this format exactly:

Question: {input}
{agent_scratchpad}
Thought: you should think about what to do
Action: <tool name>
Action Input: <input to the tool>
Observation: <tool result>
... (repeat Thought/Action/Action Input/Observation as needed)
Thought: I now know the final answer
Final Answer: <answer>

Example:
Question: What is 2 + 2?
Thought: I should use the calculator
Action: calculate
Action Input: 2 + 2
Observation: 4
Thought: I now know the final answer
Final Answer: 4
""")