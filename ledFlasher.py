from gpiozero import LED
from time import sleep

class LEDFlasher:
	def __init__(self):
		self.led = LED(23)
		
	def flashOnce(self):
		self.led.on()
		sleep(1)
		self.led.off()
		sleep(1)
		
	def flashAlways(self):
		while(1):
			self.flashOnce()
	
	def turnOn(self):
		self.led.on()
	
	def turnOff(self):
		self.led.off()
