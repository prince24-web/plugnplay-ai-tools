from pydantic import BaseModel
import datetime
from langchain_core.tools import tool

class GetTimeInput(BaseModel):
    """No params needed, just fetch time."""
    pass

@tool
def get_time() -> dict:
    """Return the current system time in HH:MM:SS format."""
    return {"time": datetime.datetime.now().strftime("%H:%M:%S")}
