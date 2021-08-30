#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)


# In[3]:


global_temp=pd.read_csv('E:/Python/Data/Global_Warming_Spatial_Analysis/GlobalTemperatures.csv')
global_temp.head()


# In[4]:


global_temp['dt'][0].split('-')[0]


# In[5]:


def fetch_year(date):
    return date.split('-')[0]


# In[7]:


global_temp['years'] = global_temp['dt'].apply(fetch_year)


# In[8]:


global_temp.head()


# In[10]:


data = global_temp.groupby('years').agg({'LandAverageTemperature':'mean', 'LandAverageTemperatureUncertainty':'mean'}).reset_index()


# In[11]:


data.head()


# In[12]:


data['Uncertainity Top'] = data['LandAverageTemperature'] + data['LandAverageTemperatureUncertainty']
data['Uncertainity Bottom'] = data['LandAverageTemperature'] - data['LandAverageTemperatureUncertainty']
data.head()


# In[13]:


data.columns


# In[15]:


fig=px.line(
    data, 
    x='years', y=['LandAverageTemperature', 'Uncertainity Top', 'Uncertainity Bottom'],
    title='Avg Land temp in World'
    )
fig.show()


# In[16]:


global_temp['dt'][0].split('-')[1]


# In[17]:


global_temp['dt'] = pd.to_datetime(global_temp['dt'])


# In[18]:


global_temp['month'] = global_temp['dt'].dt.month
global_temp.head()


# In[19]:


def get_season(month):
    if month >=3 and month <= 5:
        return 'spring'
    elif month >=6 and month <= 8:
        return 'summer'
    elif month >=9 and month <= 11:
        return 'autumn'
    else:
        return 'winter'


# In[20]:


global_temp['season'] = global_temp['month'].apply(get_season)


# In[21]:


global_temp.head()


# In[24]:


years = global_temp['years'].unique()


# In[23]:


years


# In[25]:


spring_temps = []
summer_temps = []
autumn_temps = []
winter_temps = []


# In[27]:


for year in years:
    current_df = global_temp[global_temp['years']==year]
    spring_temps.append(current_df[current_df['season'] == 'spring']['LandAverageTemperature'].mean())
    summer_temps.append(current_df[current_df['season'] == 'summer']['LandAverageTemperature'].mean())
    autumn_temps.append(current_df[current_df['season'] == 'autumn']['LandAverageTemperature'].mean())
    winter_temps.append(current_df[current_df['season'] == 'winter']['LandAverageTemperature'].mean())


# In[29]:


spring_temps

season = pd.DataFrame()
# In[32]:


season = pd.DataFrame()
season['year'] = years
season['Winter Temp'] = winter_temps
season['Spring Temp'] = spring_temps
season['Summer Temp'] = summer_temps
season['Autumn Temp'] = autumn_temps


# In[33]:


season.head()


# In[34]:


season.columns


# In[36]:


fig = px.line(
    season,
    x='year',
    y=['Winter Temp', 'Spring Temp', 'Summer Temp', 'Autumn Temp'],
    title='Season Wise Average Temperage'
)

fig


# In[ ]:




