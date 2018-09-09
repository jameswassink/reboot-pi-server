import socketio
import eventlet
import eventlet.wsgi

from flask import Flask, render_template

sio = socketio.Server()

from ledFlasher import LEDFlasher

from carcontrol import CarControl

app = Flask(__name__)

lf = LEDFlasher()

@app.route('/')
def socket():
	return render_template('holdforlight.html')
	
@sio.on('light')
def lightChange(sid, data):
	if data == 1:
		lf.turnOn()
	else:
		lf.turnOff()
	
	
@app.route('/carcontrol')
def carcontrol():
	return render_template('carcontrol.html')	
	
@sio.on('carcommand')
def carcommand(sid, data):
	print data
	cc = CarControl()
	cc.write(data)

if __name__ == '__main__':
	# wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
    
    
