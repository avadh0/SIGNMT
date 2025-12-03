# SIGN FOR Ac

> **Multilingual, rule-based sign-language rendering system (no ML trained yet)**

---

## 1. Project summary

**sign.ac** converts:

* Text → Sign Video
* Speech → Text → Sign Video
* YouTube Audio → Text → Sign Video

**This version does NOT use any trained ML models.**
All processing is rule-based: dummy glossing, dictionary-based gloss→pose mapping, and OpenCV rendering.

---

## 2. Current achievements (what works now)

* ✅ Multilingual text translation (any language → English using `deep-translator`)
* ✅ Speech recognition: microphone input and YouTube audio extraction
* ✅ Dummy gloss generation (simple uppercase token glossing)
* ✅ Gloss → pose mapping (dictionary-based synthetic pose generation)
* ✅ Video rendering (lightweight OpenCV-based rendering → `output.mp4`)
* ✅ Runs on basic laptops (Python 3.10, low RAM, no GPU required)

> **Important:** No ML models trained. No datasets used. All behavior is pre-coded rules.

---

## 3. Future goals (phase 2)

* Train a real Text → Gloss model (datasets: RWTH-PHOENIX-2014T, How2Sign, ASLG-PC12)
* Train a Gloss → Pose generation model (use Mediapipe pose sequences; LSTM / Transformer)
* Add 3D pose & avatar animation
* Implement proper sign grammar rules
* Collect and preprocess datasets (open tasks for contributors)

---

## 4. Folder structure

### 📦 Project Structure Diagram (Visual)

```
SIGNMT/
│
├── demo_run.py
├── output.mp4
│
├── utils/
│   ├── text_clean.py
│   ├── segmentation.py
│   ├── langid.py
│   ├── gloss_to_pose_dict.py
│   ├── pose_render.py
│   ├── stt.py
│   └── youtube_audio.py
│
├── models/
│   ├── text2gloss/        (placeholder)
│   ├── gloss2pose/        (placeholder)
│   └── README.md          (explanation of missing ML models)
│
```

```
SIGNMT/
│ demo_run.py                → Main pipeline (runs text/speech/video input)
│ output.mp4                 → Final generated video
│
├── utils/
│   ├── text_clean.py        → Text preprocessing
│   ├── segmentation.py      → Sentence splitting
│   ├── langid.py            → Language detection
│   ├── gloss_to_pose_dict.py→ Dictionary-based pose generator (NO ML)
│   ├── pose_render.py       → Video rendering (OpenCV)
│   ├── stt.py               → Speech-to-text
│   └── youtube_audio.py     → YouTube audio extraction
│
├── models/                  → (Currently contains no trained ML models)
│
├── sign-datasets/           → Placeholder for future datasets
│
└── signmt-env/              → Python environment
```

**Note:** `models/` contains placeholders only. No training performed.

---

## 5. Working Structure (System Flow Diagram)

```
┌────────────────────┐
│ 1. User Input       │
│  • Text             │
│  • Microphone audio │
│  • YouTube audio    │
└─────────┬──────────┘
          │
          ▼
┌──────────────────────────┐
│ 2. Language Detection     │
│  (langdetect)             │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ 3. Translation to English │
│  (deep-translator)        │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ 4. Text Cleaning          │
│  (lowercase, punctuation) │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ 5. Dummy Gloss Generator  │
│  (word → UPPERCASE token) │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ 6. Gloss → Pose Mapping   │
│  (dictionary-based rules) │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ 7. Pose Renderer          │
│  (OpenCV → output.mp4)    │
└──────────────────────────┘
```

## 5. How the system works (pipeline)

1. Input selection: text / microphone / YouTube audio
2. Language detection (`langdetect`) → translate to English (`deep-translator`)
3. Text cleaning (lowercase, punctuation removal)
4. Dummy gloss generation (words → UPPERCASE tokens)
5. Gloss → Pose generation (lookup in dictionary)
6. Video rendering (OpenCV draws simple pose dots/lines → `output.mp4`)

