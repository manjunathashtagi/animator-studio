import os
from PIL import Image, ImageDraw, ImageFont
from core.animator_2_5d import animate_image


def generate_scene_image(scene, output_dir):
    """
    Temporary visual generator:
    creates a simple image with scene text.
    (This will later be replaced by AI image generation)
    """
    os.makedirs(output_dir, exist_ok=True)

    img = Image.new("RGB", (1280, 720), color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    text = f"Scene {scene.id}\n{scene.type}\n\n{scene.text[:200]}"
    draw.multiline_text((50, 100), text, fill=(230, 230, 230))

    image_path = os.path.join(output_dir, f"scene_{scene.id}.png")
    img.save(image_path)
    return image_path


def generate_preview(scene):
    preview_dir = "outputs/previews"
    image_dir = "outputs/previews/images"
    os.makedirs(preview_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    image_path = generate_scene_image(scene, image_dir)

    preview_path = os.path.join(
        preview_dir, f"scene_{scene.id}_preview.mp4"
    )

    animate_image(
        image_path=image_path,
        duration=scene.duration,
        output_path=preview_path
    )

    return preview_path
