from moviepy.editor import ImageClip
import numpy as np


def animate_image(image_path, duration, output_path):
    """
    Cinematic 2.5D animation:
    - Slow zoom in
    - Gentle vertical drift
    """

    clip = ImageClip(image_path).set_duration(duration)
    w, h = clip.size

    def make_frame(get_frame, t):
        # Zoom from 1.0 → 1.08 over time
        zoom = 1 + 0.08 * (t / duration)

        # Gentle vertical float
        y_offset = int(20 * np.sin(2 * np.pi * t / duration))

        frame = get_frame(t)
        frame_clip = ImageClip(frame).resize(zoom).set_position(
            ("center", h / 2 + y_offset)
        )

        return frame_clip.get_frame(0)

    animated = clip.fl(make_frame)

    animated.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio=False,
        verbose=False,
        logger=None,
    )

    return output_path
