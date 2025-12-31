from moviepy.editor import ImageClip
import numpy as np


def animate_image(image_path, duration, output_path):
    """
    Stable 2.5D animation using time-based lambdas
    (MoviePy-safe, no fl(), no frame hacks)
    """

    clip = ImageClip(image_path).set_duration(duration)
    w, h = clip.size

    # Time-based zoom
    clip = clip.resize(lambda t: 1 + 0.08 * (t / duration))

    # Time-based vertical drift
    clip = clip.set_position(
        lambda t: ("center", h / 2 + 20 * np.sin(2 * np.pi * t / duration))
    )

    clip.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio=False,
        verbose=False,
        logger=None,
    )

    return output_path
