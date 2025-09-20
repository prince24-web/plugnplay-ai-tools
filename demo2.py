# demo2.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tools.text_cleaner import clean_text

# Load API key
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

TOOLS = [clean_text]
llm_with_tools = llm.bind_tools(TOOLS)

# Load your big HTML from a file
with open("long_demo.html", "r", encoding="utf-8") as f:
    messy_html = f.read()

# Ask naturally (no raw HTML inside f-string)
user_request = f"Clean this text: remove all HTML tags, punctuation, and lowercase it:\n\n{messy_html}"

response = llm_with_tools.invoke(user_request)

if response.tool_calls:
    for call in response.tool_calls:
        if call["name"] == "clean_text":
            result = clean_text.invoke(call["args"])
            print("✅ Cleaned text:\n", result["cleaned_text"][:500], "...")  # preview first 500 chars
else:
    print("💬 AI Response:", response.content)
