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

# Get device list
device_Rembg = ["Default","cpu"]
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        device_Rembg.append(f"cuda:{i}")
if torch.backends.mps.is_available():
    device_Rembg.append("mps:0")

class InspyrenetRembg:
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
    DESCRIPTION = """
    The function of this node: 
        1: When multiple InspyrenetRembg nodes are used, only one model can be loaded into memory/graphics memory (shared model).
        2: Three models are available for selection
        3: You can also choose not to input the model and default to using the base model
        4: When sharing models, it can save 1.2 seconds of model loading time on solid-state drives, 
           and mechanical hard drives can save even more

    此节点的作用：
        1: 当使用多个InspyrenetRembg节点时,可以仅加载一个模型到内存/显存(共用模型)
        2: 可选三种模型
        3: 也可以不输入模型,默认使用base模型
        4: 共用模型时可节省固态硬盘1.2秒模型加载时间，机械硬盘可节省更多
        """
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
            "optional": {
                "model": ("inspyrenet",),
            }
        }
    
    CATEGORY = "InspyrenetRembg"
    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "remove_background"

    def remove_background(self, image ,model=None):
        if len(device_Rembg) > 2:
            device = device_Rembg[2]
        else:
            device = device_Rembg[1]
        if model is None:
            model = Remover(mode="base", jit=False ,device=device)

        img_list = []
        for img in tqdm(image, "Inspyrenet Rembg"):
            mid = model.process(tensor2pil(img), type='rgba')
            out =  pil2tensor(mid)
            img_list.append(out)
        img_stack = torch.cat(img_list, dim=0)
        mask = img_stack[:, :, :, 3]
        return (img_stack, mask)

class load_Inspyrenet_model: 
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": (["base", "fast", "base-nightly"],{"default": "base"}),
                "device": (device_Rembg,{"default": "Default"}),
                "torchscript_jit": ("BOOLEAN",{"default": False}),
            },
        }
    
    CATEGORY = "InspyrenetRembg"
    RETURN_TYPES = ("inspyrenet",)
    RETURN_NAMES = ("inspyrenet_model",)
    FUNCTION = "load_model"

    def load_model(self, model, device,torchscript_jit):
        if device == "Default": 
            if len(device_Rembg) > 2:
                device = device_Rembg[2]
            else:
                device = device_Rembg[1]
        model = Remover(mode=model, jit=torchscript_jit,device=device)
        return (model,)

class InspyrenetRembgAdvanced:
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