from dataclasses import dataclass

@dataclass
class Scene:
    id: int
    text: str
    type: str
    duration: int
    nsfw: bool
    status: str = "generated"


def build_scenes(segments, nsfw_enabled=False):
    scenes = []
    for i, seg in enumerate(segments):
        scene_type = "DIALOGUE"
        if "appeared" in seg.lower():
            scene_type = "CHARACTER_ENTRY"
        if "battle" in seg.lower():
            scene_type = "ACTION"

        scenes.append(
            Scene(
                id=i + 1,
                text=seg,
                type=scene_type,
                duration=8,
                nsfw=nsfw_enabled and scene_type == "INTIMACY",
            )
        )
    return scenes
