"""
demo_run.py — main runner for sign.mt

Modes:
1) Text -> Sign
2) Microphone -> Speech -> Sign
3) YouTube -> Speech -> Sign

Produces a single file: output.mp4 (in project root).
"""

import os
from deep_translator import GoogleTranslator

# Utils
from utils.text_clean import simple_clean
from utils.segmentation import split_sentences
from utils.langid import detect_language
from utils.gloss_to_pose_dict import sentence_to_pose_sequence
from utils.pose_render import render_video

# Speech + YouTube helpers
from utils.stt import audio_to_text, record_audio
from utils.youtube_audio import download_youtube_audio

# Performance settings
VIDEO_PATH = "output.mp4"
WIDTH = 360
HEIGHT = 360
FPS = 15
FRAMES_PER_TOKEN = 3
DOT_RADIUS = 4
USE_WEBM = False  # set to True to output webm instead of mp4

def run_text_to_sign(text):
    """
    Convert given text (any language) into a sign-video saved at VIDEO_PATH.
    """
    # 1) Language detection
    lang, prob, _ = detect_language(text)

    # 2) Translate to English for pipeline (if not English)
    if lang != "en":
        try:
            text = GoogleTranslator(source='auto', target='en').translate(text)
        except Exception as e:
            print("Translation failed, using original text:", e)

    # 3) Clean & split
    cleaned = simple_clean(text)
    sents = split_sentences(cleaned)

    # 4) Dummy gloss (uppercase tokens) — replace later with model
    glosses = [[w.upper() for w in s.split()] for s in sents]
    gloss_tokens = [g for sent in glosses for g in sent]

    # 5) Gloss -> Pose sequence (dictionary-based)
    pose_seq = sentence_to_pose_sequence(gloss_tokens, frames_per_token=FRAMES_PER_TOKEN)

    # 6) Remove existing output and render video
    if os.path.exists(VIDEO_PATH):
        try:
            os.remove(VIDEO_PATH)
        except Exception:
            pass

    render_video(
        pose_seq,
        out_video_path=VIDEO_PATH,
        fps=FPS,
        width=WIDTH,
        height=HEIGHT,
        dot_radius=DOT_RADIUS,
        use_webm=USE_WEBM
    )

    print("Video created:", os.path.abspath(VIDEO_PATH))


if __name__ == "__main__":
    print("sign.mt — optimized runner")
    print("1) Text -> Sign")
    print("2) Microphone -> Sign")
    print("3) YouTube -> Sign")
    mode = input("Enter 1, 2 or 3: ").strip()

    if mode == "1":
        txt = input("Enter text: ")
        run_text_to_sign(txt)

    elif mode == "2":
        audio_file = "mic_audio.wav"
        record_audio(audio_file, duration=4)
        txt = audio_to_text(audio_file)
        run_text_to_sign(txt)
        try:
            os.remove(audio_file)
        except:
            pass

    elif mode == "3":
        url = input("Enter YouTube link: ").strip()
        audio_file = "yt_audio.wav"
        download_youtube_audio(url, audio_file)
        txt = audio_to_text(audio_file)
        run_text_to_sign(txt)
        try:
            os.remove(audio_file)
        except:
            pass
    else:
        print("Invalid option.")
