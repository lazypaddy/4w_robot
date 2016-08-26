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

def move_robot(fwd, rev, left, right):
	direction=""

	if fwd:
		direction=direction+"Forward"
		if left:
			direction=direction+" + Left"
		if right:
			direction=direction+" + Right"
	elif rev:
		direction=direction+"Reverse"
		if left:
			direction=direction+" + Left"
		if right:
			direction=direction+" + Right"
	elif left:
		direction=direction+"Left"
	elif right:
		direction=direction+"Right"
	else:
		direction="Not Moving"

	print direction

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