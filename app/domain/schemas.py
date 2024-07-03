from pydantic import BaseModel, Field, ConfigDict

class User(BaseModel):
    email :str
    hashed_password:str
    fullname:str
    rol:str

class Token(BaseModel):
    access_token: str
    token_type: str

class Ingredient(BaseModel):
    fullname:str
    Almacen:str
    Cantidad:str