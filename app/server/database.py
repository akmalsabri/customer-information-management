import motor.motor_asyncio
from bson.objectid import ObjectId
from decouple import config


MONGO_DETAILS = config("MONGO_DETAILS")  # read environment variable

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.customers

customer_collection = database.customers_collection


# customer info, parsing from database query into python dict


def customer_info(customer) -> dict:      

        return {
        "id": str(customer["_id"]),
        "fullname": customer["fullname"],
        "address": customer["address"],
        "email": customer["email"],
        "occupation": customer["occupation"],
        "age": customer["age"],
    }


# crud operations


# Retrieve all customers data in the database
async def retrieve_customers():
    customers = []
    async for customer in customer_collection.find():
        customers.append(customer_info(customer))
    return customers


# Add a new customer into to the database
async def add_customer(customer_data: dict) -> dict:
    customer = await customer_collection.insert_one(customer_data)
    new_customer = await customer_collection.find_one({"_id": customer.inserted_id})
    return customer_info(new_customer)


# Retrieve a customer with a matching _id
async def retrieve_customer(id: str) -> dict:
    customer = await customer_collection.find_one({"_id": ObjectId(id)})
    if customer:
        return customer_info(customer)


# Update a customer with a matching _id
async def update_customer(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    customer = await customer_collection.find_one({"_id": ObjectId(id)})
    if customer:
        updated_customer = customer_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_customer:
            return True
        return False


# Delete a customer from the database
async def delete_customer(id: str):
    customer = await customer_collection.find_one({"_id": ObjectId(id)})
    if customer:
        await customer_collection.delete_one({"_id": ObjectId(id)})
        return True