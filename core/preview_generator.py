import os
from PIL import Image, ImageDraw, ImageFont
from core.animator_2_5d import animate_image


import os
from PIL import Image, ImageDraw, ImageFont
from core.animator_2_5d import animate_image


def generate_scene_image(scene, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # Bigger canvas
    img = Image.new("RGB", (1280, 720), color=(10, 10, 10))
    draw = ImageDraw.Draw(img)

    # Try to use a bigger font
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 48)
        small_font = ImageFont.truetype("DejaVuSans.ttf", 32)
    except:
        font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    # Title
    draw.text(
        (60, 60),
        f"Scene {scene.id} — {scene.type}",
        fill=(255, 200, 80),
        font=font
    )

    # Body text
    draw.multiline_text(
        (60, 160),
        scene.text,
        fill=(220, 220, 220),
        font=small_font,
        spacing=10
    )

    image_path = os.path.join(output_dir, f"scene_{scene.id}.png")
    img.save(image_path)
    return image_path



def generate_preview(scene):
    preview_dir = "outputs/previews"
    image_dir = "outputs/previews/images"
    os.makedirs(preview_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    from core.cartoon_image_generator import generate_cartoon_image

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


