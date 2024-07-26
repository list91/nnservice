
from fastapi import FastAPI, Header, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
import shutil
import os
from stack_queue import StackQueue
import random
import string
import time
import nn
import cv2

queue = StackQueue()
app = FastAPI()

def nn_work(fn):
    res = nn.detect_people("/home/user/nn_service/uploads/"+fn)
    cv2.imwrite("res_nn\\"+fn, cv2.cvtColor(res, cv2.COLOR_RGB2BGR))
    return "res_nn\\"+fn

def generate_random_string(length):
    letters_and_digits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def get_name():
    while 1:
        res = generate_random_string(19)
        if res not in os.listdir(upload_dir):
            return res

upload_dir = "uploads"

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # new_name = get_name() + ".jpg"
        new_name = "result.jpg"
        file_location = os.path.join(upload_dir, new_name)

        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        res_path = nn_work(new_name)

        return FileResponse(res_path, filename=new_name)
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Error uploading file", "detail": str(e)})