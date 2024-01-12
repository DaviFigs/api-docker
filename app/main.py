from fastapi import FastAPI

app = FastAPI()

@app.get('/add_task')
def add_task(name_task:str,importance:int):
    pass