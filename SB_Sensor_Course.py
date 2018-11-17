# This code needs to be opened through the terminal
import RPi.GPIO as GPIO
import time
import curses
GPIO.setmode(GPIO.BOARD)

# Get the curses window, turn off echoig of keyboard to screen, turn on
# install (no waiting) key response, and use special values for cursor keys
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# Map Motor Controller pins to Pi GPIO pin number
ENA = 11  # drive motor enable
IN1 = 13  # forward
IN2 = 15  # back
IN3 = 16  # right
IN4 = 18  # left
ENB = 22  # steering motor enable

# Sensor pins to GPIO pin number
TRIG = 24
ECHO = 26

# Set up the GPIOs of the car
GPIO.setup(ENA,GPIO.OUT) 
GPIO.setup(IN1,GPIO.OUT) 
GPIO.setup(IN2,GPIO.OUT) 
GPIO.setup(IN3,GPIO.OUT) 
GPIO.setup(IN4,GPIO.OUT) 
GPIO.setup(ENB,GPIO.OUT) 

# Set up the GPIOs of the sensor
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(ECHO,GPIO.IN)

print("press 'control'+'c' to stop")

# Define each function
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

def stop():
    GPIO.output(ENA,False)
    GPIO.output(ENB,False)
    GPIO.output(IN2,False)
    GPIO.output(IN1,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,False)

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

# Get the car running     
try:
    while True:
        forward()
        # Get the sensor running
        while True:
            GPIO.output(TRIG,True)
            time.sleep(0.0001)
            GPIO.output(TRIG,False)

            while GPIO.input(ECHO) == False:
                start = time.time()

            while GPIO.input(ECHO) == True:
                end = time.time()

            sig_time = end-start

            #cm:
            distance = sig_time / 0.000058      #inches: 0.000148
             #reads distance
            if distance < 20:      
            # Set the directions
                back()
                time.sleep(3)  # Goes back for 3 seconds
                rightF()
                time.sleep(3)  # Goes right for 3 seconds
                break  # Goes back to going forward
except KeyboardInterrupt:
    # Stop the car.
    # Cntrol C
    stop()

GPIO.cleanup()

