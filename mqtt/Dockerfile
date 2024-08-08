# Pythonのベースイメージ
FROM python:3.11

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Qt4 ソースのダウンロードとビルド
RUN wget https://download.qt.io/archive/qt/4.8/4.8.7/qt-everywhere-opensource-src-4.8.7.tar.gz && \
    tar xzf qt-everywhere-opensource-src-4.8.7.tar.gz && \
    cd qt-everywhere-opensource-src-4.8.7 && \
    ./configure -opensource -confirm-license && \
    make -j$(nproc) && \
    make install

# RTIMU ライブラリのインストール
RUN git clone https://github.com/RPi-Distro/RTIMULib.git /opt/RTIMULib && \
    cd /opt/RTIMULib && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
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

