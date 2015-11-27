import cv2
import numpy as np 


i=34
img = cv2.imread('test_image1.jpg')





#################### kernel processing##################
##kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))


# IGNORE THIS BIT
##erosion = cv2.erode(img,kernel,iterations = 1)
##dilation = cv2.dilate(img, kernel, iterations = 3)
##
##opening = cv2.dilate(erosion, kernel, iterations = 1)
##closing = cv2.erode(dilation, kernel, iterations = 1)




################ contouring#######################

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # makes it grayscale 
##cv2.imshow('gs',gray)
ret,thresh = cv2.threshold(gray,127,255,0) #thresholds it

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)# finds the contours
cv2.drawContours(img,contours,40,(0,0,255),1) # draws the contours

##################### CONTOUR FILTERING #################
##print "Area = ", cv2.contourArea(contours[i])
for count in range(len(contours)):
    if cv2.contourArea(contours[count]) < 400: # 400 is the best yet
        pass
    
    elif cv2.contourArea(contours[count]) > 2000:
        pass
    else:
        cv2.drawContours(img,contours,count,(0,255,0),2)
        



###########################################################################################
cv2.imshow('image',img)
#cv2.imshow("thresh",thresh)
## Close and exit
cv2.waitKey(0)
cv2.destroyAllWindows()
