#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)


# In[2]:


state_temp = pd.read_csv("E:/Python/Data/Global_Warming_Spatial_Analysis/GlobalLandTemperaturesByState.csv")
state_temp.head()


# In[3]:


filter = state_temp['Country'] == 'United States'
USA_State_Temp = state_temp[filter]


# In[4]:


USA_State_Temp.head()


# In[5]:


USA_State_Temp.dropna(axis='index', how='any', subset=["AverageTemperature"], inplace = True)


# In[6]:


USA_State_Temp.head()


# In[7]:


USA_State_Temp['State'].unique()


# In[8]:


state = {
    'District Of Columbia':'Columbia',
    'Georgia (State)':'Georgia'
}


# In[9]:


USA_State_Temp['State'].replace(state, inplace=True)


# In[10]:


USA_State_Temp = USA_State_Temp[['AverageTemperature','State']]


# In[11]:


USA_State_Temp.head().reset_index()


# In[12]:


USA_State_Temp = USA_State_Temp.groupby('State')['AverageTemperature'].mean().reset_index()
USA_State_Temp.head()


# In[13]:


get_ipython().system('pip install opencage')


# In[14]:


from opencage.geocoder import OpenCageGeocode


# In[15]:


key = 'f38486c8be304643b3ba9af7bb587814'


# In[16]:


geocoder = OpenCageGeocode(key)


# In[17]:


location = 'Lucknow,India'
results = geocoder.geocode(location)
results


# In[18]:


location = [results[0]['geometry']['lat'],results[0]['geometry']['lng']]
location


# In[19]:


list_lat = []
list_lng = []


# In[20]:


USA_State_Temp.head()


# In[21]:


for state in USA_State_Temp["State"]:
    result = geocoder.geocode(state)
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    list_lat.append(lat)
    list_lng.append(lng)


# In[22]:


USA_State_Temp['Lat'] = list_lat
USA_State_Temp['Lon'] = list_lng


# In[23]:


USA_State_Temp.head()


# In[24]:


get_ipython().system('pip install folium')
import folium


# In[25]:


from folium.plugins import HeatMap


# In[26]:


Basemap = folium.Map()
Basemap


# In[27]:


USA_State_Temp[['Lat','Lon','AverageTemperature']]


# In[28]:


HeatMap(USA_State_Temp[['Lat','Lon','AverageTemperature']]).add_to(Basemap)
Basemap


# In[ ]:


|

