# 目次

- [はじめに](#はじめに)
- [機能](#機能)
- [環境](#環境)
   - [実行環境](#実行環境)
   - [コンテナ内環境](#コンテナ内環境)
- [前提条件](#前提条件)
- [初期起動](#初期起動)
- [サンプルデータ登録](#サンプルデータ登録任意)

# はじめに

下剋上は[e-typing](https://www.e-typing.ne.jp/)でのタイピング成績の登録、ランキング表示、成長記録の確認ができるWebアプリケーションです。<br>
新人１名のキーボード演習の日々の成績の推移の確認すること、また先輩の成績と比較をすることを目的として作成しました。<br>
新人のみ成績の追加登録が可能なように、現バージョンでは直接成績登録用のURLにアクセスしない限り成績入力フォームの表示ができないようになっています。（改善方法検討中）

[公開サイトはこちら](https://gekokujyo.castle.gq/)

# 機能

- 登録
  - 成績登録機能
    - 利用者が、成績登録時に成績登録画面からタイピング結果から取得できる全項目を登録可能
    

- 閲覧
  - ランキング一覧機能（トップ画面）
    - 閲覧者が、登録されている全員のベスト成績での最新ランキング結果を確認できる
  - 成長記録確認機能
    - 指定User_idの全記録を日付が新しい順に見ることができる

# 環境

![architecture](https://user-images.githubusercontent.com/86756223/176816200-720e9d63-fccf-463a-9e7e-6d5e4d67b7e3.png)


## 実行環境
- Linux 5.4.0
- Docker 20.10.14
- docker-compose 1.29.2

## コンテナ内環境
- PostgreSQL 14.2
- Django 2.1.3
- Python 3.10.4

# 前提条件

- 実行環境構築済み

# 初期起動

1. ソースコードダウンロード<br>
    ```
    git clone git@github.com:TachikawaAkebonochoClub/gekokujo.git
    ```
2. 環境に応じて.envファイル作成<br>
    - .envの構成
      ```
      DJANGO_ALLOWED_HOSTS=アクセスを許可するホスト名
      DJANGO_DEBUG=任意（True or False）
      DOCKER_DJANGO_PORT=Djangoコンテナのポート番号
      ROOKIES_ID=成長記録を確認したいuser_id
      ```

    - 環境を切り分ける場合
      1. docker-compose に読ませる `.env` を切り替える
          - 開発 : env.dev
          - 本番 : env.prod
      2. Django`settings.py` は環境変数から取得する（`.env`は読まない）
      3. Django`settings.py` への環境変数はdocker-compose.yaml 内で引き渡す
      
          - 開発用か本番用のenvファイルを適用する
            ```
            cp env.devもしくはenv.prod .env
            ```
          - 必要に応じて編集する
            ```
            vi .env
            ```

3. DB側のコンテナを起動<br>
    ```
    docker-compose up -d db
    ```
4. Django側のコンテナを起動<br>
    ```
    docker-compose up -d web
    ```
5. アプリ側のコンテナに入る<br>
    ```
    docker exec -it gekokujo_web bash
    ```

6. DBにテーブル作成<br>
    1. gekokujo_appにマイグレーションファイルを作成<br>
        ```
        python manage.py makemigrations gekokujo_app
        ```
    2. マイグレーションファイルをデータベースに適用<br>
        ```
        python manage.py migrate
        ```


7. `http://実行場所のIP:.envで指定したポート番号`にアクセス(Chrome/Edge)<br>
  以下の画面表示であれば正常

![image](https://user-images.githubusercontent.com/107466011/176812910-f33cf072-37a5-4426-be90-a666ca2ed0a4.png)

8. コンテナの停止<br>
    ```
    docker-compose stop
    ```

# サンプルデータ登録（任意）

1. sample_data.csvファイルをDBのコンテナにコピーする<br>
    ```
    docker cp ./data/sample_data.csv gekokujo_db:tmp/
    ```
2. DB側のコンテナに入る<br>
    ```
    docker exec -it gekokujo_db bash
    ```
3. postgresに接続<br>
    ```
    psql -U postgres
    ```
4. sample_data.csvファイルからscoretableにデータをコピーする<br>
    ```
    \copy gekokujo_app_scoretable (user_id,name,date,course,score,level,time,count,miss,read,rate,weakness) from '/tmp/initial_data.csv' DELIMITER ',' CSV HEADER encoding 'sjis';
    ```

