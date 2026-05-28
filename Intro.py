#PYTHON API
#It is a set of rules and protocols that allows different software applications to communicate with each other. 
#APIs define how requests and responses should be structured, what data can be accessed, and how to authenticate and authorize access to the API.
#APIs are used to enable integration between different software systems, allowing them to share data and functionality.
#APIs can be used for a wide range of purposes, such as accessing data from a web service, integrating with third-party applications, or building custom applications that leverage existing services.

#FASTAPI
#It is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 
#FastAPI is designed to be easy to use and to provide high performance, making it a popular choice for building APIs in Python.
#FastAPI is a combination of starlette and pydantic libraries 
#Starlette handles how API receive requests and sends back responses   
#Pydantic checks data validation(correct data and format) while receiving

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello world'}

@app.get("/about")
def about():
    return {'message':'My name is you'}