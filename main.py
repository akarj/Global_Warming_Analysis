#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install plotly


# In[19]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)


# In[5]:


global_country = pd.read_csv("E:\Python\Data\Global_Warming_Spatial_Analysis/GlobalLandTemperaturesByCountry.csv")


# In[6]:


global_country


# In[7]:


global_country.isna().sum()


# In[8]:


global_country.dropna(axis='index', how='any', subset=["AverageTemperature"], inplace = True)


# In[9]:


global_country.isna().sum()


# In[10]:


global_country['Country'].nunique()


# In[11]:


global_country['Country'].unique()


# In[13]:


dict={
    'Congo (Democratic Republic Of The)':'Congo',
    'France (Europe)':'France',
    'Netherlands (Europe)':'Netherlands',
    'Denmark (Europe)':'Denmark',
    'United Kingdom (Europe)':'United Kingdom',
}


# In[15]:


global_country['Country'].replace(dict,inplace=True)


# In[16]:


global_country['Country'].nunique()


# In[17]:


global_country.groupby(['Country'])['AverageTemperature'].mean().to_frame().reset_index()


# In[18]:


avg_temp = global_country.groupby(['Country'])['AverageTemperature'].mean().to_frame().reset_index()
avg_temp


# In[21]:


fig = px.choropleth(avg_temp, locations='Country', locationmode='country names', color='AverageTemperature')
fig.update_layout(title = 'choropleth map of avg temp')
fig.show()


# In[ ]:




