from os import urandom
from typing import Callable
from typing import Collection
from typing import Dict
from typing import List
from typing import Optional

from django.contrib.auth import get_user_model
from django.test import Client

User = get_user_model()


class UserTestMixin:
    def create_user(
        self,
        placeholder: Optional[str] = None,
        user_kw: Optional[Dict] = None,
        verified=False,
    ) -> User:
        placeholder = placeholder or urandom(4).hex()
        form_data = {
            "username": f"{placeholder}",
            "email": f"email_{placeholder}@test.com",
            "password": placeholder,
        }

        user_kw = (user_kw or {}).copy()
        user_kw.update(form_data)

        user = User.objects.create_user(**user_kw)
        user.save()

        if verified:
            self.create_auth_profile(user)

        self.create_profile(user)

        return user

    @staticmethod
    def create_auth_profile(user: User):
        auth = AuthProfile(
            user=user, verification_code=user.username, verified_at=utcnow(),
        )
        auth.save()

        return auth

    @staticmethod
    def create_profile(user):
        profile = Profile(user=user, name=f"name_{user.username}")
        profile.save()
        return profile

    def create_auth_token(self, user, client: Optional[Client] = None) -> str:
        cli = client or self.client

        credentials = {"username": user.username, "password": user.username}

        resp = cli.post("/api/obtain_auth_token/", credentials)
        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        payload = resp.json()
        self.assertEqual(1, len(payload))
        self.assertIsInstance(payload, dict)
        self.assertIn("token", payload)

        token = payload["token"]
        self.assertTrue(token)

        return token


class ResponseTestMixin:
    def validate_response(
        self,
        *,
        url: str,
        expected_view_name: str,
        expected_view: type,
        expected_template: str,
        method: Optional[str] = "get",
        form_data: Optional[Dict] = None,
        expected_status_code: Optional[int] = 200,
        content_filters: Optional[Collection[Callable[[bytes], bool]]] = None,
        expected_redirect_chain: Optional[List] = None,
        client: Optional = None,
    ):
        cli = client if client else Client()
        meth = getattr(cli, method)

        meth_args = []
        if form_data:
            meth_args.append(form_data)

        resp = meth(url, *meth_args, follow=True)
        self.assertEqual(resp.status_code, expected_status_code)

        if expected_redirect_chain is not None:
            self.assertEqual(resp.redirect_chain, expected_redirect_chain)

        self.assertEqual(resp.resolver_match.view_name, expected_view_name)
        self.assertEqual(
            resp.resolver_match.func.__name__, expected_view.as_view().__name__
        )

        self.assertIn(expected_template, resp.template_name)

        for content_filter in content_filters or []:
            self.assertTrue(content_filter(resp.content))
