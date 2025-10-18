import argparse
from react_agent import app

# ----------------------------
# Run the agent
# ----------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the ReAct agent with a custom input.")
    parser.add_argument("--input", type=str, default="What is the price of a laptop?", help="Input prompt for the agent")
    args = parser.parse_args()

    result = app.invoke({"input": args.input})
   