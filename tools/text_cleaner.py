# tools/text_cleaner.py
import re
from bs4 import BeautifulSoup
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class TextCleanerInput(BaseModel):
    """Input schema for cleaning text."""
    text: str = Field(..., description="The raw text that may contain HTML or punctuation")
    remove_html: bool = Field(True, description="Whether to remove HTML tags")
    remove_punctuation: bool = Field(True, description="Whether to remove punctuation")
    lowercase: bool = Field(False, description="Whether to convert text to lowercase")

@tool(args_schema=TextCleanerInput)
def clean_text(text: str, remove_html: bool = True, remove_punctuation: bool = True, lowercase: bool = False) -> dict:
    """Cleans text by removing HTML tags, punctuation, and optionally converting to lowercase."""

    cleaned = text

    # Remove HTML tags
    if remove_html:
        cleaned = BeautifulSoup(cleaned, "html.parser").get_text()

    # Remove punctuation
    if remove_punctuation:
        cleaned = re.sub(r"[^\w\s]", "", cleaned)

    # Lowercase
    if lowercase:
        cleaned = cleaned.lower()

    return {"cleaned_text": cleaned}
