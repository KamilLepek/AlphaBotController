
import RPi.GPIO as GPIO
import time
import sys
from AlphaBot import AlphaBot

Ab = AlphaBot()

IR = 18
PWM = 50

def printHelp():
        file = open('help.txt', 'r')
        print file.read()
        file.close()
        return

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IR,GPIO.IN,GPIO.PUD_UP)
try:
	input = sys.argv[1]
	availableCommands = ["forward", "backward", "left", "right"]
	if input not in availableCommands:
		printHelp()
		exit()
	try:
		duration = int(sys.argv[2])
	except ValueError:
		print("Failed to parse duration argument")
		GPIO.cleanup()
		exit()
	except IndexError:
		print("Please enter duration [ms]")
		print("python Remote.py <COMMAND> <DURATION> [<PWM>]")
		exit()
	try:
		PWM = int(sys.argv[3])
		if(PWM>100):
			PWM = 100
			print("Maximum PWM is 100")
		if(PWM<35):
			PWM=35
			print("Minimum PWM is 35")
		Ab.setPWMA(PWM)
		Ab.setPWMB(PWM)
	except ValueError:
		print("Failed to parse PWM argument")
		GPIO.cleanup()
		exit()
	except IndexError:
		pass
	while (duration>0):
		if(input != None):
			if input == "forward":
				Ab.forward()
			if input == "left":
				Ab.left()
			if input == "right":
				Ab.right()
			if input == "backward":
				Ab.backward()
		duration=duration-1
		time.sleep(0.001)
except KeyboardInterrupt:
	GPIO.cleanup()
except IndexError:
	printHelp()
        exit()
GPIO.cleanup()
