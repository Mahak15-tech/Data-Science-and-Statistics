#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp no.6


# In[2]:


#Aim: To perform the Data Visualization using Matplotlib


# In[3]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 19/09/2025


# In[4]:


#importing the basic library 
import numpy as np
from matplotlib import pyplot as plt


# In[5]:


x=np.arange(1,11)


# In[6]:


x


# In[7]:


y= 2*x


# In[8]:


y


# LINE CHART

# In[9]:


plt.plot(x,y)
plt.title("Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# BAR CHART

# In[10]:


plt.bar(x,y)
plt.title("Bar Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# In[11]:


colors = ['red', 'green', 'blue', 'purple', 'orange']  # Match number of bars

plt.bar(x, y, color=colors)
plt.title("Bar Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# SCATTER PLOT

# In[12]:


a=(1,5,8,6,3,7,9,4)
b=(10,55,21,64,85,33,44,28)
plt.scatter(a,b)
plt.title("Scatter Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()


# HISTOGRAM

# In[13]:


H=[1,1,1,2,6,6,6,6,4,4,4,4,4,4,3,3,10,10,10,10,2,2,7,7,7,8,8,8,8,8]


# In[14]:


plt.hist(H)
plt.show()

