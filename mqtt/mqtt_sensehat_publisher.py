import os
import time
import paho.mqtt.client as mqtt
from sense_hat import SenseHat

# 環境変数からMQTT設定を取得
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC_PREFIX = os.getenv("MQTT_TOPIC_PREFIX", "sensehat/")

# Sense HATの設定
sense = SenseHat()

# MQTTクライアントの初期化
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC_PREFIX + "status")

client.on_connect = on_connect

def publish_sensor_data():
    while True:
        # センサーデータの取得
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()

        # MQTTでの公開
        client.publish(MQTT_TOPIC_PREFIX + "temperature", temperature)
        client.publish(MQTT_TOPIC_PREFIX + "humidity", humidity)
        client.publish(MQTT_TOPIC_PREFIX + "pressure", pressure)
        
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity} %")
        print(f"Pressure: {pressure} hPa")

        time.sleep(10)  # 10秒ごとにデータを公開

if __name__ == "__main__":
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_start()
    publish_sensor_data()

