from fastapi import FastAPI  # FASTAPI should be FastAPI (case-sensitive)
import json

app = FastAPI()

def load_data():
    with open('patient.json','r') as f:
      data = json.load(f)

      return data

@app.get("/")
def hello():
    return {"message": "Patient management system API"}


@app.get("/about")
def about():
    return {"message":"Fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()

    return data