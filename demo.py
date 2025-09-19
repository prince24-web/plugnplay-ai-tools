# demo.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Import tools
from tools.math_tools import (
    add_numbers,
    subtract_numbers,
    multiply_numbers,
    divide_numbers,
    sqrt_number
)
from tools.time_tools import get_time

# --- Load environment ---
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Bind all tools
TOOLS = [add_numbers, subtract_numbers, multiply_numbers, divide_numbers, sqrt_number, get_time]
llm_with_tools = llm.bind_tools(TOOLS)

# --- Example queries ---
queries = [
    "Add 12 and 8",
    "Subtract 50 and 12",
    "Multiply 6 and 7",
    "Divide 100 by 25",
    "What is the square root of 81?",
    "What time is it now?"
]

for q in queries:
    print(f"\n❓ User: {q}")
    response = llm_with_tools.invoke(q)

    if response.tool_calls:  # If Gemini decides to call a tool
        for call in response.tool_calls:
            tool_name = call["name"]
            tool_args = call["args"]

            # Dynamically find and run the right tool
            for tool in TOOLS:
                if tool.name == tool_name:
                    tool_result = tool.invoke(tool_args)
                    print(f"✅ Tool `{tool_name}` executed:", tool_result)
    else:
        print("💬 AI Response:", response.content)
