# Task Manager FastAPI
Real-time task manager for my FastAPI course
https://stepik.org/course/179694/

Task Manager FastAPI is a simple task management API built using FastAPI. 
It provides basic CRUD (Create, Read, Update, Delete) operations for tasks and includes real-time updates for task status changes via WebSocket.

This task manager is deliberately made not completely asynchronous in order for students to complete the Final project on their own. It also uses at least 4 deprecated methods for the same purposes. To improve, it is necessary to make asynchronous work with databases and update the endpoints code.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Testing with SwaggerUI](#testing-the-api-with-swagger-ui)
- [Testing with pytest](#testing-the-api-with-pytest-framework)
- [Potential Improvements](#potential-improvements)
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
├── tests/
├── .env
├── .gitignore
├── alembic.ini
├── README.md
├── main.py
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
- PostgreSQL.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Cheater121/task_manager_fastapi.git
   cd task_manager_fastapi
   ```

2. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
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


## Testing the API with Swagger UI

Fast API comes with Swagger UI. This tool is automatically generated based on your API's route definitions and Pydantic models.

### Accessing Swagger UI

Once the API is running, Swagger UI can be accessed on the following URL:

```bash
http://localhost:8000/docs
```

You can use swagger UI to:

1. **Browse Endpoints**
2. **Send Requests**
3. **View Responses**
4. **Test Validations**

**To Test with SwaggerUI, you can do the following for each endpoint explained above**

1. Open your web browser and navigate to the /docs path as mentioned above.

2. Explore the available endpoints and select the one you want to test.

3. Click on the "Try it out" button to open an interactive form where you can input data.

4. Fill in the required parameters and request body (if applicable) according to the API documentation given above.

5. Click the "Execute" button to send the request to the API.

6. The response will be displayed below, showing the status code and response data.

7. You can also view example request and response payloads, which can be helpful for understanding the expected data format.

## Testing the API with pytest Framework

A suite of `tests` using the pytest framework was used to help verify the functionality of the Task Manager FastAPI.

### Running the tests

1. Navigate to the `task_manager_fastapi` (root) directory using a terminal:

```bash
cd <your_path_to_project>/task_manager_fastapi
```

2. Run the tests by executing the following command (don't forget to activate your virtual environment if used):

```bash
pytest
```

This command will automatically discover and run the test cases defined in the `tests` directory.

## Potential Improvements

Enhance your Task Manager FastAPI project with the following potential improvements:

1. **Asynchronous Database Operations and Route Handlers**:
   - Utilize asynchronous database drivers like `asyncpg` for faster database access.
   - Rewrite route handlers as asynchronous to fully leverage FastAPI's asynchronous capabilities for better performance.

2. **Task Prioritization and Deadlines**:
   - Allow users to set task priorities (e.g., high, medium, low).
   - Implement deadlines and reminders for tasks, potentially using BackgroundTasks or Celery.
   - Create sorting mechanisms for tasks based on priority and deadlines.

3. **User Profile Management and User-Specific Tasks**:
   - Develop user profile management to enable users to update their information.
   - Associate tasks with specific users, allowing each user to see only their tasks.

4. **Task Assignment to Users or Groups**:
   - Enable task assignments to individual users or groups.
   - Implement notifications for task assignments.
   - Allow users to delegate tasks to others.

5. **User Roles and Role-Based Access Control (RBAC)**:
   - Introduce user roles (e.g., admin, manager, user) to control access.
   - Implement Role-Based Access Control (RBAC) for fine-grained access control.

6. **Test Expansion and Integration Tests**:
   - Expand unit tests to cover edge cases and scenarios.
   - Develop integration tests to validate interactions between components.
   - Create a test database for isolated and secure testing.

7. **Advanced Logging and Error Handling**:
   - Enhance logging by categorizing log messages (info, warnings, errors).
   - Implement structured logging for better analysis.
   - Improve error handling for user-friendly error messages.

8. **Database Layer Separation or Design Patterns**:
   - Consider separating database operations into a dedicated layer or applying a design pattern like the repository pattern.
   - Modularize components into separate services for a microservices approach.

9. **Security Enhancement with Cookies and Refresh Tokens**:
   - Implement secure cookies for browser-based sessions.
   - Generate and validate refresh tokens for enhanced security.
   - Implement token expiration and renewal mechanisms.

10. **Scalability and Performance Optimization**:
    - Optimize database queries and indexes for improved performance.
    - Introduce caching mechanisms (e.g., Redis) for frequently accessed data.
    - Explore containerization and orchestration for scalable deployment.

11. **User-Friendly Documentation**:
    - Improve API documentation using tools like Swagger UI or ReDoc.
    - Provide detailed explanations and examples for API endpoints.
    
12. **Internationalization and Localization**:
    - Enable multi-language support for the application.
    - Allow users to select their preferred language.

13. **User Feedback and Notifications**:
    - Implement a feedback system for users to report issues and suggestions.
    - Add notification features such as email or in-app alerts for important updates.

These potential improvements can enhance the functionality, scalability, and user experience of your Task Manager FastAPI project. Prioritize them based on project goals and user needs.


## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and test thoroughly.
4. Create a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
