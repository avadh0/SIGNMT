# utils/pose_render.py
# Optimized, low-resource renderer that writes output.mp4 (or webm)
import os
import cv2
import numpy as np
import gc

def render_video(
    pose_seq,
    out_video_path="output.mp4",
    fps=15,
    width=360,
    height=360,
    dot_radius=4,
    background_color=(0,0,0),
    dot_color=(255,255,255),
    use_webm=False
):
    """
    Render pose sequence into a single video file.
    pose_seq: list of frames; each frame is an iterable of (x,y) normalized coords.
    This function centers the pose cloud and writes frames efficiently.
    """
    fourcc = cv2.VideoWriter_fourcc(*("VP80" if use_webm else "mp4v"))
    video = cv2.VideoWriter(out_video_path, fourcc, fps, (width, height))

    for frame in pose_seq:
        # create blank image
        img = np.zeros((height, width, 3), dtype=np.uint8)
        # convert frame to numpy array (N,2)
        pts = np.asarray(frame, dtype=np.float32)
        if pts.size == 0:
            video.write(img)
            continue
        if pts.ndim == 1:
            pts = pts.reshape(1, -1)
        xs = pts[:, 0]
        ys = pts[:, 1]
        # safety clip in [0,1]
        xs = np.clip(xs, 0.0, 1.0)
        ys = np.clip(ys, 0.0, 1.0)
        # pixels
        xs_px = xs * width
        ys_px = ys * height
        # center on screen
        x_offset = (width / 2.0) - np.mean(xs_px)
        y_offset = (height / 2.0) - np.mean(ys_px)
        pts_px = np.stack([xs_px + x_offset, ys_px + y_offset], axis=1).astype(np.int32)
        # clip
        pts_px[:, 0] = np.clip(pts_px[:, 0], 0, width - 1)
        pts_px[:, 1] = np.clip(pts_px[:, 1], 0, height - 1)
        # draw dots
        for (px, py) in pts_px:
            cv2.circle(img, (int(px), int(py)), dot_radius, dot_color, -1)
        video.write(img)

    video.release()
    # free memory
    try:
        del pose_seq
    except:
        pass
    gc.collect()
    return out_video_path
