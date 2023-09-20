from django.apps import AppConfig


class EmailSenderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'email_sender'

    def ready(self):
        import email_sender.signals   # Import signals when the app is ready
