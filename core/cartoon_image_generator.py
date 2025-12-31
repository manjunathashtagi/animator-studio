import torch
from diffusers import StableDiffusionPipeline
import os

MODEL_ID = "stabilityai/sdxl-turbo"  # fast & cartoon-friendly

_pipe = None

def get_pipe():
    global _pipe
    if _pipe is None:
        _pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16,
            variant="fp16"
        ).to("cuda")
    return _pipe


def generate_cartoon_image(scene, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    prompt = (
        "cartoon anime illustration, mythology style, "
        "clean line art, vibrant colors, cinematic lighting, "
        f"{scene.text}"
    )

    pipe = get_pipe()
    image = pipe(
        prompt=prompt,
        num_inference_steps=6,
        guidance_scale=0.0
    ).images[0]

    path = os.path.join(output_dir, f"scene_{scene.id}_cartoon.png")
    image.save(path)
    return path
