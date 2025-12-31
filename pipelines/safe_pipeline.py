from core.story_parser import split_story_into_segments
from core.scene_builder import build_scenes

def run_safe_pipeline(story: str):
    segments = split_story_into_segments(story)
    scenes = build_scenes(segments, nsfw_enabled=False)
    return scenes
