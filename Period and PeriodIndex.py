#!/usr/bin/env python
# coding: utf-8

# In[1]:


# opening the period which is x(any period) ending in december i.e 'A-DEC' 
import pandas as pd
y = pd.Period('2020')
y


# In[2]:


dir(y) # all the properties


# In[3]:


y.start_time


# In[4]:


y.is_leap_year


# In[5]:


# montly time period as frequency is M
m = pd.Period('2020-1', freq='M')
m


# In[6]:


y.end_time


# In[7]:


# month you want
m+1


# In[8]:


m+7


# In[14]:


# quaterly timeperiod
q = pd.Period('2017Q1')
q


# In[15]:


q+1


# In[16]:


# quaterly timeperiod starting from Jan
q = pd.Period('2017Q1', freq='Q-JAN')
q


# In[17]:


q.start_time


# In[18]:


#converting quaterly time to montly
q.asfreq('M',how='start')


# In[19]:


#converting quaterly time to montly another
q2 = pd.Period('2019Q1', freq='Q-JAN')
q2


# In[21]:


q2-q # difference of two 


# In[22]:


# change the periods that you want to identify
idx = pd.period_range('2011', '2020', freq='Q-JAN')
idx


# In[24]:


idx[22]


# In[25]:


idx[22].start_time


# In[26]:


idx[22].end_time


# In[28]:


# just give the periods
idx = pd.period_range('2011', periods=20, freq='Q-JAN')
idx


# In[31]:


# to create the series
import numpy as np
ps = pd.Series(np.random.randn(len(idx)), idx)
ps


# In[32]:


# period index
ps.index


# In[34]:


#converted to date time index
pst = ps.to_timestamp()
pst


# In[35]:


# checking 
pst.index


# In[36]:


#date time index to period time index
pst.to_period()

