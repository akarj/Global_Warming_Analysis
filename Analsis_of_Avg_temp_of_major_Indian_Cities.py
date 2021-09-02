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


Cities_temp_data = pd.read_csv("E:/Python/Data/Global_Warming_Spatial_Analysis/GlobalLandTemperaturesByCity.csv")


# In[3]:


Cities_temp_data.head()


# In[4]:


Indian_cities = Cities_temp_data[Cities_temp_data['Country'] == 'India']


# In[6]:


Indian_cities['City'].unique()


# In[8]:


cities = ['New Delhi', 'Visakhapatnam', 'Bombay', 'Bangalore', 'Agra','Varanasi', 'Calcutta' ]


# In[9]:


cities = Indian_cities[Indian_cities['City'].isin(cities)]
cities.head()


# In[11]:


cities['Latitude'] = cities['Latitude'].str.strip('N')


# In[12]:


cities['Longitude'] = cities['Longitude'].str.strip('E')


# In[13]:


cities.head()


# In[14]:


cities['dt'] = pd.to_datetime(cities['dt'])


# In[15]:


cities['Month'] = cities['dt'].dt.month


# In[16]:


cities.head()


# In[20]:


cities_temp = cities.groupby(['Month','City'])['AverageTemperature'].mean().to_frame().reset_index()
cities_temp.head()


# In[22]:


cities_temp.columns = ['Month','City','Mean_temp']
cities_temp.head()


# In[24]:


df = cities_temp.merge(
                    cities,
                    on = 'City' 
                )
df.head()


# In[25]:


data = df.drop_duplicates(subset=['Month_x','City'])


# In[26]:


data.head()


# In[27]:


data = data.rename(columns = {'Month_x': 'Month'}, inplace = False)


# In[28]:


data.head()


# In[29]:


data2 = data[['Month', 'City', "Mean_temp", 'Country', 'Latitude', 'Longitude']]


# In[30]:


data2.head()


# In[31]:


import plotly.graph_objs as go


# In[35]:


heatmap_data = [go.Heatmap(
    x=data2['Month'],
    y=data2['City'],
    z=data2['Mean_temp']
)]


# In[37]:


layout = go.Layout(title='Avg temp of Cities by Month')


# In[39]:


fig = go.Figure(data = heatmap_data, layout = layout)
fig.show()


# In[40]:


import folium
from folium.plugins import HeatMap
basemap = folium.Map()


# In[47]:


basemap


# In[42]:


data2.head()


# In[45]:


for id,row in data2.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup = row['Mean_temp']).add_to(basemap)


# In[46]:


basemap


# In[ ]:




