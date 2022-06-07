import cv2
import numpy as np
scale = 3
layout = np.zeros((600 ,600 ,3))

c = 20

h1 = np.array([[0,599-0], [120,599-0], [120,599-120], [0,599-120]])
cv2.fillPoly(layout, pts = [h1], color =(255,255,255))

h2 = np.array([[0,599-180], [120,599-180], [120,599-240], [0,599-240]])
cv2.fillPoly(layout, pts = [h2], color =(255,255,255))
        
h3 = np.array([[0,599-300], [120,599-300], [120,599-420], [0,599-420]])
cv2.fillPoly(layout, pts = [h3], color =(255,255,255))

h4 = np.array([[0,599-480], [120,599-480], [120,599-599], [0,599-599]])
cv2.fillPoly(layout, pts = [h4], color =(255,255,255))

h5 = np.array([[480,599-599], [599,599-599], [599,599-480], [480,599-480]])
cv2.fillPoly(layout, pts = [h5], color =(255,255,255))

h6 = np.array([[480,599-420], [599,599-420], [599,599-330], [480,599-330]])
cv2.fillPoly(layout, pts = [h6], color =(255,255,255))

h7 = np.array([[480,599-240], [599,599-240], [599,599-120], [480,599-120]])
cv2.fillPoly(layout, pts = [h7], color =(255,255,255))

h8 = np.array([[480,599-60], [599,599-60], [599,599-0], [480,599-0]])
cv2.fillPoly(layout, pts = [h8], color =(255,255,255))

h9 = np.array([[480,599-60], [599,599-60], [599,599-0], [480,599-0]])
cv2.fillPoly(layout, pts = [h9], color =(255,255,255))

h10 = np.array([[285-c,599-315-c], [315+c,599-315-c], [315+c,599-285+c], [285-c,599-285+c]])
cv2.fillPoly(layout, pts = [h10], color =(255,255,255))

cv2.circle(layout,(300,599-150),45+c,(255,255,255),-1)

cv2.circle(layout,(300,599-450),45+c,(255,255,255),-1)

# cv2.imshow(" layout ", layout)
# cv2.waitKey(0)