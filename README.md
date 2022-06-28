# 下剋上

下剋上は[e-typing](https://www.e-typing.ne.jp/)でのタイピング成績の登録、ランキング、成長記録の表示をさせるWebアプリケーションです。<br>
新人１名のキーボード演習の日々の成績の推移の確認すること、また先輩の成績と比較をすることを目的として作成しました。

## 環境

- Linux 5.4.0
- Docker 20.10.14
- docker-compose 1.29.2

- PostgreSQL 14.2
- Django 
- Python

## 前提条件

- docker使用
- DBはPostgreSQL

## 初期起動

1. ソースコードダウンロード<br>
  `git clone git@github.com:TachikawaAkebonochoClub/gekokujo.git`
2. 環境に応じて.envファイル作成<br>
    ```
    DJANGO_ALLOWED_HOSTS=アクセスを許可するホスト名
    DJANGO_DEBUG=任意（True or False）
    DOCKER_DJANGO_PORT=Djangoコンテナのポート番号
    ROOKIES_ID=成長記録を確認したいuser_id
    ```

    環境を切り分ける場合
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



3. DB側のコンテナを起動<br>
  `docker-compose up -d db`
4. Django側のコンテナを起動<br>
  `docker-compose up -d`<br>
  もしくは<br>
  `docker-compose up -d web`
5. アプリ側のコンテナに入る<br>
  `docker exec -it gekokujo_web bash`


6. DBにテーブル作成<br>
    - gekokujo_appにマイグレーションファイルを作成<br>
      `python manage.py makemigrations gekokujo_app`
    - マイグレーションファイルをデータベースに適用<br>
      `python manage.py migrate`


7. `http://実行場所のIP:.envで指定したポート番号`にアクセス<br>
  以下の画面表示であれば正常

![image](https://user-images.githubusercontent.com/107466011/175890119-c21fabac-4036-4ead-ad0c-7cd7031d8d2f.png)

## 初期データ登録

1. sample_data.csvファイルをDBのコンテナにコピーする<br>
  `docker cp ./data/sample_data.csv gekokujo_db:tmp/`
2. DB側のコンテナに入る<br>
  `docker exec -it gekokujo_db bash`
3. postgresに接続<br>
  `psql -U postgres`
4. sample_data.csvファイルからscoretableにデータをコピーする
`\copy gekokujo_app_scoretable (user_id,name,date,course,score,level,time,count,miss,read,rate,weakness) from '/tmp/initial_data.csv' DELIMITER ',' CSV HEADER encoding 'sjis';`

## 機能

- 登録
  - 成績登録機能
    - 利用者が、成績登録時に成績登録画面からタイピング結果でわかる項目を登録することができる
    

- 閲覧
  - ランキング一覧機能（トップ画面）
    - 閲覧者が登録されている全員のベスト成績での最新ランキング結果を確認できる
  - 成長記録確認機能
    - 指定User_idの全記録を日付が新しい順に見ることができる

## デモ

- ランキング一覧画面

![image](https://user-images.githubusercontent.com/107466011/175880752-ae488379-899c-4fb0-bdf0-de830e7d670a.png)

- 成績登録画面

![image](https://user-images.githubusercontent.com/107466011/175881059-b1155db2-a881-4ec4-bd40-42890093dec9.png)

![image](https://user-images.githubusercontent.com/107466011/175881221-90f4f65c-802f-4d64-8968-008e3e4ec22d.png)

- 成長記録画面

![image](https://user-images.githubusercontent.com/107466011/175881424-057a8b15-d02a-4aca-9558-3597f6ee5324.png)

※入力されているデータは仮のものです。
