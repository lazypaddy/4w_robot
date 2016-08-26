#import RPi.GPIO as GPIO # Import the GPIO Library
import os 
import time # Import the Time library
import curses

   
# Here starts the code to make the robot move
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.nodelay(1)  #nodelay(1) give us a -1 back when nothing is pressed
keys = ' '

forward = False
reverse = False

while keys != ord('q'):
   #Start of while loop
   stdscr.refresh()
   
   keys = stdscr.getch() #Gets the key which is pressed
      
   stdscr.addch(20,25,keys)

   if  keys == ord('a'):
      if reverse: print "Left and Reverse"
      else: print "Left and Forward"

   if keys == ord('d'):
      if reverse: print 'Right and Forward'
      else: print 'Right and Reverse'

   if keys == ord('s'):
      print 'Reverse'
      reverse = True

   
   if keys == ord('w'):
      print 'Forward'
      reverse = False
   
   #if keys == int('-1'):
      #print 'error'
      
   time.sleep(0.04) #I need the timesleep because if not the robot will get a -1 all the time and not move to fast while loop I think, have to work on this.
   #End of while loop
   
#Important to set everthing back by end of the script

curses.nocbreak()
stdscr.keypad(0)
curses.endwin()