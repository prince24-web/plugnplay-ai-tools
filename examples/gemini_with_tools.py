import os, getpass
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# import Pydantic classes (schemas) so we can bind tools
from tools.math_tools import AddNumbersInput, add_numbers
from tools.time_tools import GetTimeInput, get_time
from tools.weather_tools import WeatherInput, get_weather

load_dotenv()
if not os.getenv("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = getpass.getpass("Enter your Gemini API key: ")

# Init Gemini LLM (same pattern we've used)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

# Bind Pydantic classes as tools
# langchain's bind_tools accepts Pydantic BaseModel classes (the library maps to function schemas)
llm_with_tools = llm.bind_tools([AddNumbersInput, GetTimeInput, WeatherInput])

# Example: ask model to add numbers
resp = llm_with_tools.invoke("Add 12 and 30")
print("Model response (tool call):", resp)

# Example: ask for time
resp2 = llm_with_tools.invoke("What time is it now?")
print("Model response (tool call):", resp2)
