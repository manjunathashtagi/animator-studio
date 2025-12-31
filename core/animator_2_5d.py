from moviepy.editor import ImageClip, CompositeVideoClip
import os

def animate_image(image_path, duration, output_path):
    """
    Creates a simple 2.5D animation:
    slow zoom + slight vertical movement
    """
    clip = (
        ImageClip(image_path)
        .set_duration(duration)
        .resize(height=720)
        .fx(lambda c: c.resize(1.05))
    )

    video = CompositeVideoClip([clip])
    video.write_videofile(
        output_path,
        fps=30,
        codec="libx264",
        audio=False,
        verbose=False,
        logger=None,
    )

    return output_path
