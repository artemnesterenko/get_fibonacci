DOCKER_COMPOSE=docker-compose -p fibonacci
TEST_SETTINGS=get_fibonacci.test_settings

build:
	$(DOCKER_COMPOSE) build

up:
	$(DOCKER_COMPOSE) up

test:
	$(DOCKER_COMPOSE) run --rm --no-deps -e DJANGO_SETTINGS_MODULE=$(TEST_SETTINGS) web python manage.py test