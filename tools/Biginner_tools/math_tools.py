from pydantic import BaseModel, Field

class AddNumbersInput(BaseModel):
    """Add two numbers together."""
    a: int = Field(..., description="The first number")
    b: int = Field(..., description="The second number")

def add_numbers(a: int, b: int) -> dict:
    """Implementation of adding numbers."""
    return {"result": a + b}
