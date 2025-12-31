from moviepy.editor import VideoFileClip, concatenate_videoclips

def compose_videos(video_paths, output_path):
    """
    Combines approved scenes into one final video.
    """
    clips = [VideoFileClip(v) for v in video_paths]
    final = concatenate_videoclips(clips, method="compose")

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        fps=30
    )

    return output_path
