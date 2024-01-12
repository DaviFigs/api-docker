from fastapi import FastAPI

app = FastAPI()

#list all tasks
@app.get('/list_tasks')
def view_tasks():
    pass


#adding and modifiyng tasks
@app.post('/add_task')
def add_task(name_task:str,importance:int):
    pass

@app.post('/modify_task')
def modify_task(task_id:int):
    pass

@app.post('/remove_task')
def remove_task(task_id:int):
    pass




