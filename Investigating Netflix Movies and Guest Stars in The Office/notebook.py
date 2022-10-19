#!/usr/bin/env python
# coding: utf-8

# ## 1. Welcome!
# <p><img src="https://assets.datacamp.com/production/project_1170/img/office_cast.jpeg" alt="Markdown">.</p>
# <p><strong>The Office!</strong> What started as a British mockumentary series about office culture in 2001 has since spawned ten other variants across the world, including an Israeli version (2010-13), a Hindi version (2019-), and even a French Canadian variant (2006-2007). Of all these iterations (including the original), the American series has been the longest-running, spanning 201 episodes over nine seasons.</p>
# <p>In this notebook, we will take a look at a dataset of The Office episodes, and try to understand how the popularity and quality of the series varied over time. To do so, we will use the following dataset: <code>datasets/office_episodes.csv</code>, which was downloaded from Kaggle <a href="https://www.kaggle.com/nehaprabhavalkar/the-office-dataset">here</a>.</p>
# <p>This dataset contains information on a variety of characteristics of each episode. In detail, these are:
# <br></p>
# <div style="background-color: #efebe4; color: #05192d; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/office_episodes.csv</b></div>
# <ul>
#     <li><b>episode_number:</b> Canonical episode number.</li>
#     <li><b>season:</b> Season in which the episode appeared.</li>
#     <li><b>episode_title:</b> Title of the episode.</li>
#     <li><b>description:</b> Description of the episode.</li>
#     <li><b>ratings:</b> Average IMDB rating.</li>
#     <li><b>votes:</b> Number of votes.</li>
#     <li><b>viewership_mil:</b> Number of US viewers in millions.</li>
#     <li><b>duration:</b> Duration in number of minutes.</li>
#     <li><b>release_date:</b> Airdate.</li>
#     <li><b>guest_stars:</b> Guest stars in the episode (if any).</li>
#     <li><b>director:</b> Director of the episode.</li>
#     <li><b>writers:</b> Writers of the episode.</li>
#     <li><b>has_guests:</b> True/False column for whether the episode contained guest stars.</li>
#     <li><b>scaled_ratings:</b> The ratings scaled from 0 (worst-reviewed) to 1 (best-reviewed).</li>
# </ul>
#     </div>

# In[2]:


# Use this cell to begin your analysis, and add as many as you would like!
import pandas as pd
import numpy as np
k = pd.read_csv("datasets/office_episodes.csv")


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


def rColor(k):
    if k < 0.25:
        return "red"
    elif k >= 0.25 and k < 0.5:
        return "orange"
    elif k >= 0.5 and k < 0.75:
        return "lightgreen"
    else:
        return "darkgreen"
col = np.vectorize(rColor)
colarr = col(k["ratings"] / 10)


# In[5]:


def sizing(b):
    if b:
        return 250
    else:
        return 25
sizes = [sizing(b) for b in k["has_guests"]]


# In[6]:


plt.title("Popularity, Quality, and Guest Appearances on the Office")
plt.xlabel("Episode Number")
plt.ylabel("Viewership (Millions)")
plt.scatter(x = k["episode_number"], y = k["viewership_mil"], c = colarr, s = sizes)
fig = plt.figure()

