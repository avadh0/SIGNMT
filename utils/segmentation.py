# utils/segmentation.py
import re

def split_sentences(text: str):
    """
    Very simple sentence split: split on .!? then strip.
    If nothing, return list with original text.
    """
    if not text:
        return []
    # split and keep punctuation
    parts = re.split(r'(?<=[\.\!\?])\s+', text)
    parts = [p.strip() for p in parts if p.strip()]
    if not parts:
        return [text.strip()]
    return parts
