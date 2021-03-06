import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Set pin number configuration to BCM numbering
 #button set to GPIO2
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False) # Ignore warning for now

def button_callback(channel):
    print("Button was pushed!")


GPIO.add_event_detect(2, GPIO.FALLING, callback=button_callback, bouncetime=630)

try:
    while True:
            time.sleep(20) #you can put every value of sleep you want here..

except KeyboardInterrupt:
    GPIO.cleanup()
