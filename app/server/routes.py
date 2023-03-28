from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from .database import (    
                       
    retrieve_customer,
    retrieve_customers,
    add_customer,
    delete_customer,
    update_customer,
)

from .models import (
    ErrorResponseModel,
    ResponseModel,
    CustomerSchema,
    UpdateCustomerModel,
)

router = APIRouter()

# add customer
@router.post("/", response_description="Customer data added into the database")
async def add_customer_data(customer: CustomerSchema = Body(...)):
    customer = jsonable_encoder(customer)
    new_customer = await add_customer(customer)
    return ResponseModel(new_customer, "Customer added successfully.")

# retrieve customers data
@router.get("/", response_description="Customers retrieved")
async def get_customers():
    customers = await retrieve_customers()
    if customers:
        return ResponseModel(customers, "Customers data retrieved successfully")
    return ResponseModel(customers, "Empty list returned")

# retrieve customer data
@router.get("/{id}", response_description="Customer data retrieved")
async def get_customer_data(id):
    customer = await retrieve_customer(id)
    if customer:
        return ResponseModel(customer, "Customer data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Customer doesn't exist.")

# update customer data
@router.put("/{id}")
async def update_customer_data(id: str, req: UpdateCustomerModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_customer = await update_customer(id, req)
    if updated_customer:
        return ResponseModel(
            "Customer with ID: {} name update is successful".format(id),
            "Customer name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the customer data.",
    )

# delete customer data
@router.delete("/{id}", response_description="Customer data deleted from the database")
async def delete_customer_data(id: str):
    deleted_customer = await delete_customer(id)
    if deleted_customer:
        return ResponseModel(
            "Customer with ID: {} removed".format(id), "Customer deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Customer with id {0} doesn't exist".format(id)
    )