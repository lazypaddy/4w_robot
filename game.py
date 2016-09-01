#!/usr/bin/python

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import atexit
import pygame, time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)

KEYSTATE_FORWARD=False
KEYSTATE_BACKWARD=False
KEYSTATE_TURNLEFT=False 
KEYSTATE_TURNRIGHT=False

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT(addr=0x60)

################################# DC motor test!
front_left = mh.getMotor(1)
front_right= mh.getMotor(2)
back_left = mh.getMotor(3)
back_right=mh.getMotor(4)

def main():
	
	global KEYSTATE_FORWARD
	global KEYSTATE_BACKWARD
	global KEYSTATE_TURNLEFT
	global KEYSTATE_TURNRIGHT
	
	while True:

		#----------------------------------------------------------------------
		# Check for events
		for event in pygame.event.get():
			#print event

			if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_ESCAPE):
				raise SystemExit()

			elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_UP:
				KEYSTATE_FORWARD = True
			elif event.type == pygame.KEYUP and event.dict['key'] == pygame.K_UP:
				KEYSTATE_FORWARD = False

			elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_DOWN:
				KEYSTATE_BACKWARD = True
			elif event.type == pygame.KEYUP and event.dict['key'] == pygame.K_DOWN:
				KEYSTATE_BACKWARD = False

			elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_LEFT:
				KEYSTATE_TURNLEFT = True
			elif event.type == pygame.KEYUP and event.dict['key'] == pygame.K_LEFT:
				KEYSTATE_TURNLEFT = False

			elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_RIGHT:
				KEYSTATE_TURNRIGHT = True
			elif event.type == pygame.KEYUP and event.dict['key'] == pygame.K_RIGHT:
				KEYSTATE_TURNRIGHT = False

			elif event.type == pygame.KEYDOWN and event.dict['key'] == pygame.K_SPACE:
				KEYSTATE_FIRE = True
			elif event.type == pygame.KEYUP and event.dict['key'] == pygame.K_SPACE:
				KEYSTATE_FIRE = False

			#print KEYSTATE_FORWARD, KEYSTATE_BACKWARD, KEYSTATE_TURNLEFT, KEYSTATE_TURNRIGHT
			move_robot(KEYSTATE_FORWARD, KEYSTATE_BACKWARD, KEYSTATE_TURNLEFT, KEYSTATE_TURNRIGHT)



# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
	global mh
	
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

def move_robot(fwd, rev, left, right):
	
	wheel_distance = 140.0	
	turning_radius = 300.0
	#set the speed from 0 to 255
	speed = 100
	inside_speed = int(float(speed)*(1+(wheel_distance/(2*turning_radius))))
	outside_speed = int(float(speed)*(1-(wheel_distance/(2*turning_radius))))
	print "Inside Speed:", inside_speed
	print "Outside Speed", outside_speed
	global mh 
	
	direction=""

	if fwd:
		direction=direction+"Forward"
		set_speeds(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, speed, speed, speed, speed)
		
		if left:
			direction=direction+" + Left"
			set_speeds(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, inside_speed, inside_speed, outside_speed, outside_speed)

		if right:
			direction=direction+" + Right"
			set_speeds(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, outside_speed, outside_speed, inside_speed, inside_speed)

	elif rev:
		direction=direction+"Reverse"
		set_speeds(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, speed, speed, speed, speed)

		if left:
			set_speeds(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, inside_speed, inside_speed, outside_speed, outside_speed)
			direction=direction+" + Left"
		if right:
			set_speeds(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, outside_speed, outside_speed, inside_speed, inside_speed)
			direction=direction+" + Right"
	elif left:
		set_speeds(Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, speed, speed, speed, speed)
		direction=direction+"Left"
	elif right:
		set_speeds(Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.BACKWARD, speed, speed, speed, speed)
		direction=direction+"Right"
	else:
		direction="Not Moving"
		set_speeds(Adafruit_MotorHAT.RELEASE, Adafruit_MotorHAT.RELEASE, Adafruit_MotorHAT.RELEASE, Adafruit_MotorHAT.RELEASE)

	print direction
def set_speeds(fl_dir, bl_dir, fr_dir, br_dir, fl_speed=0, bl_speed=0, fr_speed=0, br_speed=0):
	
	global front_left
	global front_right
	global back_left
	global back_right

	
	front_left.run(fl_dir)
	front_right.run(fr_dir)
	back_left.run(bl_dir)
	back_right.run(br_dir)
	front_left.setSpeed(fl_speed)
	front_right.setSpeed(fr_speed)
	back_left.setSpeed(bl_speed)
	back_right.setSpeed(br_speed)

if __name__ == "__main__":
	atexit.register(turnOffMotors)
	main()
