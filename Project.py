from fastapi import FastAPI,Path,HTTPException,Query
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

#Query Parameters
#It is an optional key=value pairs appended to the end of a URL to pass additional data to the server in an HTTP request
#It is used for filtering,sorting,searching

@app.get("/sort")
def sort_patients(sort_by:str = Query(...,description = 'Sort on the basis of age'),order:str = Query('asc',description = 'Sort in asc or desc order')):
    valid_fields = ['age']
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = 'Invalid field select from {valid_fields}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = 'Invalid order select between asc or desc')
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by,0),reverse = sort_order)
    return sorted_data
    


