#from gpio import *
import gpio
from time import *


def main():
	# 보드 주변 장 치프로그램 구성
	# pin 설정
	gpio.pinMode(0,gpio.OUT)
	gpio.pinMode(1,gpio.OUT)
	gpio.pinMode(2,gpio.IN)
	
	# pin 상태, output -> HIGH(3.3v)/ LOW(0v)
	while 1:
		gpio.digitalWrite(0,gpio.HIGH)
		sleep(1)
		gpio.digitalWrite(0,gpio.LOW)
		sleep(1)

		gpio.digitalWrite(1,gpio.HIGH)
		sleep(1)
		gpio.digitalWrite(1,gpio.LOW)
		sleep(1)

		
		button=gpio.digitalRead(2)
		if (button==gpio.HIGH):
			gpio.digitalWrite(0,gpio.HIGH)
			sleep(1)
			gpio.digitalWrite(0,gpio.LOW)
			sleep(1)

		else:
			gpio.digitalWrite(0,gpio.LOW)
		
if __name__ == '__main__':
	main()
