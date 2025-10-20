from PIL import Image
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
import io

eval_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

def predict_image(model, idx_to_class, image_bytes, topk=3):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img_t = eval_transform(img).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img_t)
        probs = F.softmax(outputs, dim=1)
        top_probs, top_idxs = torch.topk(probs, topk)

    results = []
    for prob, idx in zip(top_probs[0], top_idxs[0]):
        dish = idx_to_class.get(idx.item(), "unknown")
        results.append({"dish": dish, "confidence": float(prob)})
    return results
