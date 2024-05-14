from flask import Flask, render_template, request
from gpiozero import LED

led_01 = LED(17)
led_02 = LED(27)

pins = {"1": {"pin": led_01, "state": "off"}, "2": {"pin": led_02, "state": "off"}}

for pin in pins.values():
	pin["pin"].off()

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
	for pin, action_data in data.items():
		if pin in pins:
			if pins[pin]["state"] == "on":
				pins[pin]["pin"].on()
			else:
				pins[pin]["pin"].off()
