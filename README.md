# AlphaBotController

AlphaBot User Manual: https://www.mouser.com/pdfdocs/AlphaBot-User-Manual2.pdf

Remote.py - Script used to control remotely AlphaBot platform connected to Raspberry Pi 3 Model B  
Moves the robot in specified direction for specified amount of milliseconds.

Usage:
```
python Remote.py COMMAND <DURATION> [<PWM>]
```
Available commands: 
```
	forward  
	backward  
	left  
	right
```
Duration is required parameter which determines for how long the operation will be performed.  
PWM is optional parameter which sets PWM on both motors (values 35-100, default=50)
