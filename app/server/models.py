from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class CustomerSchema(BaseModel):
    fullname: str = Field(...)
    address: str = Field(...)
    email: EmailStr = Field(...)
    occupation: str = Field(...)
    age: int = Field(..., gt=0, lt=120)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Ahmad Akmal",
                "address":" Cyberjaya, Selangor",
                "email": "akmalsabri90@gmail.com",
                "occupation": "Data Scientist",
                "age": 33,
            }
        }


class UpdateCustomerModel(BaseModel):
    fullname: Optional[str]
    address: Optional[str]
    email: Optional[EmailStr]
    occupation: Optional[str]
    age: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Ahmad Akmal",
                "address":" Cyberjaya, Selangor",
                "email": "akmalsabri90@gmail.com",
                "occupation": "Data Scientist",
                "age": 32,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}