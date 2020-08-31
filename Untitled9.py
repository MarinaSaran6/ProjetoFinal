#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd


# In[27]:


import matplotlib.pyplot as plt


# In[28]:


import seaborn as sns


# In[29]:


import numpy as np


# In[30]:


df = pd.read_excel("Eleições 2018 - Copia.xlsx")


# In[ ]:





# In[31]:


df


# In[32]:


df.head


# In[33]:


df.dtypes


# In[34]:


df.shape


# In[35]:


df.info()


# In[36]:


df.describe().T


# In[37]:


df['Taxa de analfabetismo da população de 18 anos ou mais'] = df['Taxa de analfabetismo da população de 18 anos ou mais'].str.replace(',', '').astype(float) #retirando a vírgula


# In[38]:


df['Taxa de analfabetismo da população de 18 anos ou mais '] = df['Taxa de analfabetismo da população de 18 anos ou mais '].str.rstrip('%').astype(float)/100 #retirando o sinal de porcentagem


# In[39]:


df['IDH - 2010']


# In[40]:


df['Cidade']


# In[41]:


fig, ax = plt.subplots(figsize=(30, 5))
sns.barplot(x='Cidade', y='IDH - 2010',data=df,
          palette='Reds_r')


# In[ ]:




