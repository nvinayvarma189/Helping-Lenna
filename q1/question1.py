# import required libraries

# pandas==0.22.0
# opencv-python==3.4.2.16

import cv2
import pandas as pd

answers = [] #initialize a list for storing the output (amount required by lenna ) for each image.

def num_states(image):
	img = cv2.imread(image,0) #take in the input image as a grayscale image.
	imgneg = cv2.bitwise_not(img) #convert the image to it's negative.
	ret,thresh = cv2.threshold(imgneg,127,255,0) #threshold the image.
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #find the contours with hierarchy-0
	return len(contours) 

for i in range(1,10001): #number of images in testing folder are given
    image_name = "./testing/"+str(i)+".png" #load the name of the image.
    sublist = [] #initialize a sublist.
    sublist.append(i) #append index of the image.
    sublist.append(num_states(image_name)) #append the corresponding output for an image.
    answers.append(sublist) #append this sublist into answers (answers list will be of the form - [[i,j].[i,j],[i,j],[i,j]...])


df = pd.DataFrame(answers,columns=['id','amount']) #initialize a dataframe and feed answers list as the data into it.
df.to_csv('submission_1.csv', sep=',',index=False) #write the dataframe to a csv file in the required format.

