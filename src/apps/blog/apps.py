from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = "apps.blog"  # путь к приложухе
    label = "blog"  # для админки и нэймспейса в урлах
