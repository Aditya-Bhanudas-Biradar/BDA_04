#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('./Crop Production data.csv')
df


# In[8]:


df.columns


# In[9]:


df.isnull().sum()


# In[10]:


df['Production']=df['Production'].fillna('0')


# In[11]:


df.info()


# In[12]:


df.describe()


# In[13]:


df['State_Name'].value_counts()


# In[14]:


df.groupby('State_Name').value_counts()


# In[18]:



print(df.dtypes)


# In[19]:



df['Production'] = pd.to_numeric(df['Production'], errors='coerce')
print(df['Production'].isnull().sum()) 


# In[20]:



df.dropna(subset=['Production'], inplace=True)


print(df['Production'].isnull().sum())  


# In[21]:


state_production = df.groupby('State_Name')['Production'].sum().sort_values(ascending=False).reset_index()

# Plotting the top 10 states by crop production
plt.figure(figsize=(14, 6))
sns.barplot(data=state_production.head(10), x='State_Name', y='Production', palette='viridis')
plt.title('Top 10 States by Crop Production')
plt.xlabel('State')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()


# In[22]:


crop_production = df.groupby('Crop')['Production'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(14, 6))
sns.barplot(data=crop_production.head(10), x='Crop', y='Production', palette='Blues_r')
plt.title('Top 10 Crops by Production')
plt.xlabel('Crop')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()


# In[23]:


district_production = df.groupby('District_Name')['Production'].sum().sort_values(ascending=False).reset_index()
plt.figure(figsize=(14, 6))
sns.barplot(data=district_production.head(10), x='District_Name', y='Production', palette='autumn')
plt.title('Top 10 Districts by Crop Production')
plt.xlabel('District')
plt.ylabel('Total Production')
plt.xticks(rotation=45)
plt.show()


# In[24]:


crop_counts = df['Crop'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.bar(crop_counts.index, crop_counts.values, color='gold', edgecolor='black')

plt.title('Overall Distribution of the Top 10 crops that are produced all over India', fontsize=12)

plt.xticks(crop_counts.index, crop_counts.index, rotation=90)

plt.xlabel('Name of the Crop')
plt.ylabel('Total Number of Values in the Data Frame')

plt.show()


# In[25]:


plt.figure(figsize=(12, 6))
production_by_year = df.groupby('Crop_Year')['Production'].sum().reset_index()
sns.lineplot(data=production_by_year, x='Crop_Year', y='Production')
plt.title('Total Crop Production by Year')
plt.xlabel('Year')
plt.ylabel('Total Production')
plt.show()


# In[26]:


groupby_crop = df.groupby("Season")["Production"].median().reset_index()
plt.figure(figsize=(15, 5))
sns.barplot(x=groupby_crop["Season"], y=groupby_crop["Production"], palette='Blues')
plt.title("Crops produced during different Seasons.")
plt.xlabel("Season")
plt.ylabel("Production")
plt.xticks(rotation=45) 
plt.show()


# In[27]:


groupby_crop = df.groupby("State_Name")["Production"].median().reset_index().head(25)

plt.figure(figsize=(20,5))
sns.barplot(x=groupby_crop["State_Name"], y=groupby_crop["Production"], palette='plasma')
plt.title("compare the production across different States", fontsize=20)
plt.xlabel("State",  fontsize=12)
plt.ylabel("Production",  fontsize=12)
plt.xticks(rotation=45) 
plt.show()


# In[ ]:




