# ComfyUI-Inspyrenet-Rembg
[ComfyUI](https://github.com/comfyanonymous/ComfyUI) node for background removal implementing [InSPyReNet](https://github.com/plemeri/InSPyReNet)
</br></br>

I've tested a lot of different AI rembg methods (BRIA - U2Net - IsNet - SAM - OPEN RMBG, ...) but in all of my tests InSPyReNet was always ON A WHOLE DIFFERENT LEVEL!

The cherry on top is that [InSPyReNet](https://github.com/plemeri/InSPyReNet) has MIT License which allows for Commercial use (for example BRIA does not allow Commercial use to my knowledge)


The node was missing from comfy so I developed this which has been of great help to me ever since.

It can take image batch as input too

I hope it helps you and your workflows as well🙂


Check [InSPyReNet](https://github.com/plemeri/InSPyReNet) License for yourself I will not be held accountable :)


## Installation 

1. Clone to your `custom_nodes` folder in ComfyUI:

```
git clone https://github.com/john-mnz/ComfyUI-Inspyrenet-Rembg.git
```

2. Install requirements:

```
pip install -r requirements.txt
```

If torchscript_jif is set to on, it will trace model with pytorch built-in torchscript JIT compiler. May cause delay in initialization, but reduces inference time and gpu memory usage.


![ComfyUI-Inspyrenet-Rembg2](https://github.com/user-attachments/assets/f68ec1ae-5c64-4ded-899b-10dfb783d5eb)

![ComfyUI-Inspyrenet-Rembg](https://github.com/user-attachments/assets/e1817609-7645-4d72-b187-0cf5e74cb6c5)
