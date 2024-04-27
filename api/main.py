# Import fast api
from fastapi import FastAPI, UploadFile, File
import uvicorn
from io import BytesIO
from PIL import Image
import numpy as np
from  plant_medicinal_data import Plant_Details

app = FastAPI() # Creating a instance

food_items = {
    "Indian" : ["dosa","Biriyani"],
    "Japanese" : ["Dumplings","rice ball"],
    "USA" : ["pizza","burgar"],
}

# Endpoint
@app.get("/")
async def home():
    return "Hello World!"

@app.get("/items/{cuisine}")
async def item_menu(cuisine : str):
    if cuisine not in food_items:
        return f"Only available cuisines are {list(food_items.keys())}"
    return  food_items.get(cuisine)

def read_file_as_image(data):
    return np.array(Image.open(BytesIO(data)))


@app.post("/predict")
async def predict(file : UploadFile = File(...)):
    image = read_file_as_image( await file.read())
    image_batch= np.expand_dims(image,0)
    print(image_batch[0].shape)
    return "file uploaded"


@app.get("/{plant}")
async def get_plant(plant):
    plant = Plant_Details.get(plant.strip())[0]
    if plant:
        return f"""{plant["scientific_name"]}  {plant["scientific_medicinal_properties"]}
{plant["common_location"]}
{plant["popular_usecase"]}
{plant["Disclaimer"]}
{plant["lament_medicinal_property"]}"""
    else:
        return f"Plant not found"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)