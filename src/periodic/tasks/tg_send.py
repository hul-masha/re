import requests
from django.db.models import Q
from dynaconf import settings

from periodic import tasks
from periodic.app import app


@app.task
def tg_send():  # pragma: no cover
    print(f"BEGIN | {tg_send.__name__}")
    # from apps.api.views import tg
    # print(tg)
    # for c in tg:
    try:
        from apps.blog.models import Post

        if all(
            i == True
            for i in list(map(lambda x: x.sending_tg == True, Post.objects.all()))
        ):
            r = requests.post(
                f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                json={"chat_id": 605985152, "text": "we haven't a new post=("},
            )
        else:
            for p in Post.objects.all():
                if p.sending_tg == None or p.sending_tg == False:
                    r = requests.post(
                        f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                        json={"chat_id": 605985152, "text": "we have a new post=)"},
                    )
                    # f"{text.upper()}={eval(text)}"},
                    print(f"XXX sendMessage resp: {r}")
                    p.change_sending_tg()
    except Exception as err:
        print(err)

    print(f"END | {tg_send.__name__}")
