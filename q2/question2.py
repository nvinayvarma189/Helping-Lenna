# import required libraries

# pandas==0.22.0
# opencv-python==3.4.2.16

import cv2
import pandas as pd

answers = [] #initialize a list for storing the output (amount required by lenna ) for each image.

def max_cities(image):
	dict_states = {} #initialize a dictionary to store number of cities for each state.
	img = cv2.imread(image,0) #take in the input image as a grayscale image.
	imgneg = cv2.bitwise_not(img) #convert the image to it's negative.
	ret,thresh = cv2.threshold(imgneg,155,255,0) #threshold the image
	im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find all the contours in the image.
	filtered_hierarchy = [] #initialize a list to filter out the unwanted hirerarchy of contours.
	for i in range(len(contours)):
		approx = cv2.approxPolyDP(contours[i],0.01*cv2.arcLength(contours[i],True),True) #to check if the contour is a circle or not.
		area = cv2.contourArea(contours[i]) #calculate the area of the contour
		if (len(approx) > 8 or (area > 180 and area < 700)): #if number of side of a contour >  8 and area of the contour in [180,700].
			filtered_hierarchy.append(hierarchy[0][i].tolist()) #hierarchy[0][i] is a ndarray. convert it to list and append to filtered_hierarchy.

	for h in filtered_hierarchy:
		if (h[3] != -1): # if the contour is a child another contour
			if (h[3] not in dict_states.keys()): # store the number of cities as a value for each state as the key.
				dict_states[h[3]] = 1
			else:
				dict_states[h[3]] += 1
	if (dict_states.values()): #check if dict_states not empty.
		return max(dict_states.values())
	else: 						#the intenral contours were not detected properly.
		return 5 #a random number

for i in range(1,10001): #number of images in testing folder are given
    image_name = "./testing/"+str(i)+".png" #load the name of the image.
    sublist = [] #initialize a sublist.
    sublist.append(i) #append index of the image.
    sublist.append(max_cities(image_name))  #append the corresponding output for an image.
    answers.append(sublist) #append this sublist into answers (answers list will be of the form - [[i,j].[i,j],[i,j],[i,j]...])

df = pd.DataFrame(answers,columns=['id','number']) #initialize a dataframe and feed answers list as the data into it.
df.to_csv('submission_2.csv', sep=',',index=False) #write the dataframe to a csv file in the required format.