import os
from core.animator_2_5d import animate_image
from core.cartoon_image_generator import generate_cartoon_image


def generate_preview(scene):
    preview_dir = "outputs/previews"
    image_dir = "outputs/previews/images"

    os.makedirs(preview_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    # Generate cartoon image
    image_path = generate_cartoon_image(scene, image_dir)

    preview_path = os.path.join(
        preview_dir, f"scene_{scene.id}_preview.mp4"
    )

    animate_image(
        image_path=image_path,
        duration=scene.duration,
        output_path=preview_path
    )

    return preview_path
