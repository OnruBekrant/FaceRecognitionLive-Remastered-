import insightface
import numpy as np
import cv2
from PIL import Image
import io

# Modeli yükle (ilk seferde indirir)
model = insightface.app.FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
model.prepare(ctx_id=0)

def recognize_face(image_file):
    # Resmi oku (byte -> np.array)
    image = Image.open(image_file.stream).convert("RGB")
    img_np = np.array(image)

    # Yüz algılama ve tanıma
    faces = model.get(img_np)

    if len(faces) == 0:
        return {"error": "No face detected"}

    # İlk yüzün embedding'ini al (512 boyutlu)
    embedding = faces[0].embedding.tolist()

    return {
        "message": "Face recognized (demo)",
        "embedding_sample": embedding[:5]  # örnek olarak ilk 5 değeri göster
    }

def extract_embedding(image_file):
    image = Image.open(image_file.stream).convert("RGB")
    img_np = np.array(image)
    faces = model.get(img_np)

    if not faces:
        return None

    return faces[0].embedding
