#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp no.2


# In[2]:


#Aim: Central Tendancy of Measures


# In[3]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 01/08/2025


# In[4]:


age=[20,21,20,30,40,33,20,35,56,76,89,77,66,67,77,54,20,21,21,20,38,22,33,44,33,22,22,22,21,21,23,32,34,54,45,45,54,48,98,89,98,89,90,76,78,65,65,67,48,47,37,47,58,36,26]


# In[5]:


age


# In[6]:


print(age)


# In[7]:


import statistics as stats


# In[8]:


a = stats.mean(age)


# In[9]:


a


# In[10]:


b = stats.median(age)


# In[11]:


b


# In[12]:


c = stats.mode(age)


# In[13]:


c


# In[14]:


import numpy as np
x=np.array([1,2,3,4,5,6,7,2,6,2,1,4,2,2,6])


# In[15]:


x


# In[16]:


print(np.mean(x))


# In[17]:


print(np.median(x))


# In[18]:


from scipy import stats


# In[19]:


print(stats.mode(x))


# In[20]:


print(np.std(x))


# In[21]:


print(np.var(x))

