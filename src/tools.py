from langchain_core.tools import tool
import requests

# ----------------------------
# Define tools
# ----------------------------

@tool
def calculate(expression: str) -> str:
    """Evaluate a math expression."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"


@tool
def request_price(product: str) -> str:
    """Send a request to the local API server to get the price of a product."""
    url = "http://127.0.0.1:8000/query"
    payload = {"query": product}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"


tools = {t.name: t for t in [calculate, request_price]}
