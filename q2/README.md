## Question 2

# AIM:
It is to find the maximum number of cities that Lenna can visit with just 1$. That implies we have to find the state with the maximum number of cities and return the number of cities in that state.

This can be solved efficiently with the classical methods of Image Processing instead of trying to complicate by training ML models. We can increase accuracy by playing with the parameters to see the results changing.

# Solution:
My approach was to find the number of cities for each state in the image and return the maximum number.
1. Like in the previous solution we convert the image to its negative so that the bounding contour box is neglected.

2. We need to choose a threshold value for thresholding so that all the cities of different colors(Blue, Yellow, Purple) will be converted to black (in negative image). Ex: for 127 as the threshold value, the blue and yellow cities will be converted to black but the purple cities will remain white.

3. Now we need to identify the cities to count them. This is where hierarchy comes to play.

4. For this, we need to pass `cv2.RETR_TREE` into `cv2.findContours()` so that we will get all the contours in the image (cities, states, loops) and also we would get a ndarray called hierarchy which gives the relation between all the detected contours.

5. The hierarchy will be of the form [next, previous, first_child, parent]. Where `next` is the index of the next contour, `previous` is the id of the previous contour, `first_child` is the id of its first child contour, `parent` is the id of its parent contour. For further information regarding this hierarchy with examples, please refer [this](https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html)

6. All the state contours (outer most contours) will have hierarchy of the form [x, y, z, -1] because they won't have a parent.

7. If the last element of a hierarchy is not equal to -1, then that particular contour is a child contour (city or a loop).

8. Before that, we would want to remove all the hierarchies of contours which are not cities.

9. For this purpose, we check the shape of the contour and also the area of the contour,

10. `cv2.approxPolyDP()` function is used to find the number of edges of a contour. ex: if this returns a value 3 then the shape would be a triangle

11. As a circle will have many points we check if the value of `cv2.approxPolyDP()` is large.

12. Also the area of these circles (cities) range from 180 to 700 (rough approximatio of all areas of all cities). With these restrictions, we can filter out the hierarchies of contours of states and loops.

13. if we see the filtered hierarchies as follows:

    [2, -1, -1, 0]

    [3, 1, -1, 0]

    [-1, 2, -1, 0]

    [6, -1, -1, 4]

    [7, 5, -1, 4]
    
    [8, 6, -1, 4]
    
    [-1, 7, -1, 4]
    

    [11, -1, -1, 9]
    
    [12, 10, -1, 9]
    
    [13, 11, -1, 9]
    
    [14, 12, -1, 9]
    
    [-1, 13, -1, 9]
    
There are 3 child contours (all these three will be cities because the loops are filtered out in the above steps) for a contour of index 0 which is a parent contour (state). Similarly, for contour 9 (parent contour/state), there are 5 child contours (cities).

14. So these parent contour indices are put as keys into a dictionary and their corresponding values will be assigned with the number of child contours it has.

15. The maximum value of the values of this dictionary gives us the maximum number of cities in a single state. For the above example, it would retirn 5.

16. However, this process of detecting all the contours is not effective and few of the contours will not be detected which may result in dictionary values to be empty. For this case, I simply put a random value 5 which will be returned.

17. Playing with the condition on line 21 in `question2,py` we would get different accuracies. Ex: for `len(approx) > 8 or (area > 
180 and area < 700)` condition, 477 of first 500 images will get correct output (I submitted this solution and got 94.44 accuracy). For `len(approx) > 20 or (area > 180 and area < 700)` condition, 487 of first 500 images will get correct output.
