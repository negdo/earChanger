import PIL
import requests
import torch
from io import BytesIO
from torchvision import transforms
from diffusers.models import AutoencoderKL

from diffusers import StableDiffusionInpaintPipeline
from diffusers import UNet2DConditionModel


def inpaint(image_path, mask_path):
    #open images
    init_image = PIL.Image.open(image_path).convert("RGB").resize((512, 512))
    mask_image = PIL.Image.open(mask_path).convert("L").resize((512, 512))


    unet = UNet2DConditionModel.from_pretrained("runwayml/stable-diffusion-inpainting", subfolder="unet")
    # vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse")

    # pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting", torch_dtype=torch.float32)
    # pipe = StableDiffusionInpaintPipeline.from_pretrained("runwayml/stable-diffusion-inpainting",revision="fp16",torch_dtype=torch.float16)
    pipe = StableDiffusionInpaintPipeline.from_pretrained("classes/ami-more", torch_dtype=torch.float32, unet=unet)
    # pipe = StableDiffusionInpaintPipeline.from_pretrained("D:/3d/slikovna biometrija/awe 8200", torch_dtype=torch.float32, unet=unet)
    pipe = pipe.to("cuda")

    prompt = "photo of amiawe ear"
    image = pipe(prompt=prompt, image=init_image, mask_image=mask_image, num_inference_steps=20).images[0]

    # print type of image: <class 'PIL.Image.Image'>
    return image
    
