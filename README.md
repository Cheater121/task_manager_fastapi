# Task Manager FastAPI
Real-time task manager for my FastAPI course
https://stepik.org/course/179694/

Task Manager FastAPI is a simple task management API built using FastAPI. 
It provides basic CRUD (Create, Read, Update, Delete) operations for tasks and includes real-time updates for task status changes via WebSocket.

This task manager is deliberately made not completely asynchronous in order for students to complete the Final project on their own. It also uses at least 4 deprecated methods for the same purposes. To improve, it is necessary to make asynchronous work with databases and update the endpoint code.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User registration and authentication.
- CRUD operations for tasks (Create, Read, Update, Delete).
- Real-time updates for task status changes using WebSocket.
- OAuth2 authentication for API access.
- Simple and straightforward project structure.

## Project Structure

The project follows the following directory structure:

```
task_manager_fastapi/
├── app/
│   ├── alembic/
│   ├── api/
│   │   ├── endpoints/
│   │   ├── middleware/
│   │   ├── models/
│   ├── core/
│   ├── db/
│   ├── main.py
├── tests/
├── .env
├── .gitignore
├── alembic.ini
├── README.md
├── requirements.txt
```

- `app`: Contains the main application code.
  - `alembic`: Database migration files (if used).
  - `api`: Contains API endpoints for tasks and users.
    - `endpoints`: Task and user API endpoints.
    - `middleware`: Custom middleware (simple logging for example).
    - `models`: Pydantic models for request and response.
  - `core`: Core utilities and configurations.
  - `db`: Database configuration and models.
- `tests`: Unit tests.
- `.env`: Store environment variables (e.g., database credentials).
- `.gitignore`: Lists files and directories to be ignored by version control.
- `alembic.ini`: Alembic configuration (if used).
- `README.md`: Documentation about the project.
- `requirements.txt`: List of project dependencies.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.7+ (3.10+ recommended).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/cheater121/task_manager_fastapi.git
   cd task_manager_fastapi
   ```

2. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate.bat
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To run the FastAPI application locally, use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Replace `0.0.0.0` and `8000` with your desired host and port.

Or you can just run `main.py`:
```bash
python3 main.py
```

### API Endpoints

The API exposes the following endpoints:

- `POST /api/v1/users/register/`: Register a new user.
- `POST /api/v1/users/login/`: Authenticate and receive a JWT token.
- `GET /api/v1/about_me/`: Retrieve user info (protected endpoint).
- `GET /api/v1/tasks/`: Retrieve a list of tasks (protected endpoint).
- `POST /api/v1/tasks/`: Create a new task (protected endpoint).
- `GET /api/v1/tasks/{task_id}`: Retrieve a specific task (protected endpoint). 
- `PUT /api/v1/tasks/{task_id}`: Update a specific task (protected endpoint).
- `DELETE /api/v1/tasks/{task_id}`: Delete a specific task (protected endpoint). 

For real-time updates on task status changes, use WebSocket connections to `/ws/tasks/{client_id}`.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and test thoroughly.
4. Create a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
