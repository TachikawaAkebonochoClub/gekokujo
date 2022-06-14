FROM python:3
# Pythonがpyc filesとdiscへ書き込むことを防ぐ(キャッシュを作成しない)
ENV PYTHONDONTWRITEBYTECODE=1
# Pythonが標準入出力をバッファリングすることを防ぐ
# (出力がターミナルに直接送信される為、ログをリアルタイムで確認できる)
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
