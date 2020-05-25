#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
df = pd.read_csv('G:\\MSFTwodate.csv')
df# file executing 


# In[27]:


df = pd.read_csv('G:\\MSFTwodate.csv',index_col='Open')
df


# In[28]:


df = pd.read_csv('G:\\MSFTwodate.csv',index_col='Open')
df


# In[40]:


# range for june month (weekends also included ) for Business day as frequency is B
rng = pd.date_range(start='05/28/2019',end='05/12/2020', freq='B')
rng


# In[41]:


# put the above date to DataFrame
df.set_index(rng,inplace=True)
df


# In[42]:


# to plot the data
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.plot()


# In[43]:


df['2019-05-28':'2019-06-06'] # 10 days dat


# In[44]:


df['2019-05-28':'2019-06-06'].Close.mean() # mean


# In[45]:


# weekend days prices by using padding method
df.asfreq('D',method='pad')


# In[46]:


# week  prices by using padding method
df.asfreq('W',method='pad')


# In[47]:


# hour  prices by using padding method
df.asfreq('H',method='pad')


# In[48]:


#only starting is specific not ending and for x periods we have to find
rng = pd.date_range(start='01/01/2020',periods=45, freq='B')
rng


# In[50]:


# generate the range in random manner in given specific series 
import numpy as np
ts = pd.Series(np.random.randint(1,10,len(rng)),index=rng)
ts

