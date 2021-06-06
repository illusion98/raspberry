#from gpio import *
import gpio
from time import *


def main():
	gpio.pinMode(0,gpio.OUT) #led
	gpio.pinMode(1,gpio.IN)  #tempsesor
	gpio.pinMode(2,gpio.IN)  #switch
	
	# pin 상태, output -> HIGH(3.3v)/ LOW(0v)
	while 1:
		tempsensor=gpio.digitalRead(2)
		print('temp:{}'.format(tempsensor))
		
		button=gpio.digitalRead(1)
		if (button==gpio.HIGH):
			gpio.digitalWrite(0,gpio.HIGH)
			sleep(1)
			gpio.digitalWrite(0,gpio.LOW)
			sleep(1)

		else:
			gpio.digitalWrite(0,gpio.LOW)
		
if __name__ == '__main__':
	main()
