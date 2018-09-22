import RPi.GPIO as GPIO

GPIO.setMode(GPIO.BCM)
buttonPin = 8
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttonVal = GPIO.input(buttonPin)

print buttonVal
