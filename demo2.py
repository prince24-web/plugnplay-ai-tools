import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.passwordGenerator import generate_password

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

TOOLS = [generate_password]
llm_with_tools = llm.bind_tools(TOOLS)

response = llm_with_tools.invoke("Generate a secure password of length 16 with digits and special characters.")

if response.tool_calls:
    for call in response.tool_calls:
        if call["name"] == "generate_password":
            tool_result = generate_password.invoke(call["args"])
            print("✅ Tool executed:", tool_result)

# Step 2: Otherwise, it's just chat text
else:
    print("💬 AI Response:", response.content)