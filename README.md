# 下剋上

下剋上は[e-typing](https://www.e-typing.ne.jp/)でのタイピング成績の登録、ランキング、成長記録の表示をさせるWebアプリケーションです。

## 環境

- Python
- VSCode
- Docker
- Django
- Bootstrap4
- PostgreSQL

## 環境構築

- Git

1. gekokujoフォルダができて欲しい場所に移動
2. `git clone gekokujoのSSH URL`実行
3. .envファイル作成
4. `docker-compose up -d db`実行
5. ログがとまったら`docker-compose up -d`実行
6. `docker exeｃ -it gekokujo_web bash`実行、アプリ側のコンテナに入る
7. `python manage.py makemigrations gekokujo_app`実行、gekokujo_appにマイグレーションファイルを作成
8. `python manage.py migrate`実行、マイグレーションファイルをデータベースに適用
9. `実行場所のIP:.envで指定したポート番号`にアクセス
10. ↓この画面になればOK

![image](https://user-images.githubusercontent.com/107466011/175890119-c21fabac-4036-4ead-ad0c-7cd7031d8d2f.png)

## 環境切り分け

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


## 機能

- 登録
  - 成績登録機能
    - 利用者が、成績登録時に成績登録画面から[id、イニシャル、実施日、コース、スコア、レベル、入力時間、入力文字数、ミス入力数、WPM、正確率、苦手キー]を登録する
    - タイピングのスコアを蓄積・参照可能にする為、DB（PostgreSQL）を使用

- 閲覧
  - ランキング一覧機能（トップ画面）
    - 閲覧者が登録されている全員のベスト成績での最新ランキング結果を表形式で確認できる
    - 同じ人が別日に成績を追加してもベストスコアの 1 データのみをランキングに表示させる
  - 成長記録確認機能
    - User_idが1の結果のみを表示
      - 表形式で表示

## デモ

- ランキング一覧画面

![image](https://user-images.githubusercontent.com/107466011/175880752-ae488379-899c-4fb0-bdf0-de830e7d670a.png)

- 成績登録画面

![image](https://user-images.githubusercontent.com/107466011/175881059-b1155db2-a881-4ec4-bd40-42890093dec9.png)

![image](https://user-images.githubusercontent.com/107466011/175881221-90f4f65c-802f-4d64-8968-008e3e4ec22d.png)

- 成長記録画面

![image](https://user-images.githubusercontent.com/107466011/175881424-057a8b15-d02a-4aca-9558-3597f6ee5324.png)

※入力されているデータは仮のものです。



## 今後追加予定の機能

- 登録
  - 成績登録機能
    - ranking テーブルと別に、id とイニシャルのみのテーブルを作成し、ranking テーブルの column は[id、実施日、コース、スコア、レベル、入力時間、入力文字数、ミス入力数、WPM、正確率、苦手キー]に変更する事で、毎回イニシャルを入力しなくていいようにする 

- 閲覧
  - 成長記録確認機能
    - グラフ形式で確認できるようにする


