def approve_scene(scene):
    scene.status = "approved"
    return scene


def delete_scene(scene):
    scene.status = "deleted"
    return scene
