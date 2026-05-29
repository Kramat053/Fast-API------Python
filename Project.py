from fastapi import FastAPI,Path,HTTPException
import json
app  = FastAPI()

def load_data():
    with open ("patients.json",'r') as f:
        data = json.load(f)
    return data

@app.get("/")    
def hello():
    return {"message":"Patents Management System API"}

@app.get("/about")
def about():
    return {'message':'A fully functional API to manage patients data'}

@app.get("/view")
def view():
    data = load_data()
    return data

#Path Parameters
#It is a dynamic segment of a URL path used to identify a specific resource

@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description = 'ID of the patient in the DB', example = 'P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404, detail = 'Patient not found')

#
