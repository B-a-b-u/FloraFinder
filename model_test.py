import tensorflow as tf
from PIL import Image
import numpy as np


model = tf.keras.models.load_model("models/1/1.keras")
print(model)

def predict(model,image):
    image = image.resize((256, 256))  
    image = np.array(image) / 255.0 
    image = np.expand_dims(image, axis=0)
    pred = np.array(model.predict(image))
    return pred


path = "Dataset/Indian Medicinal Leaves Image Datasets/Medicinal plant dataset/Arali/352.jpg"
image = Image.open(path)
print(image)
pred = predict(model,image)
print(pred)