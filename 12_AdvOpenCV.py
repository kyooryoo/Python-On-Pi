### thresholding function of OpenCV segments an image by pixel color value
### it works best on grayscale images to remove or reserve target areas
##
### following program demonstrate several threshold methos
##import cv2
##import matplotlib.pyplot as plt
##img=cv2.imread('grayscale.png',0)
##th=127 # define a threshold value
##max_val=255 # which means black in grayscale
### pixels with value > th have max_val, otherwise be 0 (white)
##ret,o1=cv2.threshold(img,th,max_val,cv2.THRESH_BINARY)
### pixels with value > th be 0, otherwise be max_val of 255
##ret,o2=cv2.threshold(img,th,max_val,cv2.THRESH_BINARY_INV)
### pixels with value > th be max_val, otherwise as before
##ret,o3=cv2.threshold(img,th,max_val,cv2.THRESH_TOZERO)
### pixels with value > th as before, otherwise be max_val
##ret,o4=cv2.threshold(img,th,max_val,cv2.THRESH_TOZERO_INV)
### pixels with value > th as before, otherwise be 0
##ret,o5=cv2.threshold(img,th,max_val,cv2.THRESH_TRUNC)
##titles=['Input Image','BINARY','BINARY_INV','TOZERO','TOZERO_INV','TRUNC']
##output=[img,o1,o2,o3,o4,o5]
##for i in xrange(6):
##    plt.subplot(2,3,i+1),plt.imshow(output[i],cmap='gray')
##    plt.title(titles[i])
##    plt.xticks([]),plt.yticks([])
##plt.show()

### values of all pixels in an grayscaled image could be plot into a histogram
### usually images with a distinct background have two peaks in such histogram
### OTSU method could be used for seperating the objects from background
##import cv2
##import matplotlib.pyplot as plt
##img=cv2.imread('tank.jpg',0)
##ret,output=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
##plt.imshow(output,cmap='gray')
##plt.xticks([]),plt.yticks([])
##plt.show()

### noise is generated from digital camera devices and can degrade image quality
### Signal-to-Noise Ratio (SiginalPower/NoisePower) describes the image quality
### Kernals are squared all one matrics that could be used for noise removal
##
### cv2.filter2D() function takes kernal as a linear filter to reduce image noise
##import cv2
##import numpy as np
##import matplotlib.pyplot as plt
##img=cv2.imread('tank.jpg',1)
##original=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
### cv2.filter2D() function takes kernal as a linear filter to reduce image noise
### -1 means output has the same depth as the source image
### np.ones((7,7),np.float32/49 create an kernal with an all one 7x7 matrics
##filter2D=cv2.filter2D(original,-1,np.ones((7,7),np.float32)/49)
### cv2.boxFilter() takes the size of matrics in kernal as the parameter
### a 3x3 matrics creates a low pass filter which keeps more detail
##boxFilter=cv2.boxFilter(original,-1,(3,3),normalize=True)
### cv2.blur() works as the same with cv2.boxFilter() with normalize always be True
##blur=cv2.blur(original,(3,3))
### cv2.GaussianBlur() is especially effective for reducing Gaussian noise
##GaussianBlur=cv2.GaussianBlur(original,(3,3),0)
##titles=['Original','Filter2D','BoxFilter','Blur','GaussianBlur']
##output=[original,filter2D,boxFilter,blur,GaussianBlur]
##for i in xrange(5):
##    plt.subplot(2,3,i+1),plt.imshow(output[i])
##    plt.title(titles[i])
##    plt.xticks([]),plt.yticks([])
##plt.show()

### cv2.medianBlur() is effective for removing salt and peper noise
### following code adds and remove salt and peper noise on sample image 
##import cv2
##import numpy as np
##import random
##import matplotlib.pyplot as plt
##img = cv2.imread('sample.jpg', 1)
##input = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
##output = np.zeros(input.shape, np.uint8)
##p = 0.2 # probablity of noise
##for i in range(input.shape[0]):
##    for j in range(input.shape[1]):
##        r = random.random()
##        if r < p / 2:
##            output[i][j] = 0, 0, 0
##        elif r < p:
##            output[i][j] = 255, 255, 255
##        else :
##            output[i][j] = input[i][j]
##noise_removed = cv2.medianBlur(output, 3)
##plt.subplot(121), plt.imshow(output), plt.title('Noisy Image')
##plt.xticks([]), plt.yticks([])
##plt.subplot(122), plt.imshow(noise_removed), plt.title('Median Filtering')
##plt.xticks([]), plt.yticks([])
##plt.show()

### morphological operations change object shape in image
##import numpy as np
##import cv2
##import matplotlib.pyplot as plt
##img = cv2.imread('tank.jpg',0)
### the extent of erosion and dilation depends on kernal size and iterations
##kernel = np.ones((3,3),np.uint8)
### erosion removes the boundaries of white objects and slims them in image
##erosion = cv2.erode(img,kernel,iterations = 2)
### dilation expands the boundaries of white objects and flattens them 
##dilation = cv2.dilate(img,kernel,iterations = 2)
### gradient returns the outline of objects in the image
##gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
##titles=['Original','Erosion','Dilation','Gradient']
##output=[img,erosion,dilation,gradient]
##for i in xrange(4):
##    plt.subplot(2,2,i+1),plt.imshow(output[i],cmap='gray')
##    plt.title(titles[i]),plt.xticks([]),plt.yticks([])
##plt.show()

# motion detection
import cv2
import numpy as np
cap=cv2.VideoCapture(0)
k=np.ones((3,3),np.uint8)
t0=cap.read()[1]
t1=cap.read()[1]
while(True):
    d=cv2.absdiff(t1,t0)
    grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(grey,(3,3),0)
    ret,th=cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(th,k,iterations=2)
    contours,hierarchy=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    t2=t0
    cv2.drawContours(t2,contours,-1,(0,255,0),2)
    cv2.imshow('Output',t2)
    t0=t1
    t1=cap.read()[1]
    if cv2.waitKey(5)==27:
        break
cap.release()
cv2.destroyAllWindows()