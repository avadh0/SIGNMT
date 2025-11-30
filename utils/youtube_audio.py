# utils/youtube_audio.py
import subprocess
import shutil
import os

def download_youtube_audio(url, out_path="yt_audio.wav"):
    """
    Download audio from YouTube using yt-dlp.
    Saves as wav (requires ffmpeg in PATH).
    """
    # remove existing file
    if os.path.exists(out_path):
        try: os.remove(out_path)
        except: pass
    # yt-dlp to fetch best audio and convert to wav
    # requires: yt-dlp and ffmpeg installed
    cmd = [
        "yt-dlp", "--no-playlist", "-x", "--audio-format", "wav",
        "-o", "temp_audio.%(ext)s", url
    ]
    try:
        subprocess.run(cmd, check=True)
        # find the downloaded file (temp_audio.wav)
        if os.path.exists("temp_audio.wav"):
            shutil.move("temp_audio.wav", out_path)
        else:
            # attempt to find any temp file and move
            for f in os.listdir("."):
                if f.startswith("temp_audio"):
                    shutil.move(f, out_path)
                    break
    except Exception as e:
        print("yt-dlp failed:", e)
    return out_path
