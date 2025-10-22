#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exp no.12


# In[1]:


#Aim: Classifier-Random Forest


# In[ ]:


# Name: Mahak Sunil Kamble
# Roll No: 24
# Sec: C
# Subject: ET-1
# Date: 10/10/2025


# In[1]:


import pandas as pd


# In[2]:


import os


# In[3]:


os.getcwd()


# In[4]:


os.chdir('C:\\Users\\mahak\\OneDrive\\Desktop')


# In[5]:


data=pd.read_csv("heart.csv")


# In[6]:


data.head()


# In[7]:


data.tail()


# In[8]:


data.info


# In[9]:


data.shape


# In[10]:


data.size


# In[11]:


data.ndim


# In[12]:


data.describe()


# Data Preprocessing _ Data Cleaning _ Missing Value Treatment

# In[13]:


data.isna()


# In[14]:


data.isna().any()


# In[15]:


data.isna().sum()


# Independent and Dependent Variables

# In[16]:


x=data.drop("target", axis=1)
y=data["target"]


# Splitting of DataSet into train and Test¶

# In[17]:


#splitting the data into training and testing data sets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2 ,random_state=42)


# Random Forest Classifier

# In[41]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score 


# In[42]:


rf=RandomForestClassifier()


# In[43]:


rf.fit(x_train, y_train)


# In[44]:


y_pred5=rf.predict(x_test)


# In[45]:


accuracy_score (y_test,y_pred5)


# In[6]:


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Improved Random Forest (Bagging)
rf = RandomForestClassifier(
    n_estimators=300,      # more trees
    max_depth=None,        # allow deeper trees
    min_samples_split=2,   # allow fine splits
    bootstrap=True,        # ensures bagging
    max_features='sqrt',   # random feature selection
    random_state=42
)
rf.fit(X_train, y_train)
rf_acc = accuracy_score(y_test, rf.predict(X_test))
print("Improved Random Forest (Bagging) Accuracy:", rf_acc)


# In[8]:


from sklearn.ensemble import AdaBoostClassifier

# Wrap Random Forest inside AdaBoost
ada_rf = AdaBoostClassifier(
    base_estimator=rf,     # or estimator=rf if sklearn version >=1.2
    n_estimators=50,
    learning_rate=0.5,
    random_state=42
)
ada_rf.fit(X_train, y_train)
ada_rf_acc = accuracy_score(y_test, ada_rf.predict(X_test))
print("Random Forest with Boosting (AdaBoost) Accuracy:", ada_rf_acc)

