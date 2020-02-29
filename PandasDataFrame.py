#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from numpy.random import randn


# In[9]:


np.random.seed(101)


# In[10]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[6]:


df


# In[7]:


df['W']


# In[22]:


df['PC_Change'] = (df['W'] + df['X']) + df['X'] *100


# In[23]:


df


# In[24]:


df.drop('PC_Change',1,inplace=True)    #when inplace = True: changes the orignial data


# In[25]:


df


# In[26]:


df.loc['C']   #---> selecting a row by its' name
df.iloc[2]    #---> selecting a row by its' index


# In[11]:


df


# In[18]:


df[df['X']<0][['W','Z']]


# In[19]:


booldf = df['X']<0


# In[26]:


my_cols = ['X','Y']


# In[27]:


result = df[booldf]


# In[28]:


result[my_cols]


# In[31]:


df[df['X']<0][['X','Y']]


# In[39]:


df[(df['X']>0) & (df['Y']>0)]   #When dealing with dataframes we use "&"(and) or "|"(or) 


# In[41]:


df.reset_index()  #settign the indexes of the data frame to be numerical values (use inplace=True inorder to change the df) 


# In[42]:


Countrys = 'USA RUSSIA CHINA ISRAEL GERMANY'.split()


# In[43]:


Countrys


# In[44]:


df['Countrys'] = Countrys


# In[46]:


df.set_index('Countrys')


# In[51]:


outside = ['G1','G1','G1','G2','G2','G2']


# In[52]:


inside = [1,2,3,1,2,3]


# In[53]:


hier_index = list(zip(outside,inside))


# In[54]:


hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[55]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[56]:


df


# In[59]:


df.loc['G1'].loc[3]['B']


# In[61]:


df.index.names = ['Section','Number']


# In[62]:


df


# In[64]:


df.xs(2,level='Number')  # .xs Allows us to grab multi vals in multi level index df


# In[ ]:




