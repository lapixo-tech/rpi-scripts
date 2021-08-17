import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#obtener temperatura del procesador y devolverla en formato numérico
def get_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return (temp.replace("temp=","").replace("'C",""))

def blink():
    GPIO.output(18,GPIO.LOW)
    for x in range(0,3):
        GPIO.output(18,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(18,GPIO.LOW)
        time.sleep(0.5)
       
    GPIO.output(18,GPIO.HIGH)

def apagar_led():
    GPIO.output(18,GPIO.LOW)

def prender_led():
    GPIO.output(18,GPIO.HIHG)

#comenzamos con la logica del script.
if float(get_temp()) < 50:
    
    apagar_led()
    print("Temperatura Menor a 50")

if float(get_temp()) > 50:
    
    blink()
    print("Temperatura Mayor a 50")

    
    
