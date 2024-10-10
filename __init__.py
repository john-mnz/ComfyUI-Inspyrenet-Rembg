from .Inspyrenet_Rembg import InspyrenetRembg, InspyrenetRembgAdvanced, InspyrenetRembg_selectmodel, load_Inspyrenet_model

NODE_CLASS_MAPPINGS = {
    "InspyrenetRembg" : InspyrenetRembg,
    "InspyrenetRembgAdvanced" : InspyrenetRembgAdvanced,
    "InspyrenetRembg_selectmodel" : InspyrenetRembg_selectmodel,
    "load_Inspyrenetmodel" : load_Inspyrenet_model
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "InspyrenetRembg": "Inspyrenet Rembg",
    "InspyrenetRembgAdvanced": "Inspyrenet Rembg Advanced",
    "InspyrenetRembg_selectmodel": "InspyrenetRembg_selectmodel",
    "load_Inspyrenetmodel": "load_Inspyrenetmodel"
}
__all__ = ['NODE_CLASS_MAPPINGS', "NODE_DISPLAY_NAME_MAPPINGS"]
