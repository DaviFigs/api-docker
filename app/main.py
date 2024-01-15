from fastapi import FastAPI

app = FastAPI()

#list all tasks
@app.get('/list_tasks')
def view_tasks():
    pass


#adding and modifiyng tasks
@app.post('/add_task')
def add_task(name_task:str,importance:int):
    return{'message':'your task was added'}

@app.post('/change_state')
def modify_task(task_id:int):
    return {'message':'your task change state'}

@app.post('/remove_task')
def remove_task(task_id:int):
    return {'message':'your task was removed'}




