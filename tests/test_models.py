from sqlalchemy.orm import Session

from app.api.models.task import TaskCreate
from app.api.models.user import UserCreate
from app.db.db_structure import Task, User

db = Session()


def test_create_task():
    task_data = {"title": "Test Task", "description": "Test Task creation"}
    task = TaskCreate(**task_data)
    assert task.title == "Test Task"
    assert task.description == "Test Task creation"


def test_create_user():
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    user = UserCreate(**user_data)
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.password == "testpassword"


def test_create_task_in_db():
    task_data = {"title": "Test Task", "description": "Test for testing", "completed": False}
    task = Task(**task_data)
    db.add(task)
    db.commit()
    db_task = db.query(Task).filter(Task.title == "Test Task").first()
    assert db_task is not None
    assert db_task.title == "Test Task"
    assert db_task.completed is False


def test_create_user_in_db():
    user_data = {"username": "testuser", "email": "test@example.com", "hashed_password": "testhashed"}
    user = User(**user_data)
    db.add(user)
    db.commit()
    db_user = db.query(User).filter(User.username == "testuser").first()
    assert db_user is not None
    assert db_user.username == "testuser"
    assert db_user.email == "test@example.com"
    assert db_user.hashed_password == "testhashed"
