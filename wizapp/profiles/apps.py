from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'


    def ready(self):
        from django.contrib.auth import get_user_model
        User = get_user_model()
        from .models import CustomUser
        if User != CustomUser:
            setattr(User, 'is_admin', property(lambda self: self.is_superuser))
