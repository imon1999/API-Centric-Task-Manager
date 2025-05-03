from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# Data model using Pydantic
class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=200)
    description: str = Field("", max_length=1000)  # Added description
    completed: bool = False

# In-memory task storage (for simplicity - use a database for persistence)
tasks: List[Task] = []
next_task_id = 1

# --- API Endpoints ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API.  See /docs for API documentation."}


@app.get("/tasks/", response_model=List[Task])
def read_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
) -> List[Task]:
    """
    Retrieves a list of tasks, with optional filtering, skipping, and limiting.

    Args:
        skip: Number of tasks to skip.
        limit: Maximum number of tasks to return.
        completed: Optional filter to show only completed or incomplete tasks.

    Returns:
        A list of tasks.
    """
    filtered_tasks = tasks
    if completed is not None:
        filtered_tasks = [task for task in tasks if task.completed == completed]
    return filtered_tasks[skip : skip + limit]

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int) -> Task:
    """
    Retrieves a specific task by its ID.

    Args:
        task_id: The ID of the task to retrieve.

    Returns:
        The task with the given ID.

    Raises:
        HTTPException: 404 if the task is not found.
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: Task) -> Task:
    """
    Creates a new task.

    Args:
        task: The task to create.

    Returns:
        The created task with its ID.
    """
    global next_task_id
    task.id = next_task_id
    tasks.append(task)
    next_task_id += 1
    return task


@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int) -> Task:
    """
    Deletes a task by its ID.

    Args:
        task_id: The ID of the task to delete.

    Returns:
        The deleted task.

    Raises:
        HTTPException: 404 if the task is not found.
    """
    global tasks
    task_index = -1
    for i, t in enumerate(tasks):
        if t.id == task_id:
            task_index = i
            break
    if task_index == -1:
        raise HTTPException(status_code=404, detail="Task not found")
    deleted_task = tasks.pop(task_index)
    return deleted_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task) -> Task:
    """
    Updates a task by its ID.

    Args:
        task_id: The ID of the task to update.
        updated_task: The updated task data.

    Returns:
        The updated task.

    Raises:
        HTTPException: 404 if the task is not found.
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    # Update the task fields individually.
    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed
    return task