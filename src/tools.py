
from langchain_core.tools import tool
import datetime
import pytz


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
def get_current_time(timezone: str = "UTC") -> str:
    """Get current time in a timezone."""
    try:
        now_utc = datetime.datetime.now(datetime.UTC)
        target_timezone = pytz.timezone(timezone)
        return now_utc.astimezone(target_timezone).strftime("%Y-%m-%d %H:%M:%S %Z")
    except Exception as e:
        return f"Error: {e}"

tools = {t.name: t for t in [calculate, get_current_time]}
