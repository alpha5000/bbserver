#Barbot Server
#@Author: Marco Centracchio
#Rev: 9/25/2016
#

import RPi.GPIO as GPIO
import time

serial = 32
latch = 36
clock = 38



def main():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)

	GPIO.setup(serial,GPIO.OUT)
	GPIO.setup(latch,GPIO.OUT)
	GPIO.setup(clock,GPIO.OUT)

	print('Welcome to BarBot!')
	if(GPIO.getmode() == 10):
		print("Pi is operating in : GPIO.BOARD mode")
	if(GPIO.getmode() == 11):
		print("Pi is operating in : GPIO.BCM mode")
		
		
	GPIO.output(latch, GPIO.LOW)
	GPIO.output(clock, GPIO.LOW)

	for i in range(0,8):
		GPIO.output(serial, GPIO.LOW)
		pulseclock()
	pulselatch()
	
	time.sleep(3)
	
	for i in range(0,8):
		GPIO.output(serial, GPIO.HIGH)
		pulseclock()
	pulselatch()
	
	
	#GPIO.cleanup()
		

def pulseclock():
	print("pulsing clock")
	GPIO.output(clock,GPIO.HIGH)
	GPIO.output(clock,GPIO.LOW)
    
def pulselatch():
	print("pulsing latch")
	GPIO.output(latch, GPIO.HIGH)
	GPIO.output(latch,GPIO.LOW)



main()
