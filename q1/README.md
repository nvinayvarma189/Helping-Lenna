## Question 1

# AIM:

It is to find the number of dollars required by Lenna to travel all the states and cities. It costs 1$ to move to from one state to another state, so we have to find the number of states (individual graph blocks) in the given image.

This can be solved accurately with the classical methods of Image Processing instead of trying to complicate by training ML models.

# Solution:
  My approach was to find the number of contiguous blocks in the image. This will be the number of states in the image and hence gives us the number of dollars required by Lenna.
  
1. If we take all the contours, we would also get the cities and loops in the graphs, which are unnecessary.

2. To avoid that we can pass `cv2.RETR_EXTERNAL` into `cv2.findContours` so that only the parent contours(hierarchy level 0/ outer most contours) will be given as output. The child contours like cities, loops will be neglected.

3. With the images being white in color, there will be a contour bounding the borders of the image. When this happens, all the other contours like states, cities, and loops will become child contours to this bounding contour.

4. So if we convert the image to it's negative and then find the contours, this bounding contour will be not be detected and hence all the parent contours(states) can be retrieved through `cv2.RETR_EXTERNAL`
