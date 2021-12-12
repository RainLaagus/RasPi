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

auto_punane = 25
jala_punane = 16
auto_kollane = 8
auto_roheline = 7
jala_roheline = 20
jala_sinine = 12
jala_nupp = 1

def button_callback(button):
    print('Button {} pressed'.format(button))
    GPIO.output(jala_sinine, True)
    global nupp
    nupp = "on"

GPIO.add_event_detect(jala_nupp, GPIO.RISING, callback=lambda x: button_callback(1), bouncetime=200)


nupp = "off"
try:
    while True:   
        GPIO.output(auto_punane, True)
        GPIO.output(jala_punane, True)
        if nupp == "on":
            GPIO.output(jala_punane, False)
            GPIO.output(jala_roheline, True)
            nupp = "off"
            GPIO.output(jala_sinine, False)
            
        time.sleep(5)
        GPIO.output(jala_punane, True)
        GPIO.output(jala_roheline, False)
        GPIO.output(auto_punane, False)
        GPIO.output(auto_kollane, True)
        time.sleep(1)
        GPIO.output(auto_kollane, False)
        GPIO.output(7, True)
        time.sleep(5)
        GPIO.output(7, False)
        
        for _ in range(0,3):
            GPIO.output(auto_kollane, True)
            time.sleep(0.4)
            GPIO.output(auto_kollane, False)
            time.sleep(0.4)
            



except KeyboardInterrupt:
    print("Keyboard interrupt")
except:
    print("Other exception")
finally:
    GPIO.cleanup()
