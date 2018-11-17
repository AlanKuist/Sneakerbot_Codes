# import curses and GPIO
# curses allows keyboard input
import curses
import RPi.GPIO as GPIO
#set GPIO numbering mode
# BOARD mode refers to PHYSCAL  pin numbers, not functional GPIO names
# if you want functional GPIO names use GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD) 
# Map Motor Controller pins to Pi GPIO pin number
ENA = 11
IN1 = 13
IN2 = 15
IN3 = 16
IN4 = 18
ENB = 22

GPIO.setup(ENA,GPIO.OUT) # drive motor enable
GPIO.setup(IN1,GPIO.OUT) # forward
GPIO.setup(IN2,GPIO.OUT) # back
GPIO.setup(IN3,GPIO.OUT) # right
GPIO.setup(IN4,GPIO.OUT) # left
GPIO.setup(ENB,GPIO.OUT) # steering motor enable


# ***** This need to be run via the terminal for curses app to function *****
#This enables the keypad 
# Get the curses window, turn off echoig of keyboard to screen, turn on
# install (no waiting) key response, and use special values for cursor keys
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
stdscr = curses.initscr()
stdscr.keypad(True)

# Keyboard function menu
print("***** This need to be run via the terminal for curses app to function *****\r")
print("Use arrow keys for:\r")
print(" ^ forward\r")
print(" v reverse\r")
print(" < forward left\r")
print(" > forward right\r")
print(" ENTER or OK = stop\r")
print("Q = quit & exit\r")
print("A = backwards left\r")
print("D = backwards right\r")

def forward():
    GPIO.output(ENA,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
    GPIO.output(ENB,True)
    
def back():
    GPIO.output(ENA,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)
    GPIO.output(ENB,True)

def rightF():
    GPIO.output(ENA,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    GPIO.output(ENB,True)

def leftF():
    GPIO.output(ENA,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    GPIO.output(ENB,True)

def rightB():
    GPIO.output(ENA,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    GPIO.output(ENB,True)

def leftB():
    GPIO.output(ENA,True)
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    GPIO.output(ENB,True)

def stop():
    GPIO.output(ENA,False)
    GPIO.output(ENB,False)
    GPIO.output(IN2,False)
    GPIO.output(IN1,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

#define all the functions
try:
    while True:
#This lets you control it through the terminal until the letter "q" is pressed
        char = screen.getch()
        if char == ord('q'):
            break
#this sets the keys to each function
        elif char == curses.KEY_UP: 
            forward()
        elif char == curses.KEY_DOWN: 
            back()
        elif char == curses.KEY_LEFT: 
            leftF()
        elif char == curses.KEY_RIGHT: 
            rightF()
        elif char == ord('a'): 
            leftB()
        elif char == ord('d'): 
            rightB()
        elif char == 10:  #enter
            stop()

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
    # needed to set all GPIO pins to OFF for safety
    GPIO.cleanup()
