# Pythonのベースイメージ
FROM python:3.11

# 必要なパッケージのインストール
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    qt5-default \
    libqt5core5a \
    libqt5gui5 \
    libqt5widgets5 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*


# RTIMU ライブラリのインストール
RUN git clone https://github.com/RPi-Distro/RTIMULib.git /opt/RTIMULib || echo "Failed to clone RTIMULib repository" && \
    cd /opt/RTIMULib/Linux && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j4 && \
    sudo make install && \
    sudo ldconfig

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
