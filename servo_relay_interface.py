import RPi.GPIO as GPIO
import time


config = {
    
"leftPin": 0,
"rightPin": 0,
"afterSpdCmdDelay": 0,
"pulse_freq": 50
    
}

def angle_to_percent(angle):
    assert ((angle > 180 or angle < 0) == False)
    start = 4
    end = 12.5
    ratio = (end - start)/180 
    angle_as_percent = angle * ratio
    return start + angle_as_percent


def centerAllAxes():
    global pwmL, pwmR, config
    pwmL.start(angle_to_percent(90))
    pwmR.start(angle_to_percent(90))
    time.sleep(config["afterSpdCmdDelay"])


def pitch(angle):
    assert (-90 <= angle <= 90)
    angle += 90
    pwmL.start(angle_to_percent(180-angle))
    pwmR.start(angle_to_percent(angle))
    time.sleep(config["afterSpdCmdDelay"])


def __initialize():
    global GPIO, pwmL, pwmR
    GPIO.setmode(GPIO.BOARD) #Use Board numerotation mode
    GPIO.setwarnings(False) #Disable warnings


    frequence = config["pulse_freq"]
    GPIO.setup(config["leftPin"], GPIO.OUT)
    GPIO.setup(config["rightPin"], GPIO.OUT)
    pwmL = GPIO.PWM(config["leftPin"], frequence)
    pwmR = GPIO.PWM(config["rightPin"], frequence)


def __shutdown():
    #Close GPIO & cleanup
    pwmL.stop()
    pwmR.stop()
    GPIO.cleanup()

print("Hardware-software interface ready.")
