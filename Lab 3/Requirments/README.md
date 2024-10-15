# Task Manager API

This is a simple Flask-based API to manage tasks.

## Endpoints

| Method  | Endpoint              | Description                  |
|---------|-----------------------|------------------------------|
| GET     | `/tasks/`              | Retrieve all tasks            |
| GET     | `/tasks/{task_id}`     | Retrieve a specific task by ID |
| POST    | `/tasks/`              | Add a new task                |
| PUT     | `/tasks/{task_id}`     | Update a task by ID           |
| DELETE  | `/tasks/{task_id}`     | Delete a task by ID           |