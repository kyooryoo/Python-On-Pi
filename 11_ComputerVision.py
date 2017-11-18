# Open Source Computer Vision (OpenCV) is a lib for computer vision
# released under Berkeley Software Distribution (BSD) lic, OpenCV is
# free for academic and commercial use. It has interface for C/C++,
# Python, and Java, can run on Windows, Android, and Unix like OS.
# further detail info about OpenCV is available at www.opencv.org

# update and upgrade the OS with:
# sudo apt-get update
# sudo apt-get upgrade
# sudo rpi-update
# sodu reboot -h now
# install OpenCV for Python:
# sudo apt-get install python-opencv -y

# Numpy is a matrix lib for scientific computing with Python
# which support linear algebra and container for generic data
# Numpy is used to save and process arrays of OpenCV image data
# detail about Numpy is available at http://www.numpy.org/

# import numpy as np

# Numpy has array() method for creating an array
# x=np.array([1,2,3])

# linspace() takes three paremeters of start_num, end_num and count
# which create count number elements with equal space in between
# y=np.linspace(0,8,3) # y==array([0.,4.,8.])

# Numpy array supports standalone and cross operations
# z=x**2 # z==array([1,4,9])
# z=x-y # z==array([1.,-2.,-5.])

# linear algebra functions are also supported such as:
# transpose(): permuete the dimensions of an array
# linalg.inv(): compute multiplicative inverse of a matrix
# linalg.solve(): solve a linear matrix equation
# dot(): doc product of two arrays

# following statements should be executed within Python 2
import cv2
# print cv2.__version__ # double check the lib is imported
# cv2.imread('image',mode) can import image with specified mode
# the image load mode could be color, grayscale, or alpha channel
# color: with value of "cv2.IMREAD_COLOR" or "1"
# grayscale: with value of "cv2.IMREAD_GRAYSCALE" or "0"
# alpha channel: with "cv2.IMREAD_UNCHANGED" or "-1"
# following code read sample image in color mode
# img=cv2.imread('sample.jpg',cv2.IMREAD_COLOR)
# this line of code above is the same with
img=cv2.imread('sample.jpg',1) # which is more commonly used
cv2.imshow('sample',img) # display image in "img" titled "sample"
keyPress=cv2.waitKey(0) # wait for a key press and read it to var
if keyPress==ord('q'):
    cv2.destroyWindow('sample') # destroy "sample" titled image
elif keyPress==ord('s'):
    cv2.imwrite('output.jpg',img) # !!!this coqqde does not work!!!
    cv2.destroyWindow('sample')

# matplotlib could be used for displaying images too
# install if not yet: sudo apt-get install python-matplotlib
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('sample.jpg',0)
# cv2.imread() and plt.imshow() have different color settings
# so here image is displayed in gray for correct output
plt.imshow(img,cmap='gray')
plt.title('sample')
plt.xticks([]) # disable x axis
plt.yticks([]) # disable y axis
plt.show()

