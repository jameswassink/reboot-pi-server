import socketio
import eventlet
import eventlet.wsgi

from flask import Flask, render_template

sio = socketio.Server()

from ledFlasher import LEDFlasher

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
	

if __name__ == '__main__':
	# wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
    
    
