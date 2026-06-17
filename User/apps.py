from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'

    def ready(self):
        try:
            from django.contrib.auth.models import User

            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@test.com',
                    password='Admin@123'
                )

            if not User.objects.filter(username='provider').exists():
                User.objects.create_user(
                    username='provider',
                    email='provider@test.com',
                    password='Provider@123'
                )

            if not User.objects.filter(username='user').exists():
                User.objects.create_user(
                    username='user',
                    email='user@test.com',
                    password='User@123'
                )

        except Exception:
            pass
