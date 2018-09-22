import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
buttonPin = 8
ledPin = 23
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)

def onBtnPress(pin):
        print("button pressed")
        GPIO.output(ledPin, 1)
        sleep(0.5)
        GPIO.output(ledPin, 0)

GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=onBtnPress, bouncetime=200)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
