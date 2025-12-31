import os
from core.cartoon_image_generator import generate_cartoon_image
from core.image_to_video import image_to_video
from core.animator_2_5d import animate_image


def generate_preview(scene, motion_mode="camera"):
    preview_dir = "outputs/previews"
    image_dir = "outputs/previews/images"

    os.makedirs(preview_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    image_path = generate_cartoon_image(scene, image_dir)

    preview_path = os.path.join(
        preview_dir, f"scene_{scene.id}_preview.mp4"
    )

    if motion_mode == "character":
        return image_to_video(
            image_path=image_path,
            output_path=preview_path,
            motion_prompt=scene.text,
        )
    else:
        return animate_image(
            image_path=image_path,
            duration=scene.duration,
            output_path=preview_path
        )
