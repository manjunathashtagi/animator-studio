from moviepy.editor import ImageClip
import numpy as np


def animate_image(image_path, duration, output_path):
    """
    Stable cinematic animation:
    - Slow zoom using cropping (no pixel tearing)
    - Gentle vertical pan
    """

    base = ImageClip(image_path)
    W, H = base.size

    # Create a slightly larger virtual canvas
    zoom_factor = 1.15
    big = base.resize(zoom_factor).set_duration(duration)

    BW, BH = big.size

    def crop_position(t):
        # Progress 0 → 1
        p = t / duration

        # Vertical gentle movement
        y_shift = int(20 * np.sin(2 * np.pi * p))

        # Center crop + drift
        x1 = int((BW - W) / 2)
        y1 = int((BH - H) / 2 + y_shift)

        return big.crop(
            x1=x1,
            y1=y1,
            width=W,
            height=H
        )

    animated = big.fl(lambda gf, t: crop_position(t).get_frame(0))

    animated.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio=False,
        verbose=False,
        logger=None,
    )

    return output_path
