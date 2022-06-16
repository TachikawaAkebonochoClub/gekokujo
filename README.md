ishii参上
nakazawa参上


# 環境切り分け

1. docker-compose に読ませる `.env` を切り替える
2. Django`settings.py` は環境変数から取得する（.envは読まない）
3. Django`settings.py` への環境変数はdocker-compose.yaml 内で引き渡す

- .env
```bash

DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS="edo.castle.gq"
DOCKER_DJANGO_PORT=18888
```
- docker-compose.yaml
```yaml
version: "3.3"
services:
[...]
  web:
    build: ./docker
    command: python manage.py runserver 0.0.0.0:8888
    environment:
    - DOCKER_DJANGO_PORT="${WEB_PORT:-8888}
    - DEBUG=${DEBUG:-True}
    - ALLOWED_HOSTS=${ALLOWED_HOSTS:-*}
    volumes:
      - ./code:/code
    ports:
      - "${DOCKER_DJANGO_PORT}:8888"
```


## 開発
```
$ cp env.dev .env
$ cat .env # or vi .env
$ docker-compose ...
```

## 公開
```
$ cp env.prod .env
$ cat .env # or vi .env
$ docker-compose ...
```
