from PIL import Image
import numpy as np
from moviepy.editor import ImageSequenceClip
import os


def animate_image(image_path, duration, output_path):
    """
    Guaranteed-stable animation:
    - Manual frame generation (no MoviePy transforms)
    - Slow zoom + gentle vertical drift
    """

    fps = 30
    total_frames = int(duration * fps)

    img = Image.open(image_path).convert("RGB")
    W, H = img.size

    frames = []

    for i in range(total_frames):
        t = i / total_frames

        # Zoom from 1.0 → 1.1
        zoom = 1 + 0.1 * t
        new_w = int(W * zoom)
        new_h = int(H * zoom)

        resized = img.resize((new_w, new_h), Image.LANCZOS)

        # Vertical drift
        y_shift = int(20 * np.sin(2 * np.pi * t))

        # Center crop back to original size
        left = (new_w - W) // 2
        top = (new_h - H) // 2 + y_shift

        frame = resized.crop((left, top, left + W, top + H))
        frames.append(np.array(frame))

    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(
        output_path,
        codec="libx264",
        audio=False,
        verbose=False,
        logger=None,
    )

    return output_path
