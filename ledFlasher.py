import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from time import sleep

class LEDFlasher:
	def __init__(self):
		self.led = 23
		GPIO.setup(ledpin, GPIO.OUT)
		self.led = LED(23)
		
	def flashOnce(self):
		GPIO.output(self.led, 1)
		sleep(1)
		GPIO.output(self.led, 0)
		sleep(1)
		
	def flashAlways(self):
		while(1):
			self.flashOnce()
	
	def turnOn(self):
		GPIO.output(self.led, 1)
	
	def turnOff(self):
		GPIO.output(self.led, 0)

if __name__== '__main__':
	lf = LEDFlasher()
	lf.flashAlways()
