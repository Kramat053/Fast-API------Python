#Pydantic
#It is a python library for data validation
#It includes fields its data types and any condition to that field
#Then validation is done along with coercing into correct data types
#Now passing the object

from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 characters',examples=['Naeem','Ali'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0,lt=120)
    weight: Annotated[float,Field(gt=0, strict=True)]
    married: Annotated[bool,Field(default=None,description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_details: Dict[str,str]
    
def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')
 
patient_info = {'name':'Ali','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/123','age':'30','weight':75.2,'contact_details':{'phone':'5752652'}}  

patient1 = Patient(**patient_info)    

update_patient_data(patient1)
          