---

## 6. Prerequisites & setup (team members)

* **Python**: 3.10 (important)

Install required packages:

```bash
pip install numpy==1.26.4
pip install langdetect
pip install deep-translator
pip install opencv-python
pip install yt-dlp
pip install sounddevice
pip install nltk
pip install rich
pip install certifi

# Optional STT
pip install openai-whisper
```

System: Windows 10/11, 4GB RAM, no GPU required.

---

## 7. Running the project

1. Activate environment:

```powershell
signmt-env\Scripts\Activate.ps1
```

2. Run main pipeline:

```bash
python demo_run.py
```

3. Choose mode at prompt:

* `1` → Text → Sign
* `2` → Microphone → Sign
* `3` → YouTube → Sign

4. Output: `output.mp4` saved in project root.

---

## 8. Important notes for contributors

* This project currently uses **NO** ML training — everything is rule-based and modular.
* All ML-related folders are placeholders and will be filled in Phase 2.
* The pipeline is modular: translation, glossing, pose rendering are separate files to make contributions straightforward.

---

## 9. Contribution & tasks (open items)

* Collect and preprocess sign language datasets (RWTH, How2Sign, ASLG-PC12)
* Implement and train Text→Gloss and Gloss→Pose models
* Add 3D pose support and avatar rendering
* Improve rendering quality and add more naturalized poses

---

## 10. Quick developer helpers (examples)

### `demo_run.py` — minimal skeleton

```python
"""demo_run.py — minimal pipeline skeleton for SIGNMT
This skeleton shows how components are wired. Implementations live in `utils/`.
"""
import argparse
from utils.langid import detect_language
from utils.text_clean import clean_text
from utils.gloss_to_pose_dict import gloss_from_text, poses_from_gloss
from utils.pose_render import render_video


def run_text_mode(text: str, out_file: str = "output.mp4"):
    lang = detect_language(text)
    # translation step assumed handled earlier — placeholder
    cleaned = clean_text(text)
    gloss = gloss_from_text(cleaned)
    poses = poses_from_gloss(gloss)
    render_video(poses, out_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['text','mic','youtube'], default='text')
    parser.add_argument('--text', type=str, default='HELLO WORLD')
    args = parser.parse_args()

    if args.mode == 'text':
        run_text_mode(args.text)
    else:
        raise NotImplementedError('mic/youtube modes are in utils/stt.py and utils/youtube_audio.py')
```

### `utils/gloss_to_pose_dict.py` — example function

```python
# utils/gloss_to_pose_dict.py
# minimal dictionary-based gloss -> poses mapper

def gloss_from_text(text: str):
    # dummy: split and uppercase tokens
    return [w.upper() for w in text.split()]


def poses_from_gloss(gloss_tokens):
    # each token -> simple synthetic pose sequence (list of frames)
    poses = []
    for token in gloss_tokens:
        # synthetic pose: list of (x,y) landmarks for few frames
        frames = [ [(i*5, i*3) for i in range(8)] for _ in range(5) ]
        poses.append({'token': token, 'frames': frames})
    return poses
```

### `utils/pose_render.py` — minimal rendering idea

```python
# utils/pose_render.py
import cv2
import numpy as np


def render_video(poses, out_file='output.mp4', frame_size=(320,240), fps=10):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(out_file, fourcc, fps, frame_size)

    for token_block in poses:
        for frame_landmarks in token_block['frames']:
            img = np.zeros((frame_size[1], frame_size[0], 3), dtype=np.uint8)
            img.fill(255)  # white background
            for (x,y) in frame_landmarks:
                cv2.circle(img, (int(x)%frame_size[0], int(y)%frame_size[1]), 4, (0,0,0), -1)
            writer.write(img)
    writer.release()
```

---

