import torch
from diffusers import StableDiffusionPipeline

MODEL_ID = "runwayml/stable-diffusion-v1-5"

_pipe = None


def get_pipe():
    global _pipe

    if _pipe is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

        _pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32
        )

        if device == "cuda":
            _pipe.enable_attention_slicing()
            _pipe.enable_model_cpu_offload()

    return _pipe


def generate_cartoon_image(scene, output_dir):
    pipe = get_pipe()

    prompt = scene.prompt
    negative_prompt = "blurry, low quality, distorted face"

    image = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        guidance_scale=7.5,
        num_inference_steps=30
    ).images[0]

    output_path = f"{output_dir}/scene_{scene.id}.png"
    image.save(output_path)

    return output_path
