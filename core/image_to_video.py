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
        )
        # VERY IMPORTANT: memory optimizations
        _pipe.enable_model_cpu_offload()
        _pipe.enable_attention_slicing()
    return _pipe


def image_to_video(
    image_path: str,
    output_path: str,
    motion_prompt: str,
    num_frames: int = 18,   # ↑ more frames
):
    pipe = get_pipe()

    image = Image.open(image_path).convert("RGB")
    image = image.resize((384, 384))  # ↓ smaller = more motion

    with torch.no_grad():
        video_frames = pipe(
            image=image,
            motion_bucket_id=160,      # 🔥 MUCH higher motion
            fps=6,
            num_frames=num_frames,
            noise_aug_strength=0.08,   # 🔥 forces movement
            decode_chunk_size=1,       # slower but safer
        ).frames[0]

    import imageio
    imageio.mimsave(
        output_path,
        video_frames,
        fps=6,
        codec="libx264"
    )

    torch.cuda.empty_cache()
    return output_path


