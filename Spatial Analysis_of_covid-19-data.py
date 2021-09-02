#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


get_ipython().system('pip install plotly')


# In[3]:


import plotly.express as px


# In[4]:


import plotly
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import init_notebook_mode, plot, iplot


# In[5]:


covid_data = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
covid_data.head()


# In[7]:


covid_data.tail()


# In[12]:


fig = px.choropleth(covid_data, locations = 'Country', locationmode='country names', color='Cumulative_cases', animation_frame='Date_reported')


# In[13]:


fig.update_layout(title = "Choropleteh map of Covid-19 Cumulative Cases till today", template='plotly_dark')
fig.show()


# In[14]:


new_cases_fig = px.choropleth(covid_data, locations = 'Country', locationmode='country names', color='New_cases', animation_frame='Date_reported')


# In[15]:


new_cases_fig.update_layout(title = "Choropleteh map of Covid-19 new Cases till today", template='plotly_dark')
new_cases_fig.show()


# In[16]:


new_cases_fig_by_continent = px.choropleth(covid_data, locations = 'Country', locationmode='country names', color='New_cases', animation_frame='Date_reported',scope='asia')
new_cases_fig_by_continent.update_layout(title = "Choropleteh map of Covid-19 New Cases till today in Asia", template='plotly_dark')
new_cases_fig_by_continent.show()


# In[ ]:




