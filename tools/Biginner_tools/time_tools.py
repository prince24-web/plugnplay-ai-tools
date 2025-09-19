from pydantic import BaseModel
import datetime

class GetTimeInput(BaseModel):
    """No params needed, just fetch time."""
    pass

def get_time() -> dict:
    return {"time": datetime.datetime.now().strftime("%H:%M:%S")}
