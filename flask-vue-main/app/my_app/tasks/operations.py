# my_app/tasks/operations.py
from my_app.extensions import db
from my_app.tasks import models

def getById(id: int):
    task = db.session.get(models.Task, id)
    return task

def getAll():
    return db.session.query(models.Task).all()

def create(name: str):
    taskdb = models.Task(name=name)
    db.session.add(taskdb)
    db.session.commit()
    return taskdb

def update(id: int, name: str):
    taskdb = getById(id)
    if not taskdb:
        return None
    taskdb.name = name
    db.session.commit()
    return taskdb

def delete(id: int):
    taskdb = getById(id)
    if not taskdb:
        return False
    db.session.delete(taskdb)
    db.session.commit()
    return True

def pagination(page:int=1, per_page:int=10):
    return models.Task.query.paginate(page=page, per_page=per_page)