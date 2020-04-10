run: static
	DJANGO_DEBUG=TRUE pipenv run python src/manage.py runserver

static:
	DJANGO_DEBUG=TRUE pipenv run python src/manage.py collectstatic --noinput --clear -v0


test:
	DJANGO_DEBUG=TRUE pipenv run python src/manage.py test -v2 project apps
