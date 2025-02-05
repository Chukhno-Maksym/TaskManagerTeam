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

Run tests:
    `python manage.py test`