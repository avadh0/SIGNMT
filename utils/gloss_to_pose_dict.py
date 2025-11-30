# utils/gloss_to_pose_dict.py
"""
Dictionary-based gloss -> pose mapping.
This placeholder returns synthetic normalized pose frames for each gloss token.
Pose frame format: list of (x,y) pairs normalized to [0,1].
"""

import numpy as np

# small vocabulary mapping for demo; you can expand
_SIMPLE_GLOSS_POSES = {
    "HELLO": [(0.45,0.2),(0.55,0.2),(0.5,0.35)],  # head & hands
    "PLEASE": [(0.5,0.5),(0.5,0.6)],
    "THANK": [(0.5,0.55),(0.5,0.65)],
    "YES": [(0.5,0.4),(0.52,0.48)],
    "NO": [(0.5,0.4),(0.48,0.48)],
    "I": [(0.5,0.45)],
    "ME": [(0.5,0.5)],
    "WATER": [(0.5,0.6),(0.55,0.6)],
    "GIVE": [(0.45,0.55),(0.55,0.55)],
    # fallback: single neutral point
}

def _pose_for_gloss(token):
    token = str(token).upper()
    return _SIMPLE_GLOSS_POSES.get(token, [(0.5,0.5)])

def sentence_to_pose_sequence(gloss_tokens, frames_per_token=3):
    """
    Convert flat list of gloss tokens into a list of pose frames.
    Each frame is a list/array of (x,y) positions normalized [0..1].
    """
    seq = []
    for g in gloss_tokens:
        base = np.array(_pose_for_gloss(g))
        # create simple interpolation frames for motion
        for f in range(frames_per_token):
            alpha = f / max(1, frames_per_token-1)
            # apply a tiny oscillation to make motion slightly varied
            jitter = 0.02 * np.sin((f+1) * 2.0)
            frame = base + jitter
            # clip and convert to list of (x,y)
            frame = np.clip(frame, 0.0, 1.0)
            seq.append([tuple(pt.tolist()) for pt in frame])
    return seq
