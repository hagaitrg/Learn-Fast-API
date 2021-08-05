from enum import Enum
from fastapi import FastAPI


app = FastAPI()

class ModelName(str, Enum):
    framework = "framework"
    lang = "lang"
    db = "db"

class Students():
    grades = {
    1: {
        "name" : "dimas",
        "class" : "SI-42-08",
        "nim" : "1202184323",
        "grade" : "90"
    }
}

@app.get("/users/me")
def get_current_user():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")
def get_user(user_id:int):
    return {"user_id" : user_id}


@app.get("/get-item/{item_id}")
def get_data(item_id: int):
    return Students.grades[item_id]

@app.get("/models/{model_name}")
def get_model(model_name:ModelName):
    if model_name is ModelName.framework:
        return {"model_name" : model_name ,"message" : "i often use Laravel for building Web App"}
    if model_name is ModelName.lang:
        return {"model_name" : model_name, "message" :"i often use Python for logical coding"}
    return {"model_name" : model_name, "message":"i often use MySQL for building any App"}
