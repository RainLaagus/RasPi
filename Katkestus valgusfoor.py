import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


GPIO.add_event_detect(1, GPIO.RISING)

nupp = "off"
try:
    while True:
        
            
        GPIO.output(25, True)
        GPIO.output(16, True)
        if nupp == "on":
            if nupp_p6leb == "jah":
                GPIO.output(12, True)
            
            GPIO.output(16, False)
            GPIO.output(20, True)
            nupp = "off"
            GPIO.output(12, False)
        time.sleep(5)
        GPIO.output(16, True)
        GPIO.output(20, False)
        GPIO.output(25, False)
        GPIO.output(8, True)
        time.sleep(1)
        GPIO.output(8, False)
        GPIO.output(7, True)
        time.sleep(5)
        GPIO.output(7, False)
        for _ in range(0,3):
            GPIO.output(8, True)
            time.sleep(0.4)
            GPIO.output(8, False)
            time.sleep(0.4)
        nupp_p6leb = "ei"
        if GPIO.event_detected(1):
            GPIO.output(12, True)
            nupp_p6leb = "jah"
            nupp = "on"



except KeyboardInterrupt:
    print("Keyboard interrupt")
except:
    print("Other exception")
finally:
    GPIO.cleanup()
