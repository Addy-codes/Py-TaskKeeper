# Task Management System

This Django-based task management system allows users to create, list, update, and delete tasks, with support for bulk adding and deleting. Each task has a title and a completion status.

## Features

- **Create a new task**: Add tasks with a title and completion status.
- **List all tasks**: View all tasks stored in the system.
- **Get a specific task**: Retrieve details of a specific task.
- **Delete a task**: Remove a task from the system.
- **Edit a task**: Update the title and/or completion status of a task.
- **Bulk add tasks**: Add multiple tasks in a single request.
- **Bulk delete tasks**: Remove multiple tasks in a single request.

## Installation

### Prerequisites

- Python 3.6 or higher
- Django 3.0 or higher
- Django REST Framework

### Setting Up a Virtual Environment

1. Clone the repository to your local machine.
2. Navigate to the project directory and create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

### Installing Dependencies

Install the required packages using pip:

```bash
pip install django djangorestframework
```

### Database Migrations

Apply the database migrations to set up your database schema:

```bash
python manage.py migrate
```

### Running the Server

Start the Django development server:

```bash
python manage.py runserver
```

The API will be available at [http://localhost:8000/](http://localhost:8000/).

## Usage

### Endpoints

- **List/Create Tasks**: `GET` and `POST` `/tasks/`
- **Retrieve/Update/Delete Task**: `GET`, `PUT`, `PATCH`, and `DELETE` `/tasks/<int:pk>/`
- **Bulk Add Tasks**: `POST` `/tasks/bulk_add/`

![image](https://github.com/Addy-codes/Py-TaskKeeper/assets/72205091/6f018ecf-c54c-4da6-9a8f-77fa9d3540cd)


- **Bulk Delete Tasks**: `DELETE` `/tasks/bulk_delete/`

![image](https://github.com/Addy-codes/Py-TaskKeeper/assets/72205091/928e74bf-bf62-464b-a4d9-099654a17b22)



### Examples

- **Adding a New Task**:

  ```bash
  curl -X POST http://localhost:8000/tasks/ -H "Content-Type: application/json" -d '{"title": "New Task", "is_completed": false}'
  ```

- **Bulk Deleting Tasks**:

  ```bash
  curl -X DELETE http://localhost:8000/tasks/bulk_delete/ -H "Content-Type: application/json" -d '{"ids": [1,2,3]}'
  ```
