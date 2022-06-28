# はじめに

下剋上は[e-typing](https://www.e-typing.ne.jp/)でのタイピング成績の登録、ランキング表示、成長記録の確認ができるWebアプリケーションです。<br>
新人１名のキーボード演習の日々の成績の推移の確認すること、また先輩の成績と比較をすることを目的として作成しました。<br>
新人のみ成績の追加登録が可能なように、現バージョンでは直接成績登録用のURLにアクセスしない限り成績入力フォームの表示ができないようになっています。（改善方法検討中）

# 環境
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
