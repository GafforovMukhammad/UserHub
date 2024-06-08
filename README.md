# UserHub

UserHub is a Django-based web application designed for managing user data. This project includes features for creating and managing users, and it demonstrates the use of Django's powerful ORM for database operations. Additionally, it leverages the Faker library to populate the database with realistic fake data for testing and development purposes.

## Features

- User Management: Create, read, update, and delete user records.
- Database Seeding: Automatically populate the database with fake user data using the Faker library.
- Template Rendering: Display user data in HTML templates with Django's template engine.
- Organized Codebase: Structured following Django best practices, ensuring a clean and maintainable project.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/GafforovMukhammad/userhub.git

   cd userhub
  python -m venv myenv
  source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

  pip install -r requirements.txt

  python manage.py makemigrations
  python manage.py migrate

  python manage.py runserver


