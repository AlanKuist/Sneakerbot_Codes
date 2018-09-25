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

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
#car

GPIO.setup(11,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(13,GPIO.IN)
#sensor

try:
    while True:
        GPIO.output(10,True)
        GPIO.output(16,True)
        GPIO.output(18,True)
        GPIO.output(8,False)
        GPIO.output(3,False)
        GPIO.output(5,False)
        #go forward

        while True:
            GPIO.output(11,True)
            time.sleep(0.0001)
            GPIO.output(11,False)

            while GPIO.input(13) == False:
                start = time.time()

            while GPIO.input(13) == True:
                end = time.time()

            sig_time = end-start

            #cm:
            distance = sig_time / 0.000058

            print('Distance: {} cm'.format(distance)) #reads distance
            if distance < 20:      
                GPIO.output(8,True)
                GPIO.output(16,True)
                GPIO.output(18,True)
                GPIO.output(10,False)
                GPIO.output(3,False)
                GPIO.output(5,False)
                time.sleep(3)
                #goes back for 3 seconds
                GPIO.output(16,True)
                GPIO.output(18,True)
                GPIO.output(3,False)
                GPIO.output(5,True)
                GPIO.output(10,True)
                GPIO.output(8,False)
                time.sleep(3)
                #goes right
                break
except KeyboardInterrupt:
    # Stop the car.
    GPIO.output(16,False)
    GPIO.output(18,False)
    GPIO.output(5,False)
    GPIO.output(3,False)
    GPIO.output(8,False)
    GPIO.output(10,False)
  #stop 

GPIO.cleanup()
