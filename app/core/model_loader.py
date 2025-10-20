import os
import torch
import json
from torchvision import models
import torch.nn as nn

def load_model():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    model_path = os.path.join(base_dir, "model", "food_vn_resnet18.pth")
    mapping_path = os.path.join(base_dir, "model", "class_mapping.json")

    with open(mapping_path) as f:
        class_to_idx = json.load(f)
    idx_to_class = {v: k for k, v in class_to_idx.items()}

    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(class_to_idx))
    model.load_state_dict(torch.load(model_path, map_location="cpu", weights_only=True))
    model.eval()

    return model, idx_to_class
