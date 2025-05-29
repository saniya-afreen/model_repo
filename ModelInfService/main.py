# app.py
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from torchvision import models, transforms
from PIL import Image
import torch
import io
import json
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Model Inferenece Service is Up!"}



# Load ResNet18 pre-trained model
model = models.resnet18(pretrained=True)
model.eval()

# Define image transforms
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # ImageNet normalization
        std=[0.229, 0.224, 0.225]
    )
])

# Load class labels (ImageNet)
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
imagenet_classes = requests.get(LABELS_URL).text.strip().split('\n')

@app.get("/")
def read_root():
    return {"Model Inferenece Service is Up!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        img_t = transform(image)
        batch_t = torch.unsqueeze(img_t, 0)

        with torch.no_grad():
            out = model(batch_t)
            _, index = torch.max(out, 1)
            predicted_label = imagenet_classes[index.item()]

        return JSONResponse(content={"class": predicted_label})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
