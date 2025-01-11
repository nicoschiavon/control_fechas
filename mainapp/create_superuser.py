from django.contrib.auth import get_user_model

User = get_user_model()

username = "nico"
email = "nico.schiavon@gmail.com"
password = "Support01!"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully.")
else:
    print(f"Superuser '{username}' already exists.")
