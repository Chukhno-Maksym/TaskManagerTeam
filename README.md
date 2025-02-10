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

![img_9](https://github.com/user-attachments/assets/d0520319-b0e9-488b-9be3-8c706ff2f1eb)
![img_8](https://github.com/user-attachments/assets/80a98d2b-f865-4f5c-8c00-4b0c03bbcd05)
![img_7](https://github.com/user-attachments/assets/7bc0321d-9349-481a-bade-cb59cc3bdeec)
![img_6](https://github.com/user-attachments/assets/9514ff1e-540c-4ba6-aaaf-64b58c5a559d)
![img_5](https://github.com/user-attachments/assets/9df25326-eb3d-464c-bf1e-41f38dbb51fc)
![img_4](https://github.com/user-attachments/assets/47b44abe-8cee-4d0f-a77f-4a79d971b80e)
![img_3](https://github.com/user-attachments/assets/c665f85b-2e2d-4cf5-ae89-b1b5d7ff91a3)
![img_2](https://github.com/user-attachments/assets/5dfc4e53-d576-4727-bf8a-c7082438deff)
![img_1](https://github.com/user-attachments/assets/bb793389-a3b2-46e9-b352-f51d05b2b231)
![img](https://github.com/user-attachments/assets/cf6c0ea9-c679-495d-892a-ec679dfd6fe7)
