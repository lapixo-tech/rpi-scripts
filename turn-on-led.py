import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

for x in range(0,3):
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18,GPIO.LOW)
    time.sleep(0.5)
        
