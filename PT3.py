#from gpio import *
import gpio
from time import *


def main():
	gpio.pinMode(0,gpio.OUT) # led , digitalWrite
	gpio.pinMode(1,gpio.IN) # button, digitalRead
	gpio.pinMode(2,gpio.IN) # tempsensor
	#gpio.pinMode(3,gpio.OUT) # heating
	
	# pin 상태, output -> HIGH(3.3v)/ LOW(0v)
	while 1:
		tempsensor=gpio.digitalRead(2)
		temperature=(tempsensor*200)/1023-100
		
		print('tempsensor:{0:3.2f}. temperature:{}'.format(tempsensor,temperature))
		
		if (temperature>21):
			gpio.digitalWrite(0,gpio.HIGH)
		else:
			gpio.digitalWrite(0,gpio.LOW)
		
		button=gpio.digitalRead(1)
		if (button==gpio.HIGH):
			#print("button on")
			#gpio.digitalWrite(0,gpio.HIGH)
			gpio.digitalWrite(3,gpio.HIGH)

		else:
			#print('button off')
			#gpio.digitalWrite(0,gpio.LOW)
			gpio.digitalWrite(3,gpio.LOW)
		
if __name__ == '__main__':
	main()
