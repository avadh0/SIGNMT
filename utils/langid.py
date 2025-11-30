# utils/langid.py
from langdetect import detect_langs, DetectorFactory

# fix randomness
DetectorFactory.seed = 0

def detect_language(text: str):
    """
    Return (lang_code, probability, raw_list)
    If detection fails, default to 'en'
    """
    if not text:
        return "en", 1.0, None
    try:
        langs = detect_langs(text)
        if not langs:
            return "en", 1.0, None
        top = langs[0]
        return top.lang, float(top.prob), langs
    except Exception:
        return "en", 1.0, None
