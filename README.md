📘 SIGN.MT – Team Collaboration Documentation (Updated)

A clean, technical, collaboration-friendly document

1. Project Summary

sign.mt is a multilingual sign-language translation system that converts:

Text → Sign Video

Speech → Text → Sign Video

YouTube Audio → Text → Sign Video

This version of the project does NOT use any trained machine-learning model.
We have NOT trained on any dataset yet.

Instead, the system uses:

Dummy gloss generation

Dictionary-based gloss → pose mapping

Lightweight OpenCV-based video rendering

This makes the project fast, simple, and able to run on low-resource devices.

2. Current Achievements (What works now)
✔ Multilingual text translation

Any language → English (deep-translator)

✔ Speech recognition

Microphone input

YouTube audio input

✔ Dummy gloss generation

Simple uppercase token glossing.
(No ML training used.)

✔ Gloss → Pose mapping

Dictionary-based synthetic pose generation.
(No real dataset used.)

✔ Video rendering

Lightweight

Low-resolution

Optimized performer

Outputs output.mp4

✔ Runs on basic laptops

No GPU required

Python 3.10

Low RAM usage

❗ Important: No ML models are trained in this project yet

No text→gloss ML model

No gloss→pose ML model

No dataset has been trained on

Only pre-coded rule-based methods

This is clearly stated for team transparency.

3. Future Goals (What we want to achieve)
🟦 1. Train real Text → Gloss model

Using datasets like:

RWTH-PHOENIX-2014T

How2Sign

ASLG-PC12

(Model: Transformer / seq2seq)

🟦 2. Train Gloss → Pose generation model

Using:

Mediapipe extracted pose sequences

LSTM / Transformer

🟦 3. Add 3D pose and avatar animation

(Not included yet.)

🟦 4. Add proper sign grammar rules
🟦 5. Collect + preprocess datasets

Team members can help with this step.

4. Project Folder Structure (With Explanation of Missing ML Training)
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
│                            → (Text→gloss model NOT trained yet)
│                            → (Gloss→pose neural model NOT trained yet)
│

⚠ Note for team:

models/ folder contains placeholders.
No ML training has been done.
All behavior is rule-based.

5. How the System Works (For New Team Members)
✔ 1. Input selection

User chooses:

Text

Microphone speech

YouTube audio

✔ 2. Language Detection

langdetect identifies the language.

✔ 3. Translate to English

We use GoogleTranslator.

✔ 4. Text Cleaning

Lowercasing + punctuation removal.

✔ 5. Gloss Generation (Dummy)

Words → UPPERCASE tokens
(No trained gloss model is used.)

✔ 6. Gloss → Pose Generation

Using a static dictionary mapping
(No ML model involved.)

✔ 7. Video Rendering

OpenCV draws white pose dots → saves as output.mp4.

6. Prerequisites (Team Member Setup)
✔ Python 3.10

(Important!)

✔ Required packages
pip install numpy==1.26.4
pip install langdetect
pip install deep-translator
pip install opencv-python
pip install yt-dlp
pip install sounddevice
pip install nltk
pip install rich
pip install certifi


(Optional STT)

pip install openai-whisper

System Requirements:

Windows 10/11

4GB RAM

No GPU needed

7. Running the Project

Step 1 — Activate environment:

signmt-env\Scripts\Activate.ps1


Step 2 — Run main file:

python demo_run.py


Step 3 — Choose mode:

1 → Text → Sign
2 → Microphone → Sign
3 → YouTube → Sign


Step 4 — Output:

output.mp4

8. What The Team Should Know (Important Notes)
✔ This project currently uses NO AI training

Just rule-based transformations.

✔ All ML folders are placeholders

We will add real ML in Phase 2.

✔ Everyone should understand the pipeline

so future improvements can be added easily.

✔ The system is modular

Each component (translation, glossing, pose rendering) is separate.

9. Final Summary for Collaboration

This document is the official guide for contributors.
Everyone joining the project must know:

✔ What the system currently does
✔ What it does NOT do (NO TRAINED MODELS)
✔ What the next goals are
✔ How the code is structured
✔ How to run it
✔ What tasks are open for contributors

