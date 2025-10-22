#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp no.11


# In[2]:


#Aim: Classifier-Decision Tree


# In[3]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 10/10/2025


# In[4]:


import pandas as pd


# In[5]:


import os


# In[6]:


os.getcwd()


# In[7]:


os.chdir('C:\\Users\\mahak\\OneDrive\\Desktop')


# In[8]:


data=pd.read_csv("heart.csv")


# In[9]:


data.head()


# In[10]:


data.tail()


# In[11]:


data.info


# In[12]:


data.shape


# In[13]:


data.size


# In[14]:


data.ndim


# In[15]:


data.describe()


# Data Preprocessing _ Data Cleaning _ Missing Value Treatment

# In[16]:


data.isna()


# In[17]:


data.isna().any()


# In[18]:


data.isna().sum()


# Independent and Dependent Variables

# In[19]:


x=data.drop("target", axis=1)
y=data["target"]


# Splitting of DataSet into train and Test¶

# In[20]:


#splitting the data into training and testing data sets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=42)


# Decision Trees Algorithm

# In[29]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 


# In[30]:


dt=DecisionTreeClassifier()


# In[31]:


dt.fit(x_train, y_train)


# In[32]:


y_pred4=dt.predict(x_test)


# In[33]:


accuracy_score (y_test,y_pred4)

