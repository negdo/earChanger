from diffusers import StableDiffusionPipeline
import torch

torch.backends.cudnn.benchmark = True


#model_id = "classes/ami-more"
model_id = "D:/3d/slikovna biometrija/awe 8200"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cuda")

prompt = "photo of amiawe ear"
print(prompt)
#with torch.autocast("cuda"):
for i in range(10):
    image = pipe(prompt, num_inference_steps=20, guidance_scale=7.5).images[0]
    image.save(f"output/ear{i}.png")