from langchain_ollama import OllamaLLM
from tools import tools
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
import logging

# ----------------------------
# Setup Logger
# ----------------------------
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# ----------------------------
# Load Model
# ----------------------------
llm = OllamaLLM(model="llama3.2")

# ----------------------------
# Node 1: llm - Extract product name
# ----------------------------
def extract_product(state: dict) -> dict:
    input_text = state.get("input", "")
    prompt = f"Extract the product name from this question: '{input_text}'\nRespond with only the product name."
    product = llm.invoke(prompt).strip()
    logger.info(f"llm extracted product: {product}")
    state["product"] = product
    return state

# ----------------------------
# Node 2: Function Node - Get price
# ----------------------------
def get_price(state: dict) -> dict:
    product = state.get("product")
    tool = tools.get("prices")
    price = tool.invoke(product) if tool else "Unknown product"
    logger.info(f"Function Node returned price: {price}")
    state["price"] = price
    return state

# ----------------------------
# Node 3: LLM_2 - Generate final response
# ----------------------------
def generate_response(state: dict) -> dict:
    product = state.get("product")
    price = state.get("price")
    final_response = f"The price for the {product} is {price}."
    logger.info(f"Final response (formatted): {final_response}")
    state["final_answer"] = final_response
    return state

# ----------------------------
# Build LangGraph
# ----------------------------
workflow = StateGraph(dict)
workflow.add_node("extract_product", RunnableLambda(extract_product))
workflow.add_node("get_price", RunnableLambda(get_price))
workflow.add_node("generate_response", RunnableLambda(generate_response))

workflow.set_entry_point("extract_product")
workflow.add_edge("extract_product", "get_price")
workflow.add_edge("get_price", "generate_response")
workflow.add_edge("generate_response", END)

app = workflow.compile()
