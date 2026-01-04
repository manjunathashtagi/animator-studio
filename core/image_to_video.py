import torch
import gc
from diffusers import StableVideoDiffusionPipeline
from PIL import Image
import imageio
import os

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

        _pipe.enable_attention_slicing()
        _pipe.enable_model_cpu_offload()

    return _pipe


def image_to_video(image_path, output_path, num_frames=12):
    pipe = get_pipe()

    image = Image.open(image_path).convert("RGB")
    image = image.resize((512, 512))

    gc.collect()
    torch.cuda.empty_cache()
    torch.cuda.ipc_collect()

    with torch.no_grad():
        result = pipe(
            image=image,
            num_frames=num_frames,
            fps=6,
            motion_bucket_id=80,
            noise_aug_strength=0.02,
            decode_chunk_size=1
        )

    frames = result.frames[0]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    imageio.mimsave(
        output_path,
        frames,
        fps=8,
        codec="libx264"
    )

    return output_path



