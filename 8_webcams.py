# this is a study note for webcam applications with Pi
# content is pending for testing with a USB webcam or Pi Camera module

# USB webcams could be used on Pi, compatible devices could be checked 
# at http://elinux.org/RPi_USB_Webcams

# the terminal command "lsusb" list all connected USB devices

# fswebcam is a command line utility that captures images from webcam
# for install fswebcam: sudo apt-get install fswebcam
# prepare a folder for images: mkdir /home/pi/capture
# capture: fswebcam -r 1280x960 --no-banner ~/capture/camtest.jpg
# resolution has other options, --no-banner disables timestamp banner

# Cron is a time-based task scheduler configured with "crontab" file
# syntax for crontab is: 1 2 3 4 5 /location/command
# in which 1 to 5 defines Minutes, Hours, Days, Months, Days of the week
# with values of 0-59, 0-23, 0-31, 0-12, and 0-7
# for detail http://www.adminschoice.com/crontab-quick-reference
# example: * * * * * /location/command 2>&1 execute command every minute
# for executing the task every 5 minutes, use */5 * * * *
# for executing the task every 2 hours, use * */2 * * *
# "2>&1" disables default setting of email sending to administrator

# timelapse photography capture images in regular and play them with a
# higher frequency. For example, capture one image per minute for 10
# hours and combine them to a video with 30 images per second. The total
# 600 images are compressed into a 20 seconds video.

# For doing this create script file timelapse.sh under /home/pi/capture
## #!/bin/bash
## DATE=$(date+"%Y-%m-%d_%H%M")
## fswebcam -r 1280x960 --no-banner /home/pi/capture/garden_$DATE.jpg
# make the file timelapse.sh executable using: chmod +x timelapse.sh
# in terminal open crontab with: crontab -e
# add the line of script: * * * * * /home/pi/capture/timelapse.sh 2>&1

# For encoding the images into a video, use mencoder utility
# install mencoder: sudo apt-get install mencoder
# navigate to image dir: cd /home/pi/capture
# create image list file: ls garden_*.jpg > timelapse.txt
# create the video with the command: mencoder -nosound -ovc lavc
# -lavcopts vcodec=mpeg4:aspect=16/9:vbitrate=8000000 -vf scale=1290:960
# -o timelapse.avi -mf type=jpeg:fps=30 mf://@timelapse.txt
# for detail help with mencoder: man mencoder

# use webcam to record a video with avconv utility
# install: sudo apt-get install libav-tools
# record with command: avconv -f video4linux2 -r 25 -s 1280x960
# -i /dev/video0 ~/capture/VideoStream.avi
# terminate the recording: Ctrl+c
# play the video: omxplayer ~/capture/VideoStream.avi

# Pi have camera module that could be connected to CSI port
# these cameras could be configured with raspi-config utility
# capture an image: respistill -o /home/pi/capture/cam_module_pic.jpg
# a 20 seconds video: respivid -o /home/pi/capture/test.avi -t 20000
# check the content under /home/pi/capture for the output
# use command "echo $?" to check whether execution is success
# instead of fswebcam, respistill can also record timelapse sequence

# Pi camera module have an API in Python called picamera
# install: sudo apt-get install python-picamera
# following code capture an image:
import picamera
import time
with picamera.PiCamera() as cam:
    cam.resolution(1024,768)
    cam.start_preview() # start preview of the captured image
    time.sleep(5) # wait 5 seconds before capture the image
    cam.capture('/home/pi/capture/still.jpg')
# for timelapse photography with picamera:
import picamera
import time
with picamera.PiCamera() as cam:
    cam.resolution=(1024,768)
    cam.start_preview()
    time.sleep(3)
    for count, imagefile in enumerate(cam.capture_continuous('/home/pi/capture/image{counter:02d}.jpg')):
        print 'Capturing and saving ' + imagefile
        time.sleep(1)
        if count == 10:
            break
# more examples and API reference for picamera module at
# http://picamera.readthedocs.org/
        