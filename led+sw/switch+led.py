import RPi.GPIO as GPIO
from time import sleep

LED= 32 #12
Switch= 10 #8

#GPIO.setmode(GPIO.BCM) # set up BCM GPIO numbering
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT) 

while True:
    
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
        GPIO.output(LED, GPIO.HIGH)
        sleep(1)
    else:
        print("Button was not pushed!")
        GPIO.output(LED, GPIO.LOW)
        sleep(1)
