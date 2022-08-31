from django.apps import AppConfig


class CbuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cbu'

    def ready(self):
        from cbu import signals