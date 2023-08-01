from fastapi import FastAPI
from pydantic import BaseModel
import os, io
from app.core.settings import get_settings
import cv2
import base64
import numpy as np
from PIL import Image
from typing import List
from app.modules.user_analyst.user_analyst_processing import deepface_processing

settings = get_settings()

app = FastAPI()

path_temp = settings.TEMP_PATH
src_folder_name = settings.SCR_FOLDER_NAME
src_folder_path = f'{path_temp}/{src_folder_name}'

if not os.path.exists(src_folder_path):
    os.makedirs(src_folder_path)

class Item(BaseModel):
    images: List[str]
    isRequire_analys: bool

@app.post("/api/v1/object-analysis/")
async def create_item(item: Item):
    status = 200
    print(item.isRequire_analys)
    images = []
    try:
        for i, image_data in enumerate(item.images):
            decoded_image = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(decoded_image))
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            images.append(image)
            cv2.imwrite(f"{src_folder_path}/{i}.jpg", image)
            
    except Exception as e:
        print(e)
        status = 400
        
    return {"status": status}

result = deepface_processing(db_path="/home/cuongacpe/Documents/AI-Chatbot-Synthesis/app/modules/user_recognition/user/database",
                                 models="Facenet", distances='euclidean_l2',flag=True)
print(result)
