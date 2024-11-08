#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[1]:


import numpy as np
import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv("Diwali Sales Data.csv", encoding = 'unicode_escape')


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


#removing out null column unnamed1 and status
df.drop(['Status', 'unnamed1'], axis = 1 , inplace = True)


# In[10]:


df.info()


# In[11]:


pd.isnull(df)


# In[16]:


pd.isnull(df).sum


# In[18]:


pd.isnull(df['Amount']).sum


# In[20]:


df.shape


# In[21]:


df.dropna(inplace = True)


# In[22]:


df.shape


# In[25]:


#changing from float to integer
df['Amount'] = df['Amount'].astype('int')


# In[29]:


df['Amount'].dtype


# In[31]:


df.info()


# In[32]:


df.describe()


# In[36]:


ax = sns.countplot(x= 'Gender', data =df)


# In[40]:


ax = sns.countplot(x= 'Gender', data =df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[46]:


df.groupby(['Gender'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[ ]:


#this implies that spending by females and purchasing power are more than male


# In[47]:


df_data = df.groupby(['Gender'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.barplot(x = 'Gender', y = 'Amount', data = df_data)


# In[54]:


#this is to find out which age group has purchased the most
sns.countplot( x = 'Age Group', data = df)


# In[55]:


#this is to show which age group of which gender has purchased more
sns.countplot( x = 'Age Group', hue = 'Gender', data = df)


# In[59]:


#for visualization with exact count number
ax = sns.countplot( x = 'Age Group', hue = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[60]:


#to know which age group has spent what amount
df.groupby(['Age Group'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[62]:


df_group = df.groupby(['Age Group'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[63]:


sns.barplot(x = 'Age Group', y = 'Amount', data = df_group)


# In[64]:


#from above graphs we can conclude that the highest amount is spent by age group of 26-35 that too females


# In[66]:


df.groupby(['State'], as_index= False)['Orders'].sum().sort_values(by = 'Orders', ascending = False)


# In[79]:


df_orders = df.groupby(['State'], as_index= False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)


# In[80]:


#sns.set(rc={'figure.figsize': (15,5)}) this step is optional


# In[81]:


sns.barplot(x = 'State', y = 'Orders', data = df_orders)


# In[73]:


#from above graph we can see that most of the orders are from UP following MH and KA


# In[82]:


df.groupby(['State'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)


# In[83]:


df_state = df.groupby(['State'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False).head(10)


# In[84]:


sns.barplot(x = 'State', y = 'Amount', data = df_state)


# In[86]:


#purchasing power and amount is also from UP and we can also notice that number of orders for haryana were less but the amount or purchasing power of haryana is greater than kerala


# In[88]:


ax = sns.countplot(data = df, x = 'Marital_Status')


# In[95]:


sns.set(rc= {'figure.figsize': (5,5)})


# In[96]:


for bars in ax.containers:
    ax.bar_label(bars)


# In[97]:


ax = sns.countplot(data = df, x = 'Marital_Status')


# In[ ]:


#here we can conclude that most of the orders were done my married people


# In[98]:


df.groupby(['Marital_Status', 'Gender'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[99]:


df_marriage = df.groupby(['Marital_Status', 'Gender'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[100]:


sns.barplot(data = df_marriage, x = 'Marital_Status', y = 'Amount', hue = 'Gender')


# In[101]:


#from here we can see that females have spent more amount tham male in both the cases


# In[ ]:





# In[119]:


sns.countplot(x = 'Occupation', data = df)
sns.set(rc= {'figure.figsize': (26,8)})
for bars in ax.containers:
 ax.bar_label(bars)


# In[120]:


#here we can see that people from it sector has purchased the most


# In[121]:


df.groupby(['Occupation'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[123]:


df_occ = df.groupby(['Occupation'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)
sns.barplot(x = 'Occupation', y = 'Amount', data = df_occ)


# In[124]:


#here we can see thatpeople from it sector has spent the max amount


# In[125]:


sns.countplot(x = 'Product_Category', data = df)


# In[126]:


df_pro = df.groupby(['Product_Category'], as_index= False)['Amount'].sum().sort_values(by = 'Amount', ascending = False)


# In[129]:


sns.barplot(x = 'Product_Category',y = 'Amount', data = df_pro)


# In[130]:


#here we can conclude that the amount spent on food is highest


# In[138]:


df_id = df.groupby(['Product_ID'], as_index= False)['Orders'].sum().sort_values(by = 'Orders', ascending = False).head(10)


# In[139]:


sns.barplot(x= 'Product_ID', y = 'Orders', data = df_id)


# In[146]:


fig1 , ax1 = plt.subplots(figsize = (8,4))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending = False).plot(kind = 'bar')


# In[147]:


#here we get to know that which product has received most number of orders


# In[ ]:




