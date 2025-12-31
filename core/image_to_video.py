import torch
import os
from diffusers import StableVideoDiffusionPipeline
from PIL import Image

MODEL_ID = "stabilityai/stable-video-diffusion-img2vid-xt"

_pipe = None


def get_pipe():
    global _pipe
    if _pipe is None:
        _pipe = StableVideoDiffusionPipeline.from_pretrained(
            MODEL_ID,
            torch_dtype=torch.float16,
            variant="fp16"
        ).to("cuda")
    return _pipe


def image_to_video(
    image_path: str,
    output_path: str,
    motion_prompt: str,
    num_frames: int = 24,
):
    """
    Generates short character-motion video from a single image
    """

    pipe = get_pipe()

    image = Image.open(image_path).convert("RGB")

    video_frames = pipe(
        image=image,
        motion_bucket_id=127,
        fps=6,
        num_frames=num_frames,
        noise_aug_strength=0.02,
    ).frames[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    import imageio
    imageio.mimsave(
        output_path,
        video_frames,
        fps=6,
        codec="libx264"
    )

    return output_path
