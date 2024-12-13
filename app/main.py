from fastapi import FastAPI

# Create an instance of the FastAPI app
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# To run the server, use the command: uvicorn filename:app --reload
# Replace 'filename' with the name of your Python file (without the .py extension).