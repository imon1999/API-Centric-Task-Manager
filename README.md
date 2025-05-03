# API Centric(FastAPI) Task Manager 

## Description

This is a simple Task Manager API built using Python and FastAPI. It allows you to manage tasks by creating, reading, updating, and deleting them.

## Features

* **Create Task:** Add a new task to the list.
* **Read Tasks:** Retrieve a list of all tasks, with optional filtering and pagination.
* **Read Task:** Retrieve a single task by its ID.
* **Update Task:** Modify an existing task.
* **Delete Task:** Remove a task from the list.
* **API Documentation:** Interactive API documentation using Swagger UI is automatically generated at `/docs` when the application is running.

## Technologies Used

* [FastAPI](https://fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+.
* [Pydantic](https://pydantic-docs.github.io/): Used for data validation and settings management.
* [Uvicorn](https://www.uvicorn.org/): An ASGI server for running the FastAPI application.

## Requirements

* Python 3.7 or higher
* pip (Python package installer)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd api_task_manager
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install fastapi uvicorn[standard]
    ```

## Running the Application

1.  Run the application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```

2.  The API will be accessible at `http://localhost:8000`.

3.  The interactive API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

## Usage

### Interacting with the API

You can use any HTTP client (e.g., `curl`, Postman, a web browser) to interact with the API.

#### Endpoints

* **Create a task (POST):**

    ```
    POST /tasks/
    ```

    Request body (JSON):

    ```json
    {
        "title": "Task title",
        "description": "Task description",
        "completed": false
    }
    ```

    Example using `curl`:

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Grocery Shopping", "description": "Buy milk, eggs, and bread", "completed": false}' http://localhost:8000/tasks/
    ```

* **Get all tasks (GET):**

    ```
    GET /tasks/
    ```

    Optional query parameters:

    * `skip`: Number of tasks to skip (default: 0).
    * `limit`: Maximum number of tasks to return (default: 10, max: 100).
    * `completed`: Filter tasks by completion status (true or false).

    Example using `curl`:

    ```bash
    curl http://localhost:8000/tasks/?skip=0&limit=10&completed=false
    ```

* **Get a single task (GET):**

    ```
    GET /tasks/{task_id}
    ```

    Example using `curl`:

    ```bash
    curl http://localhost:8000/tasks/1
    ```

* **Update a task (PUT):**

    ```
    PUT /tasks/{task_id}
    ```

    Request body (JSON):

    ```json
    {
        "title": "Updated task title",
        "description": "Updated task description",
        "completed": true
    }
    ```

     Example using `curl`:

    ```bash
    curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Grocery Shopping", "description": "Buy milk, eggs, and bread and cheese", "completed": true}' http://localhost:8000/tasks/1
    ```

* **Delete a task (DELETE):**

    ```
    DELETE /tasks/{task_id}
    ```

    Example using `curl`:

    ```bash
    curl -X DELETE http://localhost:8000/tasks/1
    ```

---
