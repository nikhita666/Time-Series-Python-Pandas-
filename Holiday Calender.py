#!/usr/bin/env python
# coding: utf-8

# In[1]:


# calling the file
import pandas as pd 
df = pd.read_csv('G:\\holidays.csv')
df


# In[3]:


pd.date_range(start='06/1/2019',end='07/06/2019', freq='B') # for specific time period 


# In[6]:


from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

usb = CustomBusinessDay(calendar=USFederalHolidayCalendar())
usb


# In[7]:


# for holiday days
rng = pd.date_range(start='06/1/2019',end='07/06/2019', freq=usb)


# In[19]:


# Holiday calendar of US
# setting up index to holiday days it is not given firstly
rng = pd.date_range(start='06/01/2019',end='06/26/2019', freq=usb)
df.set_index(rng, inplace=True)
df


# In[ ]:




