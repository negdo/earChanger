# earChanger

Simple application for replacing ears on images. Ears are detected with Yolov5 and then inpainted with custom Stable Diffusion model trained on images from https://ctim.ulpgc.es/research_works/ami_ear_database/

## How to use

Run with following command
```
python change_ear.py
```
Browse for image and start the process with **Change Ear** button.
![image](https://user-images.githubusercontent.com/18052453/212131018-3ad0c252-f220-4e73-8739-026d2000426c.png)


## Installation of required libraries

Running this requires nvidia GPU with about 8GB VRAM. *(Tested on 16GB of VRAM)*

Create python environment
```
python -m venv venv
.\venv\Scripts\activate
```

Install Hugging Face Diffusers https://huggingface.co/docs/diffusers/installation and other libraries.
```
pip install diffusers["torch"]
pip install git+https://github.com/huggingface/diffusers

pip install accelerate
pip install transformers

pip3 install torch==1.10.1+cu113 torchvision==0.11.2+cu113 torchaudio===0.10.1+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
pip install opencv-python
pip install pandas
pip install ipython
pip install matplotlib
pip install seaborn
```
