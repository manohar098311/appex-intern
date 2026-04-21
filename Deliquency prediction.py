#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#LOAD DATASET
df = pd.read_csv(r"E:\prep\Delinquency_prediction_dataset.csv")
df.head()


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


df.drop_duplicates()


# In[6]:


#BEFORE REPLACE
df["Employment_Status"].unique()


# In[7]:


#HANDLING MISSING VALUES
df['Employment_Status'] = df['Employment_Status'].replace({
    'employed': 'Employed',
    'EMP': 'Employed',
    'retired': 'Retired'
})
# AFTER REPLACE
print("unique employment status:", df["Employment_Status"].unique())


# In[12]:


df['Income']= df['Income'].fillna(df['Income'].median())
df['Income']


# In[14]:


df['Loan_Balance'] = df['Loan_Balance'].fillna(df['Loan_Balance'].mean())
df['Credit_Score'] = df['Credit_Score'].fillna(df['Credit_Score'].median())
df['Loan_Balance']
df['Credit_Score']


# In[15]:


print("\nMissing values after cleaning:")
print(df.isnull().sum())


# In[16]:


print(df.describe())


# In[17]:


df.dropna(subset=['Credit_Score'], inplace=True)


# In[18]:


# 3. Feature Engineering (Creating New Insights)
# Insight 1: Convert text payment history to a numeric 'Risk Score'
# Map: On-time=0, Late=1, Missed=2

status_map = {'On-time': 0, 'Late': 1, 'Missed': 2}
month_cols = ['Month_1', 'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6']

for col in month_cols:
    # Create new numeric columns like 'Month_1_Num'
    df[col + '_Num'] = df[col].map(status_map)

# Sum these up to get a 'Recent_Risk_Score'

df['Recent_Risk_Score'] = df[[col + '_Num' for col in month_cols]].sum(axis=1)

# Insight 2: High Utilization Flag
# Create a flag for customers using > 80% of their credit

df['High_Utilization'] = (df['Credit_Utilization'] > 0.8).astype(int)

# Check the result

print("New columns added:", df.columns)
df.head()


# In[20]:


# Save the cleaned dataset

df.to_csv('cleaned_delinquency_dataset.csv', index=False)
print("File saved successfully!")


# In[ ]:




