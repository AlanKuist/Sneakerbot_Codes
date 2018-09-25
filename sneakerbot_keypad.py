#This need to be opened throught the terminal"""
# import curses and GPIO
import curses
import RPi.GPIO as GPIO
#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT) # left
GPIO.setup(5,GPIO.OUT) #right
GPIO.setup(8,GPIO.OUT) #back
GPIO.setup(10,GPIO.OUT) #forward
GPIO.setup(16,GPIO.OUT) #enable
GPIO.setup(18,GPIO.OUT) #enable

# Get the curses window, turn off echoig of keyboard to screen, turn on
# install (no waiting) key response, and use special values for cursor keys
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
stdscr = curses.initscr()
stdscr.keypad(True)
#This enables the keypad and the GPIOs
def forward():
    GPIO.output(10,True)
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(8,False)
    GPIO.output(3,False)
    GPIO.output(5,False)
    
def back():
    GPIO.output(8,True)
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(10,False)
    GPIO.output(3,False)
    GPIO.output(5,False)

def rightF():
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(3,False)
    GPIO.output(5,True)
    GPIO.output(10,True)
    GPIO.output(8,False)

def leftF():
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(5,False)
    GPIO.output(3,True)
    GPIO.output(10,True)
    GPIO.output(8,False)

def rightB():
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(3,False)
    GPIO.output(5,True)
    GPIO.output(8,True)
    GPIO.output(10,False)

def leftB():
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(5,False)
    GPIO.output(3,True)
    GPIO.output(8,True)
    GPIO.output(10,False)

def stop():
    GPIO.output(16,False)
    GPIO.output(18,False)
    GPIO.output(5,False)
    GPIO.output(3,False)
    GPIO.output(8,False)
    GPIO.output(10,False)

#define all the functions
try:
    while True:

        char = screen.getch()
        if char == ord('q'):
            break
#This lets you control it through the terminal until the letter "q" is pressed
        elif char == curses.KEY_UP: 
            forward()
        elif char == curses.KEY_DOWN: 
            back()
        elif char == curses.KEY_RIGHT: 
            rightF()
        elif char == ord('a'): 
            leftB()
        elif char == 10:  #enter
            stop()
        elif char == curses.KEY_LEFT: 
            leftF()
        elif char == ord('d'): 
            rightB()
#this sets the keys to each function

finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
