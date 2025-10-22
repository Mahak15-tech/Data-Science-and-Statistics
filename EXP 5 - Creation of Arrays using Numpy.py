#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp no.5


# In[2]:


#Aim: Creation of Arrays using Numpy


# In[1]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 12/08/2025


# In[2]:


# Step 1: Importing the NumPy library
import numpy as np


# In[3]:


# Step 2: Creating a 1-D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1-D Array:")
print(arr1)


# In[4]:


# Step 3: Creating a 2-D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D Array:")
print(arr2)


# In[5]:


# Step 4: Creating an array of zeros
arr3 = np.zeros((3, 3))
print("\nArray of Zeros:")
print(arr3)


# In[6]:


# Step 5: Creating an array of ones
arr4 = np.ones((2, 4))
print("\nArray of Ones:")
print(arr4)


# In[7]:


# Step 6: Creating an array with a range of values
arr5 = np.arange(0, 10, 2)
print("\nArray using arange():")
print(arr5)


# In[8]:


# Step 7: Creating an array with equally spaced values
arr6 = np.linspace(0, 1, 5)
print("\nArray using linspace():")
print(arr6)


# In[9]:


# Step 8: Creating an identity matrix
arr7 = np.eye(4)
print("\nIdentity Matrix:")
print(arr7)


# In[10]:


# Step 9: Creating a random array
arr8 = np.random.rand(2, 3)
print("\nRandom Array:")
print(arr8)

