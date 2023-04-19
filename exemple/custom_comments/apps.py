from django.apps import AppConfig


class CustomCommentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "exemple.custom_comments"

    def ready(self):
        import exemple.custom_comments.receivers
