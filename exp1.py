#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
color_image=cv2.imread('sun2.jpg',1)
cv2.imshow('sun2',color_image)
cv2.waitKey(0)


# In[4]:


import cv2
color_image = cv2.imread('sun2.jpg',1)
h = cv2.imwrite('sun2.jpg',color_image)
cv2.imshow('hari',color_image)
cv2.waitKey(0) 


# In[5]:


import cv2
color_image = cv2.imread('sun2.jpg',1)
print(color_image.shape)


# In[ ]:


import random
import cv2
color_image = cv2.imread('sun2.jpg',1)
for i in range(150):
    for j in range(color_image.shape[1]):
        color_image[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('sun2.jpg',color_image)
cv2.waitKey(0)


# In[ ]:


import cv2
color_image = cv2.imread('sun2.jpg',1)
part = color_image[300:400,300:400]
color_image[50:150,50:150] = part
cv2.imshow("hari",color_image)
cv2.waitKey(0)


# In[ ]:




