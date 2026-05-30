# ✅ Task Manager

A lightweight task management web application built with **Django**. Create, view, complete, and delete tasks through a clean, straightforward interface.

## 🚀 Features

- View all tasks in a list
- Create new tasks with a title and description
- View individual task details
- Mark tasks as completed
- Delete tasks
- Flash messages for user feedback

## 🛠️ Tech Stack

| Layer      | Technology          |
|------------|---------------------|
| Language   | Python 3.9+         |
| Framework  | Django ≥ 3.2        |
| Database   | SQLite              |
| Templating | Django Templates    |

## 📁 Project Structure

\`\`\`
shivam20-tech-taskmanager/
├── TaskManagerProject/
│   ├── manage.py
│   ├── requirements.txt
│   ├── TaskManagerProject/       # Project config (settings, urls, wsgi)
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── tasks/                    # Core app
│       ├── models.py             # Task model
│       ├── views.py              # Business logic
│       ├── migrations/           # DB migrations
│       └── templates/tasks/      # HTML templates
\`\`\`

## ⚙️ Getting Started

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/your-username/shivam20-tech-taskmanager.git
   cd shivam20-tech-taskmanager/TaskManagerProject
   \`\`\`

2. **Create and activate a virtual environment**
   \`\`\`bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Apply database migrations**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Run the development server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

6. Open your browser and visit: [http://localhost:8000](http://localhost:8000)

## 🗺️ URL Routes

| URL                    | View            | Description              |
|------------------------|-----------------|--------------------------|
| `/`                    | `task_list`     | List all tasks           |
| `/task/<pk>/`          | `task_detail`   | View a task's details    |
| `/create/`             | `task_create`   | Create a new task        |
| `/complete/<pk>/`      | `task_complete` | Mark a task as completed |
| `/delete/<pk>/`        | `task_delete`   | Delete a task            |
| `/admin/`              | Django Admin    | Admin panel              |

## 🗄️ Data Model

```python
class Task(models.Model):
    title       = CharField(max_length=255)
    description = TextField()
    completed   = BooleanField(default=False)
```

## 🔒 Security Notes

> This project is configured for **development only**.

- `DEBUG = True` — must be set to `False` in production
- `SECRET_KEY` is hardcoded — move it to an environment variable before deploying
- `ALLOWED_HOSTS = []` — add your domain/IP before deploying

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)