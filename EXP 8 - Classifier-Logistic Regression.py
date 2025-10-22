#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exp no.8


# In[2]:


#Aim: Classifier-Logistic Regression


# In[3]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 26/09/2025


# In[4]:


import pandas as pd


# In[5]:


import warnings
warnings.filterwarnings('ignore')


# In[6]:


import os


# In[7]:


os.getcwd()


# In[8]:


os.chdir('C:\\Users\\mahak\\OneDrive\\Desktop')


# In[9]:


data=pd.read_csv("heart.csv")


# In[10]:


data.head()


# In[11]:


data.tail()


# In[12]:


data.info


# In[13]:


data.shape


# In[14]:


data.size


# In[15]:


data.ndim


# In[16]:


data.describe()


# Data Preprocessing _ Data Cleaning _ Missing Value Treatment

# In[17]:


data.isna()


# In[18]:


data.isna().any()


# In[19]:


data.isna().sum()


# Independent and Dependent Variables

# In[20]:


x=data.drop("target", axis=1)
y=data["target"]


# Splitting of DataSet into train and Test¶

# In[21]:


#splitting the data into training and testing data sets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=42)


#  Logistic Regression

# In[22]:


from sklearn.linear_model import LogisticRegression


# In[23]:


log = LogisticRegression()
log.fit(x_train, y_train)


# In[24]:


y_pred1 = log.predict(x_test)


# In[25]:


from sklearn.metrics import accuracy_score 


# In[26]:


accuracy_score (y_test,y_pred1)


# In[27]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


# In[28]:


cm = confusion_matrix(y_test, y_pred1)


# In[29]:


labels = np.unique(y_test)  # Get unique class labels
cm_df = pd.DataFrame(cm, index=labels, columns=labels)


# In[30]:


# Plot confusion matrix using seaborn
plt.figure(figsize=(6, 4))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues', linewidths=1, linecolor='black')

plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()


# In[31]:


import matplotlib.pyplot as plt

# Model names and corresponding accuracies
models = ['LR', 'KNN', 'SVM', 'DT', 'RF']
accuracies = [0.7853658536585366, 0.7317073170731707, 0.6829268292682927, 0.9853658536585366, 0.9853658536585366]

# Define a different color for each bar
colors = ['steelblue', 'darkorange', 'seagreen', 'crimson', 'purple']

# Plotting
plt.figure(figsize=(6, 6))
bars = plt.bar(models, accuracies, color=colors)
plt.ylim(0, 1.05)
plt.ylabel('Accuracy')
plt.title('Model Accuracies Comparison')

# Add accuracy labels above each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.01, f'{height:.3f}', ha='center', va='bottom')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

