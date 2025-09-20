from pydantic import BaseModel, Field
from langchain_core.tools import tool
import random
import string

class PasswordGeneratorInput(BaseModel):
    length: int = Field(..., description="Length of the password to generate (e.g., 8–32)")
    use_digits: bool = Field(default=True, description="Include digits in the password")
    use_special: bool = Field(default=True, description="Include special characters in the password")

@tool(args_schema=PasswordGeneratorInput)
def generate_password(length: int, use_digits: bool = True, use_special: bool = True) -> dict:
    """Generate a strong random password with given options."""
    
    # Start with lowercase + uppercase letters
    chars = string.ascii_letters  

    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if length < 4:
        return {"error": "Password length must be at least 4"}

    # Randomly select characters
    password = ''.join(random.choice(chars) for _ in range(length))
    return {"password": password}
