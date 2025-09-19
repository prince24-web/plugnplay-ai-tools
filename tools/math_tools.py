from pydantic import BaseModel, Field
from langchain_core.tools import tool
import math

class AddNumbersInput(BaseModel):
    a: int = Field(..., description="The first number")
    b: int = Field(..., description="The second number")

class SubtractNumbersInput(BaseModel):
    a: int = Field(..., description="The first number")
    b: int = Field(..., description="The second number")

class MultiplyNumbersInput(BaseModel):
    a: int = Field(..., description="The first number")
    b: int = Field(..., description="The second number")

class DivideNumbersInput(BaseModel):
    a: int = Field(..., description="Numerator")
    b: int = Field(..., description="Denominator")

class SqrtNumberInput(BaseModel):
    x: int = Field(..., description="The number to take the square root of")


@tool(args_schema=AddNumbersInput)
def add_numbers(a: int, b: int) -> dict:
    """Add two numbers together."""
    return {"result": a + b}

@tool(args_schema=SubtractNumbersInput)
def subtract_numbers(a: int, b: int) -> dict:
    """Subtract one number from another."""
    return {"result": a - b}

@tool(args_schema=MultiplyNumbersInput)
def multiply_numbers(a: int, b: int) -> dict:
    """Multiply two numbers together."""
    return {"result": a * b}

@tool(args_schema=DivideNumbersInput)
def divide_numbers(a: int, b: int) -> dict:
    """Divide one number by another."""
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": a / b}

@tool(args_schema=SqrtNumberInput)
def sqrt_number(x: int) -> dict:
    """Calculate the square root of a number."""
    if x < 0:
        return {"error": "Square root of a negative number is not allowed"}
    return {"result": math.sqrt(x)}
