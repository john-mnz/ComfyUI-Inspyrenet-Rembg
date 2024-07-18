# ComfyUI-Inspyrenet-Rembg
[ComfyUI](https://github.com/comfyanonymous/ComfyUI) node for background removal, implementing [InSPyReNet](https://github.com/plemeri/InSPyReNet)
</br></br>

I've tested a lot of different AI rembg methods (BRIA - U2Net - IsNet - SAM - OPEN RMBG, ...) but in all of my tests InSPyReNet was always ON A WHOLE DIFFERENT LEVEL!

The cherry on top is that [InSPyReNet](https://github.com/plemeri/InSPyReNet) has MIT License which allows for Commercial use (for example BRIA does not allow Commercial use to my knowledge)

Check [InSPyReNet](https://github.com/plemeri/InSPyReNet) License for yourself I will not be held accountable :)

## Features

superior rembg quality compared to other methods

can take batch of images as input

Optimized for image batch to be the fastest rembg node (perfect for video frames)

outputs both the image and the corresponding mask


## Installation 

### Simple way:

search for  `ComfyUI-Inspyrenet-Rembg` in ComfyUI-Manager and hit install.

Done!

### Manual:

1. Go to your `custom_nodes` folder in ComfyUI, open the terminal and run the following command:

```
git clone https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg.git
```

2. To install requirements, run the following commands:

```
cd ComfyUI-Inspyrenet-Rembg
pip install -r requirements.txt
```
Done!

It downloads the pretrained model automatically at first use

## note 
If torchscript_jif is set to on, it will trace model with pytorch built-in torchscript JIT compiler. May cause delay in initialization, but reduces inference time and gpu memory usage.

## show case 
![ComfyUI-Inspyrenet-Rembg2](https://github.com/user-attachments/assets/f68ec1ae-5c64-4ded-899b-10dfb783d5eb)

![ComfyUI-Inspyrenet-Rembg](https://github.com/user-attachments/assets/e1817609-7645-4d72-b187-0cf5e74cb6c5)
