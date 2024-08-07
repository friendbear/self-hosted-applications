import os
import time
import json
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

# 環境変数からMQTT設定を取得
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC_PREFIX = os.getenv("MQTT_TOPIC_PREFIX", "sensehat/")
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")

# Sense HATの設定
sense = SenseHat()

# MQTTクライアントの初期化
client = mqtt.Client()

# MQTTの認証情報を設定
if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected with result code " + str(rc))
        client.subscribe(MQTT_TOPIC_PREFIX + "status")
    else:
        print(f"Failed to connect with result code {rc}")

client.on_connect = on_connect

def publish_sensor_data():
    while True:
        try:
            # センサーデータの取得
            temperature = sense.get_temperature()
            humidity = sense.get_humidity()  # Sense HAT には湿度センサーがないので、この行はエラーになります
            pressure = sense.get_pressure()

            # JSON形式のデータ
            sensor_data = {
                "temperature": temperature,
                "humidity": humidity,
                "pressure": pressure
            }

            # MQTTでの公開
            client.publish(MQTT_TOPIC_PREFIX + "data", json.dumps(sensor_data))

            print(f"Published: {json.dumps(sensor_data)}")

        except Exception as e:
            print(f"Error occurred: {e}")

        time.sleep(10)  # 10秒ごとにデータを公開

if __name__ == "__main__":
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
    except Exception as e:
        print(f"Failed to connect to MQTT broker: {e}")
        exit(1)

    client.loop_start()
    publish_sensor_data()

