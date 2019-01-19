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

ENA = 16  
IN1 = 3
IN2 = 5
IN3 = 8
IN4 = 10
ENB = 18

# Sensor pins to GPIO pin number
TRIG = 11
ECHO = 13

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
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    GPIO.output(IN3,True)
    GPIO.output(IN4,False)
    GPIO.output(ENB,True)

def back():
    GPIO.output(ENA,True)
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(IN3,False)
    GPIO.output(IN4,True)
    GPIO.output(ENB,True)

def right():
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

def left():
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
            # Set the direction
                right()
                time.sleep(1)  # Goes right for 1 second
                break  # Goes back to going forward
            
except KeyboardInterrupt:
    # Stop the car.
    # Control C to stop
    stop()

GPIO.cleanup()

