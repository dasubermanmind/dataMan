from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def data():
    return {'message': "temp_data"}