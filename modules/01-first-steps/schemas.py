#This file defines the Pydantic schema for the Car model used in the FastAPI application.
#This schema is used to validate and serialize car data in the API.
#Pydantic is used for data validation and serialization in FastAPI applications.

from pydantic import BaseModel
class Car(BaseModel):
    id: int
    size: str
    fuel: str |None ="electric"
    doors: int |None =4
    transmission: str |None ="manual"
