from PIL import Image
import torch
import numpy as np
from .Remover_comfy_path import Remover
from tqdm import tqdm


# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# Convert PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

class InspyrenetRembg:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "torchscript_jit": (["default", "on"],)
            },
        }

    CATEGORY = "InspyrenetRembg"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "remove_background"

    def remove_background(self, image, torchscript_jit):
        if (torchscript_jit == "default"):
            remover = Remover()
        else:
            remover = Remover(jit=True)
        img_list = []
        for img in tqdm(image, "Inspyrenet Rembg"):
            mid = remover.process(tensor2pil(img), type='rgba')
            out =  pil2tensor(mid)
            img_list.append(out)
        img_stack = torch.cat(img_list, dim=0)
        mask = img_stack[:, :, :, 3]
        return (img_stack, mask)
    
class InspyrenetRembg_selectmodel:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "torchscript_jit": ("BOOLEAN",{"default": False}),
                "model": (["base", "fast", "base-nightly"],{"default": "base"}),
                "device": (["Auto", "cpu", "cuda:0", "mps:0"],{"default": "Auto"}),
            },
        }
    
    CATEGORY = "InspyrenetRembg"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "remove_background"

    def remove_background(self, image, torchscript_jit, model, device):
        if device == "Auto": device = None
        remover = Remover(mode=model, jit=torchscript_jit)

        img_list = []
        for img in tqdm(image, "Inspyrenet Rembg"):
            mid = remover.process(tensor2pil(img), type='rgba')
            out =  pil2tensor(mid)
            img_list.append(out)
        img_stack = torch.cat(img_list, dim=0)
        mask = img_stack[:, :, :, 3]
        return (img_stack, mask)
        
class InspyrenetRembgAdvanced:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "threshold": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "torchscript_jit": (["default", "on"],)
            },
        }
    
    CATEGORY = "InspyrenetRembg"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "remove_background"

    def remove_background(self, image, torchscript_jit, threshold):
        if (torchscript_jit == "default"):
            remover = Remover()
        else:
            remover = Remover(jit=True)
        img_list = []
        for img in tqdm(image, "Inspyrenet Rembg"):
            mid = remover.process(tensor2pil(img), type='rgba', threshold=threshold)
            out =  pil2tensor(mid)
            img_list.append(out)
        img_stack = torch.cat(img_list, dim=0)
        mask = img_stack[:, :, :, 3]
        return (img_stack, mask)