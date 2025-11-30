# utils/text_clean.py
import re

def simple_clean(text: str) -> str:
    """
    Basic text cleaning:
    - lowercases
    - trims spaces
    - replaces multiple spaces
    - keeps punctuation minimally
    """
    if not isinstance(text, str):
        return ""
    text = text.strip()
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r"\s+", " ", text)
    # keep characters, punctuation will be preserved to help segmentation
    return text.strip()
