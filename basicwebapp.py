from flask import Flask, render_template, request
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
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

