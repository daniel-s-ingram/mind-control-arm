#!/usr/bin/env python

import pyuarm
import serial

arm = pyuarm.uarm.UArm()
arduino = serial.Serial('/dev/ttyACM0', 9600)

maxThresh = 240
minThresh = 180
maxPeakDetected = False
signal = 0

while arduino.is_open:
	#Read raw ADC value from Arduino
	try:
		signal = int(arduino.readline().rstrip('\r\n'))
	except ValueError:
		print 'ValueError: invalid literal for int() with base 10'

	#Look for a max peak above a certain threshold
	if signal > maxThresh:
		maxPeakDetected = True

	#Look for a min peak below a certain threshold only when a max peak has already been detected
	if maxPeakDetected:
		if signal < minThresh:
			arm.set_servo_angle(2, 50.3)
			maxPeakDetected = False
			arm.set_servo_angle(2, 40.3)


arm.disconnect()