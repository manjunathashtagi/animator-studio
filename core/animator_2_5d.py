from moviepy.editor import ImageClip
import numpy as np


def animate_image(image_path, duration, output_path):
    """
    Creates visible cinematic animation:
    - Slow zoom in
    - Gentle vertical drift
    """

    clip = ImageClip(image_path).set_duration(duration)

    w, h = clip.size

    def zoom_and_pan(t):
        # Zoom from 1.0 → 1.08
        zoom = 1 + 0.08 * (t / duration)

        # Vertical drift (up-down)
        y_offset = int(20 * np.sin(2 * np.pi * t / duration))

        return clip.resize(zoom).set_position(
            ("center", h / 2 + y_offset)
        )

    animated = clip.fl(zoom_and_pan, apply_to=["mask", "video"])

    animated.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio=False,
        verbose=False,
        logger=None,
    )

    return output_path
