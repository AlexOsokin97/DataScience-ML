#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


labels = ['Adidas', 'Nike', 'Puma']
prices = [250, 200, 120]
dictionary = {'Adidas':250, 'Nike':200, 'Puma':120}


# In[4]:


pd.Series(prices, labels)


# In[5]:


pd.Series(dictionary)


# In[6]:


ser1 = pd.Series([1,2,3,4], ['Adidas','Nike','Puma','Zara'])
ser2 = pd.Series([1,4,5,3], ['Adidas','Nike','Ready', 'Zara'])


# In[7]:


ser1


# In[8]:


ser2


# In[9]:


ser1 + ser2


# In[ ]:




