# Create Rest API about customer information management 

This is a small project demonstrating how to build an API with FastAPI (python framework).



## Running the server

Create and activate your Python virtualenv, and then run the following from your terminal to install the required dependencies:

```
python -m pip install -r requirements.txt
```

Set your [Atlas URI connection string](https://docs.atlas.mongodb.com/getting-started/) as a parameter in `.env`. Make sure you replace the username and password placeholders with your own credentials.

```
ATLAS_URI=mongodb+srv://<username>:<password>@sandbox.jadwj.mongodb.net
```



Start the server:
```
python -m uvicorn main:app --reload
```


## Summary

| HTTP Method        | Route           | Description  |
| ------------- |:-------------:| -----|
| GET      | `/api/customers` | retrieve all customers data |
| POST      | `/api/customer`      |   add a new customer data |
| GET | `/api/customer/{id}`      |    get customer data |
| PUT  | `/api/customer/{id}`      |   update customer data |
| DELETE | `/api/customer/{id}`      |    delete customer data |

### Links created by FastAPI

| Link                        | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| http://127.0.0.1:8000/      | API root                                                             |
| http://127.0.0.1:8000/docs  | [Swagger UI](https://swagger.io/tools/swagger-ui/) API Documentation |
| http://127.0.0.1:8000/redoc | [ReDoc](https://redoc.ly/redoc) API Documentation                    |
