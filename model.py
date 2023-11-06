import tensorflow.keras.models as tfkm
from io import BytesIO
import numpy as np
from PIL import Image

model = None


def load_model():
    model = tfkm.load_model("vitiligoDetector.keras")
    print("Model loaded")
    return model


def predict(image: Image.Image):
    global model
    if model is None:
        model = load_model()

    image = np.asarray(image.resize((256, 256)))[..., :3]
    image = image / 255
    image = np.expand_dims(image, 0)
    result = model.predict(image)[0, 0].item()
    print(result)
    return {"result": result}


def read_imagefile(file) -> Image.Image:
    image = Image.open(BytesIO(file))
    return image
