from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def main():
	now = datetime.datetime.now()
	timeString = now.strftime("%Y-%m-%d %H:%M:%S")
	templateData = {
		'title' : 'HELLO!',
		'time': timeString
		}
	return render_template('main.html', data=templateData)
	
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
