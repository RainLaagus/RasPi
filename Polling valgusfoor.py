import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

while True:
    GPIO.output(24, True)
    time.sleep(5)
    GPIO.output(24, False)
    GPIO.output(08, True)
    time.sleep(1)
    GPIO.output(08, False)
    GPIO.output(07, True)
    time.sleep(5)
    GPIO.output(07, False)
    for _ in range(0,3):
        GPIO.output(08, True)
        time.sleep(0.4)
        GPIO.output(08, False)
        time.sleep(0.4)