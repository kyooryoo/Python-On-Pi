# Pi has a group of pins for connecting external hardwares called GPIO
# General Purpose Input Output pins has states of ON/OFF or HIGH/LOW
# a GPIO pin can act as input or output but not both at the same time
# GPIO pins could be controlled with a Python package called RPI.GPIO
# RPI.GPIO is insalled on Respbian OS by default

# following code builds a LED blinker for 1 second - tested!
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
def Blink(speed):
    GPIO.output(7,True)
    time.sleep(speed)
    GPIO.output(7,False)
    time.sleep(speed)
    GPIO.cleanup()
Blink(1)

# following code add a button to control the LED blinker - tested!
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.OUT)
while True:
    input_state=GPIO.input(12)
    if input_state==False:
        #print('Button Pressed') # comment out to stop print
        GPIO.output(7,True)
    else:
        #print('Button Released') # comment out to stop print
        GPIO.output(7,False)

# PiGlow is a hardware module which has 18 small LEDs
# for control these PiGlow LEDs individually
# install library: curl get.pimoroni.com/piglow | bash
# enable I2C: sudo raspi-config -> Advanced Options
# -> A7 I2C -> enalbed<Yes> -> loaded by default<Yes>
# more info https://shop.pimoroni.com/products/piglow

# check installation execute following statements
## import piglow
## piglow.red(64) # all LEDs to red color intensity of 64/255
## piglow.show() # update PiGlow to show the change of setting
# optionally update of PiGlow could be auto by command:
## piglow.auto_update=True
# other colors include: white, blue, green, yellow, and orange
# 18 LEDs are grouped in three for individual control
## piglow.arm(0, 128) # select arm 0 and set intensity to 128/255
## piglow.set(0, 255) # set all LEDs to full brightness
## piglow.set([1,3,5],200) # set LEDs 1, 3, 5 to intensity 200/255
## piglow.set(0,[255,255,255]) # set first 3 LEDs to full intensity

# an example for control PiGlow arms be like cycle's spokes - not tested
import time
import piglow
i=0
while True:
    print(i)
    piglow.all(0) # turn off all LEDs
    # starting from next LED set 9 of them with waved intensity
    piglow.set(i%18,[15,31,63,127,255,127,63,31,15])
    piglow.show()
    i+=1 # prepare to jump to the next LED in index
    time.sleep(0.1)

# am example of binary clock with PiGlow - not tested
import piglow
from time import sleep
from datetime import datetime
piglow.auto_update=True
show12hr=1
ledbrightness=10
hourcount=0
currenthour=0 # track the change of hour
while True:
    time=datetime.now().time()
    print(str(time))
    hour=time.hour
    min=time.minute
    sec=time.second
    if show12hr==1 and hour>12:
        hour-=12
    if currenthour!=hour: # execute at the end of every hour
        hourcount=hour # prepare to flash all LEDs for o'clock
        currenthour=hour # updage track of current hour
    for x in range(6):
        # << operation bitwise left shift the binary number of x
        # & operation bitwise AND with the binary number of hour
        # for example, 3pm has hour value of 15 which is 3 in 12hr
        # 3 is 00000011 in binary, so for the first iteration of x
        # x has original value of 0 and 1 after << operation
        # the result after AND x(1) with hour(11) is 1
        # so the 13th LED is on with brightness of 10
        # next iteration have 14th LED on with brightness of 20
        # left iterations will not have any other LEDs on
        piglow.led(13+x,(hour&(1<<x))*ledbrightness)
    for x in range(6):
        piglow.led(7+x,(min&(1<<x))*ledbrightness)
    for x in range(6):
        piglow.led(1+x,(sec&(1<<x))*ledbrightness)
    # flash all LEDs as many times as the hour for every o'clock
    if hourcount!=0:
        sleep(0.5) # display the time for 0.5 second
        piglow.white(ledbrightness)
        sleep(0.5) # flash all LEDs for 0.5 second
        hourcount=hourcount-1
    else:
        sleep(0.1)

# I need a PiGlow module to play this script in practice
# how about combine hour, min, and sec settings in one for loop?