# OpenCV support USB webcams to capture image or video
import cv2
# 0 in the code below is the first camera device index
# which could be found out with: ls -l /dev/video*
cam=cv2.VideoCapture(0)
# cam.read() return True or False of capture result first
# and the captured image file is returned as the second
ret,image=cam.read()
if ret:
    cv2.imshow('SnapshotTest',image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/capture/SnapshotTest.jpg',image)
cam.release()

# use OpenCV to display live video
import cv2
cam=cv2.VideoCapture(0)
dw=str(int(cam.get(3)))
dh=str(int(cam.get(4)))
print 'Default Resolution is '+dw+'x'+dh
w=1024
h=768
cam.set(3,w)
cam.set(4,h)
print 'Now resolution is set to '+str(w)+'x'+str(h)
while(True):
    # capture frame by frame
    ret,frame=cam.read()
    # display the result frame
    cv2.imshow('Video Test',frame)
    # wait for ESC key which has the value of 27
    if cv2.waitKey(1)==27:
        break
# when everything done, release the capture
cam.release()
cv2.destroyAllWindows()

# use OpenCV to write a video to file, use cv2.VideoWriter() function
# it takes paramters of Filename, FourCC, Framerate and Resolution
import cv2
cam=cv2.VideoCapture(0)
# the Four Character Code (FourCC) could be DIVX, XVID, H264, MJPG, WMV1, or WMV2
output=cv2.VideoWriter('VideoStream.avi',cv2,cv,CV_FOURCC(*'WMV2'),40.0,(640,480))
while (cam.isOpened()):
    ret,frame=cam.read()
    if ret==True:
        output.write(frame)
        cv2.imshow('VideoStream',frame)
        if cv2.waitKey(1)==27:
            break
    else:
        break
cam.release()
output.release()
cv2.destroyAllWindows()

# use OpenCV with PiCamera, show preview for 3 seconds and capture the image
import picamera
import picamera.array
import time
import cv2
with picamera.PiCamera() as camera:
    rawCap=picamera.array.PiRGBArray(camera)
    camera.start_preview()
    time.sleep(3)
    camera.capture(rawCap,format="bgr")
    image=rawCap.array
cv2.imshow("Test",image)
cv2.waitKey(0)
cv2.destoryAllWindows()

# Retrieve image properties with OpenCV functions
import cv2
img=cv2.imread('sample.jpg',1)
print 'the shape of sample image is: '+str(img.shape)
print 'the size is: '+str(img.size)
print 'the data type is: '+str(img.dtype)
img=cv2.imread('sample.jpg',0)
print 'the shape of sample image in gray is: '+str(img.shape)

# images in same size can have arithmetic operations performed
# images are stored as matrices and can be operated in same way
import cv2
img1=cv2.imread('sample.jpg',1)
img2=cv2.imread('background.jpg',1)
cv2.imshow('Image1',img1)
cv2.waitKey(0)
cv2.imshow('Image2',img2)
cv2.waitKey(0)
cv2.imshow('Addition',cv2.add(img1,img2))
cv2.waitKey(0)
cv2.imshow('Image1-Image2',cv2.subtract(img1,img2))
cv2.waitKey(0)
cv2.imshow('Image2-Image1',cv2.subtract(img2,img1))
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.split() splits an image to three color channel
# cv2.merge() merges different color arrays into a image
import cv2
img=cv2.imread('sample.jpg',1)
b,g,r=cv2.split(img)
cv2.imshow('Blue Channel',b)
cv2.imshow('Green Channel',g)
cv2.imshow('Red Channel',r)
img=cv2.merge((b,g,r))
cv2.imshow('Merged Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# negative of an image is the inversion of colors
# image in grayscale is the intensity inversion from 255
import cv2
img=cv2.imread('sample.jpg')
# cv2.cvtColor() function convert color
grayscale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
negative=abs(255-grayscale)
cv2.imshow('Original',img)
cv2.imshow('Grayscale',grayscale)
cv2.imshow('Negative',negative)
cv2.waitKey(0)
cv2.destroyAllWindows()

# logical operations of AND, OR, XOR and NOT on image
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread('barcode_hor.png',0)
img2=cv2.imread('barcode_ver.png',0)
not_out=cv2.bitwise_not(img1)
and_out=cv2.bitwise_and(img1,img2)
or_out=cv2.bitwise_or(img1,img2)
xor_out=cv2.bitwise_xor(img1,img2)
titles=['Image1','Image2','Image1 NOT','AND','OR','XOR']
images=[img1,img2,not_out,and_out,or_out,xor_out]
for i in xrange(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

# colorspace is a mathematical model used to represent colors
# OpenCV use BGR as its default, matplotlib use RGB
# others include HSV (Hue, Saturation and Value) and grayscale
# OpenCV uses cv2.cvtColor(img,conv_flag) to convert colorspace
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('sample.jpg',1)
# without converting BGR to RGB colorspace, image cannot show well
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img),plt.title('COLOR IMAGE'),plt.xticks([]),plt.yticks([])
plt.show()

# another less efficient way to conver an image from BGR to RGB
# split the image to channels and merge them back in RGB order
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('sample.jpg',1)
b,g,r=cv2.split(img)
img=cv2.merge((r,g,b))
plt.imshow(img),plt.title('COLOR IMAGE'),plt.xticks([]),plt.yticks([])
plt.show()

# for knowing all the colorspace conversion flags in OpenCV
import cv2
j=0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        print filename
        j+=1
print 'There are '+str(j)+' Colorspace Conversion flags in OpenCV'

# for converting a color from BGR to HSV and print it - test failed!!!
import cv2
import numpy as np
c=cv2.cvtColor(np.uint8[[[255,0,0]]],cv2.COLOR_BGR2HSV)
print c

# HSV colorspace recognizes color range easier - not tested!!!
# cv2.inRange() takes the upper and lower color bounds, and check range
# criteria for each pixel. Falling in range gets output 0, otherwise 255.
# This create a binary mask which could be used with bitwise_and() to
# extract the color range with the object that we are interested in.
import numpy as np
import cv2
cam=cv2.VideoCapture(0)
while(True):
    ret,frame=cam.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    green_mask=cv2.inRange(hsv,np.array([40,50,50]),np.array([80,255,255]))
    blue_mask=cv2.inRange(hsv,np.array([100,50,50]),np.array([140,255,255]))
    image_mask=cv2.add(green_mask,blue_mask)
    output=cv2.bitwise_and(frame,frame,mask=image_mask)
    cv2.imshow('Original',frame)
    cv2.imshow('Output',output)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cam.release()

# a similar example with above works on static images
import numpy as np
import matplotlib.pyplot as plt
import cv2
img_BGR=cv2.imread('sample.jpg',1)
img_HSV=cv2.cvtColor(img_BGR,cv2.COLOR_BGR2HSV)
green_mask=cv2.inRange(img_HSV,np.array([40,50,50]),np.array([80,255,255]))
blue_mask=cv2.inRange(img_HSV,np.array([100,50,50]),np.array([140,255,255]))
image_mask=cv2.add(green_mask,blue_mask)
output=cv2.bitwise_and(img_BGR,img_BGR,mask=green_mask)
cv2.imshow('Original',img_BGR)
cv2.imshow('Output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()