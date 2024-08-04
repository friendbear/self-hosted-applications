docker build -t my-sensehat-mqtt .

docker run --device /dev/i2c-1 \
  -e MQTT_BROKER="localhost" \
  -e MQTT_PORT="1883" \
  -e MQTT_TOPIC_PREFIX="home/sensors" \
  my-sensehat-mqtt

