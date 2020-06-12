import os

from celery import Celery
from dynaconf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery()
# dyno - для второго процесса на хероку
# см procfile woker
# а локально просто запускать через 2 консоли
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **_kwargs):
    from periodic import tasks

    sender.add_periodic_task(
        settings.CELERY_BEAT_INVITATION,
        tasks.invite_all_users.s(),
        name=tasks.invite_all_users.__name__,
    )

    sender.add_periodic_task(
        45,
        tasks.tg_send.s(),
        name=tasks.tg_send.__name__,
    )

    """sender.add_periodic_task(  # создали новую задачу
    60,
        tasks.sync_c.s(),
        name=tasks.invite_all_users.__name__,
    )"""
