#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
dates = ['2017-01-05 2:30:00  PM', 'JAN 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05', '20170105']
pd.to_datetime(dates)


# In[5]:


pd.to_datetime('5/1/2017', dayfirst=True)


# In[6]:


pd.to_datetime('5$1$2017', format='%d$%m$%Y')  # in dollar format


# In[7]:


pd.to_datetime('5@1@2017', format='%d@%m@%Y')  # in @ format


# In[8]:


# if some invalide string comes then to ignore
import pandas as pd
dates = ['2017-01-05 2:30:00  PM', 'JAN 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05', 'abc']
pd.to_datetime(dates, errors='ignore')


# In[10]:


# if some invalide string comes then to run 
import pandas as pd
dates = ['2017-01-05 2:30:00  PM', 'JAN 5, 2017 14:30:00', '01/05/2017', '2017.01.05', '2017/01/05', 'abc']
pd.to_datetime(dates, errors='coerce')


# In[12]:


# using epoch time which is use to calculate the seconds from Jan 1
t = 1501356749
pd.to_datetime(t, unit='s')


# In[15]:


# using epoch time which is use to calculate the seconds from Jan 1 using array
t = 1501356749
dt = pd.to_datetime([t], unit='s')
dt


# In[16]:


# nanoseconds
dt.view('int64')


# In[ ]:




