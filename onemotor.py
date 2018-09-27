import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time


f = 24
r = 25

GPIO.setup(f, GPIO.OUTPUT)
GPIO.setup(r, GPIO.OUTPUT)

GPIO.output(f, 1)
time.sleep(0.2)
GPIO.output(f,0)
