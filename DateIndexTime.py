#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd # opening apple stock price
df = pd.read_csv('G:\\AAPL.csv')
df


# In[7]:


type(df.Date[0]) # date column is string type


# In[9]:


df = pd.read_csv('G:\\AAPL.csv',parse_dates=['Date']) # converting string type into integer
df


# In[10]:


type(df.Date[0])  # converted to integer


# In[11]:


df = pd.read_csv('G:\\AAPL.csv',parse_dates=['Date'],index_col='Date') # first column as date  in index 
df


# In[12]:


df.index # index in date time index


# In[13]:


df['2019-05'] #of month may in 2019


# In[14]:


df['2019-05'].Close.mean() # mean close to stock price for may 2019


# In[16]:


df['2019-05-08'] # 8 may stock price


# In[17]:


df['2019-05-06':'2019-05-28'] 


# In[19]:


df.Close.resample('M').mean() # average


# In[20]:


# plotting the date vs price in time analysis monthly
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('M').mean().plot() 


# In[21]:


# plotting the date vs price in time analysis weekly
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('W').mean().plot() 


# In[22]:


# plotting the date vs price in time analysis business days (off days)
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('B').mean().plot() 


# In[23]:


# plotting the date vs price in time analysis quatrly frequensis
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('Q').mean().plot() 


# In[24]:


# plotting the date vs price in time analysis inbar from
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('W').mean().plot(kind='bar') 


# In[25]:


# plotting the date vs price in time analysis quatrly frequensis in bar
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('Q').mean().plot(kind='bar')


# In[26]:


# plotting the date vs price in time analysis monthly in bar
get_ipython().run_line_magic('matplotlib', 'inline')
df.Close.resample('M').mean().plot(kind='bar') 


# In[ ]:




