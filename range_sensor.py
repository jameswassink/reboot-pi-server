import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def getRange():
	TRIG = 20 
	ECHO = 16

	print "Distance Measurement In Progress"

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.output(TRIG, False)
	print "Waiting For Sensor To Settle"
	time.sleep(0.5)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
	  pulse_start = time.time()

	while GPIO.input(ECHO)==1:
	  pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start # ie how long it took to get there and back

	distance = pulse_duration * 17150 # based on speed of sound

	distance = round(distance, 2)

	print "Distance:",distance,"cm"
	
if __name__ == '__main__':
	getRange()
	GPIO.cleanup()
