# Pythonのベースイメージ
FROM python:3.11

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    python3-pip \
    libboost-all-dev \
    && rm -rf /var/lib/apt/lists/*

# RTIMU ライブラリのインストール
RUN git clone https://github.com/RPi-Distro/RTIMULib.git /opt/RTIMULib && \
    cd /opt/RTIMULib && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make && \
    make install && \
    ldconfig

# Pythonライブラリのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# Sense HATライブラリのインストール
RUN pip install sense-hat

# コードをコンテナ内にコピー
COPY mqtt_sensehat_publisher.py /app/mqtt_sensehat_publisher.py

# ワーキングディレクトリの設定
WORKDIR /app

# エントリーポイントの設定
CMD ["python", "mqtt_sensehat_publisher.py"]
