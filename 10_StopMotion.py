# stop-motion animation is a video of sequenced images
# which has an object appears to movie on its own

# prepare the dir for saving stopmotion images
# mkdir /home/pi/stopmotion
# cd /home/pi/stopmotion

# - not tested
import picamera
from RPi import GPIO
# use Broadcom convention rather than pin number
GPIO.setmode(GPIO.BCM)
# configure the 17th pin as input and default of pulled up
GPIO.setup(17,GPIO.IN,GPIO.PUD_UP)
with picamera.PiCamera() as camera:
    camera.vflip=False # change to True if need vertical flip
    camera.hflip=False # change to True if need horizontal flip
    camera.start_preview()
    frame=1 # prepare the number subset of image file name
    # following infinite loop take photos when button pressed
    while True:
        # next statements do not execute until pin 17 signal falls
        # which means a button could control the image capture
        GPIO.wait_for_edge(17,GPIO.FALLING)
        camera.capture('/home/pi/stopmotion/frame%03d.jpg' % frame)
        frame+=1
    camera.stop_preview()
# check the space of SD card for avoiding using up its space
# press Ctrl+c to terminate the program

# use ffmpeg utility to render the video from stopmotion images
# install ffmpeg lib: sudo apt-get install ffmpeg
# check installation: avconv
# navigate to image folder: cd /home/pi/stopmotion
# render the video: avconv -r 10 -qscale 2 -i frame%03d.jpg animation.mp4
# -r specifies the frame rate for the video
# -qscale specifies the quality for the video which can range from 2-5
# -i specifies the input stopmotion image files
# play the video with: omxplayer animation.mp4
# test Pi Camera: respistill -o image.jpg# 