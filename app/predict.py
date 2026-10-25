
import torch
import json
from torchvision import transforms
from PIL import Image

from app.model import PlantCNN

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = PlantCNN()
model.load_state_dict(
    torch.load("models/best_model.pth", map_location=device)
)
model.to(device)
model.eval()

with open("models/class_to_idx.json", "r") as f:
    class_to_idx = json.load(f)

idx_to_class = {int(v): k for k, v in class_to_idx.items()}

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


def predict_image(image: Image.Image):
    image = image.convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted = probabilities.max(1)

    confidence_value = confidence.item() * 100

    if confidence_value < 70:
        return {
            "disease": "Uncertain - please upload a clear plant leaf image",
            "confidence": round(confidence_value, 2)
        }

    return {
        "disease": idx_to_class[predicted.item()],
        "confidence": round(confidence_value, 2)
    }
