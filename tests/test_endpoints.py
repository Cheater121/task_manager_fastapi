from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

jwt_token = None


def auth_header():
    global jwt_token
    return {"Authorization": f"Bearer {jwt_token}"}


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Real-Time Task Manager API"}


def test_create_user():
    response = client.post("/api/v1/register/", json={"username": "test", "password": "test", "email": "test@test.com"})
    assert response.status_code == 200
    assert "id" in response.json()
    assert "username" in response.json()
    assert "email" in response.json()


def test_login():
    global jwt_token
    headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
    response = client.post("/api/v1/login/", data={"username": "test", "password": "test"}, headers=headers)
    jwt_token = response.json().get("access_token")
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json().get("token_type") == "bearer"


def test_create_task():
    response = client.post("/api/v1/tasks/", json={"title": "New Task", "description": "some_text"}, headers=auth_header())
    assert response.status_code == 200
    task = response.json()
    assert "id" in task
    assert task["title"] == "New Task"
    assert task["completed"] is False


def test_read_tasks():
    response = client.get("/api/v1/tasks/", headers=auth_header())
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    assert len(tasks) > 0


def test_read_task():
    task_id = 1
    response = client.get(f"/api/v1/tasks/{task_id}", headers=auth_header())
    assert response.status_code == 200
    task = response.json()
    assert task["id"] == task_id


def test_read_invalid_task():
    invalid_task_id = 999
    response = client.get(f"/api/v1/tasks/{invalid_task_id}", headers=auth_header())
    assert response.status_code == 404
