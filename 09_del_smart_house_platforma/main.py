import time

import Adafruit_DHT
import RPi.GPIO as GPIO
from flask import Flask

GPIO.setmode(GPIO.BOARD)

# Defines the sensor and it's pin
sensor = Adafruit_DHT.DHT11
sensor_pin = 4 # this must match with the pin you connected the data wire.

# Add webserver
app = Flask(__name__)

@app.route('/metrics')
def metrics():
    umid, temp = Adafruit_DHT.read_retry(sensor, sensor_pin)
    if umid is not None and temp is not None:
        return '# HELP local_temp local temperature\n# TYPE local_temp gauge\nlocal_temp {}\n# HELP local_humidity local humidity\n# TYPE local_humidity gauge\nlocal_humidity {}\n'.format(int(temp), int(umid)), 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return 'Could not read from DHT11.', 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("running flask")
    app.run(host="0.0.0.0", port=5000)
