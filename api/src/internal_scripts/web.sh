python manage.py migrate && python manage.py shell < internal_scripts/initialize_environment.py && gunicorn wsgi