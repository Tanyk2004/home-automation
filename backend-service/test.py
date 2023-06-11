import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_NUM = 4
GPIO.setup( GPIO_NUM, GPIO.OUT)
GPIO.output( GPIO_NUM, GPIO.LOW)
# sleep(1)
# GPIO.output(GPIO_NUM, GPIO.HIGH)
