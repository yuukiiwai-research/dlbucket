from django.apps import AppConfig


class BucketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bucket'

    def ready(self):
        super().ready()
        from .tasks.task import start
        start()
