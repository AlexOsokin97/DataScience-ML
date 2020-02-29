
#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np


# In[2]:


list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]


# In[3]:


arr1 = np.array(list1)
arr2 = np.array(list2)
arr3 = np.array(list3)


# In[8]:


mat1 = np.array([arr1,arr2,arr3])


# In[9]:


mat1


# In[12]:


np.arange(0,11, 2)    #np.arange allows us to create arrays quickly


# In[14]:


np.zeros((3,5))  #by passing a tuple (3,5) I created a 2d array with 3 rows and 5 columns filled with zeros


# In[18]:


np.linspace(0,10,15)      #Return evenly spaced numbers over a specified interval


# In[26]:


np.eye(6)     #Return a 2-D array with ones on the diagonal and zeros elsewhere.


# In[31]:


np.random.rand(5,5)          #Random values (0-1) in a given shape (1D - 2D).


# In[44]:


np.random.randn(5,5)      #Return a sample (or samples) from the "standard normal" distribution.


# In[49]:


np.random.randint(0,101,(5,5))      #Return random integers from `low` (inclusive) to `high` (exclusive) (1D array or 2D array).


# In[55]:


arr = np.arange(25)
arr.reshape(5,5)    # n_array.reshape Returns an array containing the same data with a new shape(must be the same size!). 


# In[56]:


ranarr = np.random.randint(0,100,10)
print(ranarr)


# In[59]:


ranarr.max()    #Returns max value in ranarr


# In[60]:


ranarr.argmax()    #returns the index of max value in ranarr


# In[61]:


ranarr.min()


# In[62]:


ranarr.argmin()


# In[64]:


ranarr.shape  #returns the shape of given array (1D or 2D)


# In[67]:


ranarr.dtype   #returns the data type of given array


# In[ ]:




