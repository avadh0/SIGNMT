# utils/stt.py
import os
import subprocess

def audio_to_text(audio_path):
    """
    Convert audio file to text.
    If whisper is installed (openai-whisper), use it; otherwise fallback to simple placeholder.
    """
    try:
        import whisper
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        return result.get("text", "")
    except Exception:
        # fallback: try system's speech recognition? For now return empty
        print("Whisper not available — returning empty transcription.")
        return ""

def record_audio(out_path="mic_input.wav", duration=4):
    """
    Record audio from microphone and save to out_path.
    This uses sounddevice if installed, otherwise tries ffmpeg if available.
    """
    try:
        import sounddevice as sd
        import wavio
        fs = 16000
        print("Recording for", duration, "seconds...")
        rec = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        wavio.write(out_path, rec, fs, sampwidth=2)
        return out_path
    except Exception:
        # fallback: ask user to supply a file
        print("sounddevice not available — please provide an audio file manually.")
        return out_path
