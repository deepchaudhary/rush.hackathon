
# coding: utf-8

# In[1]:

import graphlab


# In[2]:

sales=graphlab.SFrame.read_csv("FnB_hackathon_Pi")


# In[3]:

sales


# In[4]:

graphlab.canvas


# In[5]:

man_data=sales[sales['Company']=='men']


# In[6]:

man_data


# In[7]:

white_walkers_data=sales[sales['Company']=='white walkers']


# In[8]:

white_walkers_data


# In[9]:

man_data.show()


# In[10]:

train_data,test_data=man_data.random_split(0.8,seed=0)


# In[11]:

all_features=['MONTH','Company','Area 1','Area 2','Area 3','Area 3 Classification','Outlet Type','Outlet Name'
              ,'Product Category 1','Product Category 2','Product','Commission']


# In[12]:

all_feature_model=graphlab.linear_regression.create(train_data,target='Revenue',features=all_features)


# In[13]:

print all_feature_model.evaluate(test_data)


# In[14]:

test1=test_data[1]


# In[15]:

all_feature_model.predict(test1)


# In[16]:

test1['Revenue']


# In[17]:

all_feature_model.show()


# In[18]:

white_walkers_products=[white_walkers_data['Product'].unique()]


# In[19]:

white_walkers_products


# In[20]:

men_data_products=[man_data['Product'].unique()]


# In[21]:

men_data_products


# In[24]:

test1


# In[25]:


Out[24]:
{'Area 1': 'beyond the wall',
 'Area 2': 'stony shore',
 'Area 3': 'dothraki',
 'Area 3 Classification': 'hand of the king',
 'Commission': 2009.9266261751936,
 'Company': 'men',
 'MONTH': 'JAN',
 'Outlet Name': 'viserys ii targaryen',
 'Outlet Type': 'house wylde',
 'Product': 'nonfat ricotta cheese',
 'Product Category 1': 'indian',
 'Product Category 2': 'fino sherry',
 'Revenue': 120595.5975705116,
 'Units sold': 10.049633130875968,
 'YEAR': 2018L}


# In[26]:

testrandom1={'Area 1': 'beyond the wall',
 'Area 2': 'stony shore',
 'Area 3': 'dothraki',
 'Area 3 Classification': 'hand of the king',
 'Commission': 2009.9266261751936,
 'Company': 'men',
 'MONTH': 'JAN',
 'Outlet Name': 'viserys ii targaryen',
 'Outlet Type': 'house wylde',
 'Product': 'nonfat ricotta cheese',
 'Product Category 1': 'indian',
 'Product Category 2': 'fino sherry',
 'Revenue': 120595.5975705116,
 'Units sold': 10.049633130875968,
 'YEAR': 2018L}


# In[27]:

all_feature_model.predict(testrandom1)


# In[ ]:



