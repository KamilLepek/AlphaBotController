
import RPi.GPIO as GPIO
import time
import sys
from AlphaBot import AlphaBot

Ab = AlphaBot()

IR = 18
PWM = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IR,GPIO.IN,GPIO.PUD_UP)
try:
	input = sys.argv[1]
	try:
		duration = int(sys.argv[2])
	except ValueError:
		print("Failed to parse second argument")
		GPIO.cleanup()
		exit()
	while (duration>0):
		if(input != None):
			if input == "cleanup":
				GPIO.cleanup()
			if input == "forward":
				Ab.forward()
				print("forward")
			if input == "left":
				Ab.left()
				print("left")
			if input == "stop":
				Ab.stop()
				print("stop")
			if input == "right":
				Ab.right()
				print("right")
			if input == "backward":
				Ab.backward()
				print("backward")
			if input == "faster":
				if(PWM + 10 < 101):
					PWM = PWM + 10
					Ab.setPWMA(PWM)
					Ab.setPWMB(PWM)
					print(PWM)
			if input == "slower":
				if(PWM - 10 > -1):
					PWM = PWM - 10
					Ab.setPWMA(PWM)
					Ab.setPWMB(PWM)
					print(PWM)
		duration=duration-1
		time.sleep(0.001)
except KeyboardInterrupt:
	GPIO.cleanup()
GPIO.cleanup()
