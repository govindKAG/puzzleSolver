import cv2
import numpy as np 

##def color_grayscale(filename, g):
##     img=cv2.imread("D:\\govind\\eyantra\\PS2_Task1\\Task1_Practice\\test_images\\"+filename)
##     if g== 1 :
##          grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##          return grayImg
##     else: return img
##
##
##
##myim=color_grayscale("test_image1.jpg",1)
##cv2.imshow("my image",myim)
##
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##
##
##
i=-1
img = cv2.imread('test_image1.jpg')
#################### kernel processing##################
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))



erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 3)

opening = cv2.dilate(erosion, kernel, iterations = 1)
closing = cv2.erode(dilation, kernel, iterations = 1)
################ contouring#######################
gray = cv2.cvtColor(dilation,cv2.COLOR_BGR2GRAY)
cv2.imshow('gs',gray)
ret,thresh = cv2.threshold(gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,i,(0,255,0),3)
cv2.imshow('image',img)
cv2.imshow("thresh",thresh)
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
