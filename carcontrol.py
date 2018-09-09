import serial

class CarControl:
	def __init__(self):		
		self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
		
	def write(self, msg):
		self.ser.write(msg.encode())
		result = self.ser.read(100)
		print result
