#!/usr/bin/env python
# coding: utf-8

# EXPERIMENT 4 

# In[1]:


#Exp no.4


# In[2]:


#Aim: Missing Value Treatment


# In[3]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 29/08/2025


# In[4]:


import pandas as pd


# In[5]:


import os


# In[6]:


os.getcwd()


# In[7]:


os.chdir("C:\\Users\\mahak\\OneDrive\\Desktop")


# In[8]:


data=pd.read_csv("titanic.csv")


# In[9]:


data.head()


# In[10]:


data.info()


# In[11]:


data.shape


# In[12]:


data.size


# In[13]:


data.ndim


# In[14]:


data.columns


# In[15]:


data.describe()


# In[16]:


data.tail()


# FINDING MISSING VALUES

# In[17]:


data.isna()


# In[18]:


data.isna().any()


# In[19]:


data.isna().sum()


#  MISSING VALUE TREATMENT

# In[20]:


df1=data.fillna(data.mean())


# In[21]:


df1.isna().sum()


# 2nd METHOD

# In[22]:


df2=data["Age"].fillna(29.699118)


# In[23]:


df2.isna().sum()


# 3rd METHOD

# In[24]:


df3=data.dropna()


# In[25]:


df3


# In[26]:


df3.isna().sum()

