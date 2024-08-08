# NexGenFlow
Installation
Prerequisites
Python 3.8+
Django 3.1+
pip (Python package installer)
Git (for version control)
Setup:

Clone the repository

Create a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file for environment variables:

bash
Copy code
touch .env
Add your environment-specific variables to the .env file.

Apply migrations and create a superuser:

bash
Copy code
python manage.py migrate
python manage.py createsuperuser
Run the development server:

bash
Copy code
python manage.py runserver
Access the application:

Open your web browser and navigate to http://127.0.0.1:8000.

Usage:

User Registration:
Navigate to the registration page and create a new account.
Log in with your new account credentials.
Visualization:
Once logged in, you can view the water distribution network visualization on the main dashboard.
Optimization:
Navigate to the optimization section.
Select the desired optimization algorithm (Edmonds-Karp, Ford-Fulkerson, Dinic's, or Push-Relabel).
Run the optimization to view the results and visualize the optimized path.

Project Structure

waterflow/
│
├── manage.py
├── waterflow/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── water/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── requirements.txt

Contributing:
We welcome contributions! If you would like to contribute, please fork the repository and create a pull request with your changes.

License:
This project is licensed under the MIT License.
