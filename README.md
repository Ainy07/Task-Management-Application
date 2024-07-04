# Task-Management-Application


This is a Task Management Application developed using Django for the back-end and HTML, CSS, and JavaScript for the front-end. It allows users to manage their tasks with features like task creation, editing, and deletion.

### Table of Contents
 [Features](#Features)
 [Installation](#Installation)
 [Usage](#Usage)
 [APIDocumentation](#APIDocumentation)
 [Contributing](#Contributing)
 [License](#License)


## Features
1. Landing page displaying a list of tasks
2. Ability to add new tasks with a title, description, and due date
3. Detailed information view for each task
4. Edit existing tasks
5. Delete tasks
6. Responsive design for desktop and mobile devices


### Installation
Clone the repository:

```bash
Copy code
git clone https://github.com/Ainy07/Task_Management_Application.git
```
## Install dependencies:

```bash
Copy code
cd task-management-app
pip install -r requirements.txt
```
### Usage
Run the Django server:

```bash
Copy code
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000.

### API Documentation
The API endpoints for this application are as follows:

1. GET /api/list/task/: Retrieve all tasks
2. POST /api/create/task/: Create a new task
3. GET /api/retriever/task/<int:pk>/: Retrieve a single task by its ID
4. PUT /api/update/task/<int:pk>/: Update an existing task
5. DELETE /api/delete/task/<int:pk>/: Delete a task

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
