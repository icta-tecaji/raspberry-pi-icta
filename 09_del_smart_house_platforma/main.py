import time
import board
import adafruit_bmp280
from flask import Flask

app = Flask(__name__)

# Initialize I2C bus
i2c = board.I2C()

# Initialize BMP280 sensor
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Set sea level pressure (default: 1013.25 hPa)
# https://meteo.arso.gov.si/uploads/probase/www/observ/surface/text/sl/observationAms_PORTOROZ_SECOVLJE_history.html
bmp280.sea_level_pressure = 1010

@app.route('/metrics')
def metrics():
    temp = bmp280.temperature
    pressure = bmp280.pressure
    altitude = bmp280.altitude
    if temp is not None and pressure is not None:
        print(f"Temperature: {temp} C", f"Pressure: {pressure} hPa", f"Altitude: {altitude} m")
        return '# HELP local_temp local temperature\n# TYPE local_temp gauge\nlocal_temp {}\n# HELP local_pressure local pressure\n# TYPE local_pressure gauge\nlocal_pressure {}\n'.format(float(temp), int(pressure)), 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return 'Could not read from BMP280.', 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == "__main__":
    print("running flask")
    app.run(host="0.0.0.0", port=5000)
