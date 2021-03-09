celery -A apps.tasks worker --beat  --loglevel=info
python manage.py shell < internal_scripts/email_call.py