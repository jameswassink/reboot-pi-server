from gpiozero import LED
from time import sleep

class LEDFlasher:
	def __init__(self):
		self.led = LED(23)
		
	def flash(self):
		self.led.on()
		sleep(1)
		self.led.off()
		sleep(1)
	
