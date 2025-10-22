#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp no.1


# In[2]:


#Aim: To perform operation of Data acqisition


# In[3]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 25/07/2025


# In[4]:


#importing the basic library
import pandas as pd


# In[5]:


import  os


# In[6]:


os.getcwd()


# In[7]:


os.chdir('C:\\Users\\mahak\\OneDrive\\Desktop')


# In[8]:


data=pd.read_csv("diabetes.csv")


# In[9]:


data.head()


# In[10]:


data.tail()


# In[11]:


data.info()


# In[12]:


data.shape


# In[13]:


data.size


# In[14]:


data.ndim


# In[15]:


data.columns


# In[16]:


data.describe()

