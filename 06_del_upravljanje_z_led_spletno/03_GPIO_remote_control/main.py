from flask import Flask, render_template, request


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
    return render_template("main.html", data=data)
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)


