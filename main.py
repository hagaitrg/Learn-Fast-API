from fastapi import FastAPI

app = FastAPI()

grades = {
    1: {
        "name" : "dimas",
        "class" : "SI-42-08",
        "nim" : "1202184323",
        "grade" : "90"
    }
}

@app.get("/get-item/{item_id}")
def get_data(item_id: int):
    return grades[item_id]
