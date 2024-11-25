import RP1.GPIO as GPIO
import time
import os
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup(10, GPIO.OUT)
GPIO.setup (21, GPIO.IN)
while True:
    input_state = GPIO.input(21)
    if input_state == True:
        GPIO.output(10,1)
        print ('Motion Detected')
        os.system("/home/pi/program/pushbullet.sh Alert Motion Detected.")
        time.sleep(2)
        GPIO.output(10,0)
        time.sleep(2)