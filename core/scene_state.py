# core/scene_state.py

class Scene:
    def __init__(self, scene_id, text, duration=4):
        self.id = scene_id
        self.text = text
        self.duration = duration
        self.status = "pending"

    def approve(self):
        self.status = "approved"
        return self

    def delete(self):
        self.status = "deleted"
        return self
