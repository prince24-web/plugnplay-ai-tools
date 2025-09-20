from pydantic import BaseModel, Field
from langchain_core.tools import tool
import re

class Emailvalidatorinput(BaseModel):
    email: str = Field(..., description="The email address to validate")

@tool(args_schema=Emailvalidatorinput)
def Validate_email(email: str) -> dict:
    """Validate if an email address is in the correct format."""
    #simple regex for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        return{"valid": True, "reason": "Valid email format"}
    else:
        return{"valid": False, "reason": "Invalid email format"}
