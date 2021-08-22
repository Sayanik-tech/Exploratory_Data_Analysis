#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# Loading Dataset
athletes = pd.read_csv('athlete_events.csv')
regions = pd.read_csv('noc_regions.csv')


# In[4]:


athletes.head()


# In[5]:


regions.head()


# In[6]:


## Join the Dataframe
athletes_df = athletes.merge(regions, how = 'left', on = 'NOC')
athletes_df.head()


# In[7]:


## Shape of the Dataframe
athletes_df.shape


# In[8]:


# make the column name consistent
athletes_df.rename(columns={'region':'Region','notes':'Notes'},inplace = True)
athletes_df.head()


# In[9]:


athletes_df.info()


# In[10]:


athletes_df.describe()


# In[11]:


## check null value
athletes_df.isnull().any()
#nan_columns = nan_values.any()
#nan_columns


# In[12]:


athletes_df.isnull().sum()


# In[13]:


athletes_list=athletes_df.columns[athletes_df.isnull().any()].tolist()
athletes_list


# In[14]:


## Country details
athletes_df.query('Team == "India"').head()


# In[15]:


# Top countries participating
top_countries = athletes_df.Team.value_counts().sort_values(ascending=False).head(10)
top_countries


# In[16]:


# Plotting


# In[17]:


plt.figure(figsize=(12,6))
plt.title('overall participation by countries')
sns.barplot(x = top_countries.index, y = top_countries,palette='Set2')


# In[18]:


# Age distribution of the participants


# In[19]:


plt.figure(figsize = (12,6))
plt.title('Age distribution of the Athletes')
plt.xlabel('Age')
plt.ylabel('No of Participants')
plt.hist(athletes_df.Age, bins = np.arange(10,70,2), color = 'red', edgecolor = 'black')


# In[20]:


## Height distribution of the participants 


# In[21]:


plt.figure(figsize = (12,6))
plt.title('Height distribution of the Athletes')
plt.xlabel('Height')
plt.ylabel('No of Participants')
plt.hist(athletes_df.Height, bins = np.arange(130,230,5), color = 'orange', edgecolor = 'white')


# In[22]:


## Weight distribution of the olympics participants


# In[23]:


plt.figure(figsize = (12,6))
plt.title('Weight distribution of the Athletes')
plt.xlabel('Weight')
plt.ylabel('No of Participants')
plt.hist(athletes_df.Weight, bins = np.arange(20,160,10), color = 'blue', edgecolor = 'white')


# In[24]:


## Winter olympics sports types
winter_sports = athletes_df[athletes_df.Season == 'Winter'].Sport.unique()
winter_sports


# In[25]:


## Summer olympics sports types
summer_sports = athletes_df[athletes_df.Season == 'Summer'].Sport.unique()
summer_sports


# In[26]:


# <Male and Female Participants in olympics so far
gender_counts = athletes_df.Sex.value_counts()
gender_counts


# In[27]:


# Pie Plot for Male and Female Participants


# In[28]:


plt.figure(figsize =(12,6))
plt.title('Pie Chart For Male and Female Participants')
plt.pie(gender_counts , labels = gender_counts.index, autopct = '%1.1f%%', startangle = 150, shadow = False)


# In[29]:


# Total no of Medals
athletes_df.Medal.value_counts()


# In[30]:


## Total No of Male athletes in Each olympics and their Medals Tally


# In[31]:


Male_Participants = athletes_df[(athletes_df.Sex == 'M') & (athletes_df.Season == 'Summer')][['Sex','Year','Medal']]
Male_Participants = Male_Participants.groupby('Year').count().reset_index()
Male_Participants.tail()


# In[32]:


## How many Female participants achieve Gold Medal


# In[33]:


Goldmedal_Female = athletes_df[(athletes_df.Medal == 'Gold') & (athletes_df.Sex == 'F') & (athletes_df.Year == 2016)][['Year','Medal']]
Goldmedal_Female = Goldmedal_Female.groupby('Year').count().reset_index()
Goldmedal_Female


# In[34]:


athletes_df.head()


# In[35]:


## Gold Medal Athletes


# In[36]:


G_Medals = athletes_df[athletes_df.Medal == 'Gold']
G_Medals.head()


# In[37]:


## Gold Medal Athletes Beyond Or At the Age of 60


# In[38]:


G_Medals['ID'][G_Medals['Age'] >= 60].count()


# In[39]:


## Sporting events beyond 60 from where Gold Medals Come


# In[68]:


Sporting_Events = G_Medals['Event'][G_Medals['Age'] >=60]
Sporting_Events


# In[41]:


# Plot for Sporting Events


# In[69]:


plt.figure(figsize=(10,5))
plt.tight_layout()
sns.countplot(Sporting_Events)
plt.title('Gold medals for atheletes of Over 60 years')


# In[ ]:


## Gold Medal by each Country


# In[45]:


G_Medals['Region'].value_counts().head()


# In[ ]:


## Plotting the total Gold Medals Country wise


# In[59]:


totalgoldmedals = G_Medals['Region'].value_counts().reset_index(name = 'Medal').head()
totalgoldmedals


# In[71]:


g1 =sns.scatterplot(x ='Medal', y = 'index', data = totalgoldmedals)


# In[88]:


totalgoldmedals = G_Medals['Region'].value_counts().reset_index(name = 'Medal').head()
g2 = sns.catplot(x ='Medal', y = 'index', data = totalgoldmedals , height = 5, palette = 'rocket',kind = 'bar')
g2.set_xlabels('No of Medals')
g2.set_ylabels('Country')
plt.title('Gold Medals Per Country')


# In[ ]:


## Weight and Height comparison of atheletes who win Medals and there should be no Null values


# In[ ]:





# In[47]:


plt.figure(figsize = (15,10))
plt.title('Height (CM) Vs Weight (KG) Of Olympics Atheletes')
axis = sns.scatterplot(x = 'Height', y = 'Weight', data = not_null_medals , hue = 'Sex')


# In[ ]:


## Detais About Rio olympics


# In[50]:


max_year = athletes_df['Year'].max()
print(max_year)


# In[ ]:


## Teams as per winning medals in Rio olympics (All medals)


# In[55]:


Country_name = athletes_df[(athletes_df['Year'] == 2016) & (athletes_df['Medal'] != 'Nan')].Team
Country_name.value_counts().head(10)


# In[ ]:


## Teams as per winning Gold medals in Rio olympics


# In[89]:


Team_names = athletes_df[(athletes_df['Year'] == 2016) & (athletes_df['Medal'] == 'Gold')].Team
Team_names.value_counts().reset_index(name = 'Gold_Medal').head()


# In[85]:


Team_names.value_counts().head().index


# In[90]:


sns.barplot(x = Team_names.value_counts().head(15) , y = Team_names.value_counts().head(15).index)
plt.xlabel('country wise Gold Medal Tally for Rio Olympics')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




