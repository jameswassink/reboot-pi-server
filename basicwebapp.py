from flask import Flask, render_template, request
from ledFlasher import LEDFlasher
app = Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/hello', methods=["POST"])
def hello():	
    return render_template('hello.html', name=request.form['helloName'])
    
@app.route('/bye')
def bye():
	return "Goodbye World"
	
@app.route('/flash')
def flash():
	lf = LEDFlasher()
	lf.flash()
	return "The LED is flashing now."	
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

