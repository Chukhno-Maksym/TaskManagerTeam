# TaskManagerTeam

TeamTaskManager is a Django-based web application designed to help manage tasks, teams, and users within an
organization. It allows users to create, update, and delete tasks, assign them to different team members, and filter
tasks based on different criteria such as priority, team, and status.

Features:
* Users can register, update their profiles, and delete their accounts.
* The app uses Django’s built-in user model extended with custom fields like team and position for workers. 
* Users can create, update, and delete tasks.
* Tasks can be assigned to workers and have attributes such as name, description, deadline, priority, and status.
* Tasks can be filtered based on criteria like team, status, and priority.
* Tasks can be marked as completed or undone.

Models
* Team: Represents a team within the organization.
* Position: Represents the position of a worker (e.g., Developer, Designer).
* Worker: Extends Django’s built-in AbstractUser model with fields like position and team.
* TaskType: Represents the type of a task (e.g., Feature, Bug, Improvement).
* Task: Represents a task with fields like name, description, deadline, is_completed, priority,
assignees, and task_type.

# Project Setup Instructions

### 1. **Fork the Repository**

- Go to the repository on GitHub.
- Click the **Fork** button in the upper-right corner to create your own copy of the repository.

### 2. **Clone the Forked Repository**

- Copy the link to your fork by clicking the **Clone or download** button in your repository.
- Use the following command to clone the repository:

```git clone <link-from-your-forked-repo>```

- Replace <link-from-your-forked-repo> with the copied link.

### Create a Branch for Your Solution and Switch to It
Open the terminal in your IDE or project directory, and run the following command:

    git checkout -b develop

### Create a Virtual Environment
If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:

    python -m venv venv
    venv\Scripts\activate (on Windows)
    source venv/bin/activate (on macOS)
    pip install -r requirements.txt

### Run tests:
    python manage.py test

Create a .env file in the project's root directory and add the following:

### Database configuration
    POSTGRES_DB=<db_name>               # Name of the PostgreSQL database
    POSTGRES_DB_PORT=<db_port>          # Database port, usually 5432
    POSTGRES_USER=<db_user>             # PostgreSQL user
    POSTGRES_PASSWORD=<db_password>     # Database password
    POSTGRES_HOST=<db_host>             # Database host, usually localhost or a server address

### Django settings
    SECRET_KEY=<secret_key>             # Django secret key for encryption
    DJANGO_SETTINGS_MODULE=<path_to_settings_file>  # Path to Django settings, e.g., myproject.settings
    RENDER_EXTERNAL_HOSTNAME=<domain>   # Deployment domain (optional)

### You can load base data into the database from a fixture using the following command:
    python manage.py loaddata initial_data.json

### You cat use a test user to see the features.
* login: testuser
* password: 1qazcde3
