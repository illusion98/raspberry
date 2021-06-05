import RPi.GPIO as GPIO 
import I2C_driver as LCD
from time import sleep

GPIO.setmode(GPIO.BOARD)
LED = 12
Switch= 10
mylcd = LCD.lcd()

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(Switch) == GPIO.HIGH:
        print("Button was pushed!")
        
        GPIO.output(LED, GPIO.HIGH)
        
        mylcd.lcd_display_string("LED ON",1)
        sleep(3)
        
        mylcd.lcd_clear()
        sleep(0.2)
    else:
        print("Button was not pushed!")
        
        GPIO.output(LED, GPIO.LOW)
        
        mylcd.lcd_display_string("LED OFF",1)
        time.sleep(1)
        
        mylcd.lcd_clear()
        sleep(0.2)
