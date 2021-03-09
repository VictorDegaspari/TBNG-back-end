from django.contrib.auth.models import User

if User.objects.count() == 0:
    print("Criando novo usuário..")
    User.objects.create_superuser('admin', 'admin@triniti.com.br', 'admin')
else:
    print("Usuário já criado.")