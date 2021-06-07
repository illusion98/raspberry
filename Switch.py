import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

LED = 10
Switch= 12


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, GPIO.PUD_UP)

while True:
    
    if GPIO.input(Switch) == GPIO.LOW:
        print("Button was pushed!")
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
    else:
        print("Button was not pushed!")
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1)
