from flask import Flask, render_template, request

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = {"1": 17,
        "2": 27}
for pin in pins:
    GPIO.setup(pins[pin], GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def landing_page():
	return 'Hello World!'


@app.route("/interface")
def interface_pins():
    data = {}

    if "1" not in request.args:
        data["1"] = "off"
    else:
        data["1"] = request.args["1"]

    if "2" not in request.args:
        data["2"] = "off"
    else:
        data["2"] = request.args["2"]

    control_pins(data)
    
    return render_template("main.html", data=data)
	


def control_pins(data):
    print("CONTROLING PINS: ", data)
    for pin, action in data.items():
        if pin in pins:
            if action == "on":
                GPIO.output(pins[pin_num], GPIO.HIGH)
            else:
                GPIO.output(pins[pin_num], GPIO.LOW)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)


