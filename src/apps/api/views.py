import json

import requests
from django.http import HttpResponse
from django.views import View
from dynaconf import settings
from rest_framework.authtoken.views import ObtainAuthToken as _DrfObtainAuthToken

from apps.blog.models import Post
#tg=set()

class ObtainAuthToken(_DrfObtainAuthToken):
    swagger_schema = None


class TelegramView(View):
    def post(self, *args, **kwargs):
        try:
            payload = json.loads(self.request.body)
            message = payload["message"]
            text = message["text"]
            chat_id = message["chat"]["id"]
            #tg.add(chat_id)
            print(list(map(lambda x: x.sending_tg==True, Post.objects.all())))
            print(chat_id)
            if all(i==True for i in list(map(lambda x: x.sending_tg==True, Post.objects.all()))):
                r = requests.post(
                    f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                    json={"chat_id": chat_id, "text": "we haven't a new post=("}, )
            else:
                for p in Post.objects.all():
                    if p.sending_tg==None or p.sending_tg==False:
                        r = requests.post(
                            f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                            json={"chat_id": chat_id, "text": 'we have a new post=)'},)
            # f"{text.upper()}={eval(text)}"},
                        print(f"XXX sendMessage resp: {r}")
                        p.change_sending_tg()
        except Exception as err:
            print(err)
        return HttpResponse()
