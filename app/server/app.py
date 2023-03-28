from fastapi import FastAPI
# from dotenv import dotenv_values
# from pymongo import MongoClient

# Database
# from app.server.routes import router as CustomerRouter
from .routes import router as CustomerRouter

app = FastAPI()

# @app.on_event("startup")
# def startup_db_client():
#     app.mongodb_client = MongoClient(config["ATLAS_URI"])
#     app.database = app.mongodb_client[config["DB_NAME"]]

# @app.on_event("shutdown")
# def shutdown_db_client():
#     app.mongodb_client.close()

# customer route
app.include_router(CustomerRouter, tags=["Customer"], prefix="/customer")


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Created by Ahmad Akmal Sabri"}