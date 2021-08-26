from flask import Flask, render_template, request

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = {"1": {
		"pin_num": 17,
		"state": "off"
		},
        "2": {
		"pin_num": 27,
		"state": "off" }}
for pin in pins:
	GPIO.setup(pins[pin]["pin_num"], GPIO.OUT)
	GPIO.output(pins[pin]["pin_num"], GPIO.LOW)

app = Flask(__name__)

@app.route("/")
def landing_page():
	return 'Hello World!'


@app.route("/interface")
def interface_pins():
	print("Data: ", request.args)
	for pin in pins:
		if pin in request.args:
			pins[pin]["state"] = request.args[pin]
	data = pins
	control_pins(data)
	return render_template("main.html", data=data)


def control_pins(data):
	print("CONTROLING PINS: ", data)
	for pin, action in data.items():
		if pin in pins:
			if pins[pin]["state"] == "on":
				GPIO.output(pins[pin]["pin_num"], GPIO.HIGH)
			else:
				GPIO.output(pins[pin]["pin_num"], GPIO.LOW)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)


