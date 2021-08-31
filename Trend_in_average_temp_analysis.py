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


global_country = pd.read_csv("E:\Python\Data\Global_Warming_Spatial_Analysis/GlobalLandTemperaturesByCountry.csv")


# In[3]:


global_country.head()


# In[4]:


global_country.dropna(axis='index', how='any', subset=["AverageTemperature"], inplace = True)


# In[5]:


global_country.isna().sum()


# In[6]:


dict={
    'Congo (Democratic Republic Of The)':'Congo',
    'France (Europe)':'France',
    'Netherlands (Europe)':'Netherlands',
    'Denmark (Europe)':'Denmark',
    'United Kingdom (Europe)':'United Kingdom',
}


# In[7]:


global_country['Country'].replace(dict,inplace=True)


# In[8]:


global_country.groupby(['Country'])['AverageTemperature'].mean().to_frame().reset_index()


# In[9]:


Contries = ['Russia', 'United States', 'China', 'Japan', 'Australia', 'India']


# In[10]:


global_country.head()


# In[11]:


def fetch_year(date):
    return date.split('-')[0]


# In[12]:


Countries_df = global_country[global_country['Country'].isin(Contries)]
Countries_df.head()


# In[13]:


Countries_df['Years']=Countries_df['dt'].apply(fetch_year)


# In[14]:


avg_temp = Countries_df.groupby(['Years','Country']).agg({'AverageTemperature':'mean'}).reset_index()
avg_temp


# In[16]:


fig = px.line(
    avg_temp,
    x = 'Years',
    y = 'AverageTemperature',
    color = 'Country',
    title = 'trend in mean temperatures for the top Economies'
)
fig


# In[ ]:




