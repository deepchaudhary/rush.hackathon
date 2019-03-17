
# coding: utf-8

# In[1]:

import graphlab


# In[2]:

sales=graphlab.SFrame.read_csv("FnB_hackathon_Pi")


# In[3]:

sales


# In[4]:

sales.show()


# In[5]:

graphlab.canvas.set_target("ipynb")


# In[6]:

sales.show(view="Summary")


# In[7]:

men_data=sales[sales['Company']=='men']


# In[8]:

white_walkers_data=sales[sales['Company']=='white walkers']


# In[9]:

men_data


# # Month Vs Revenue for men

# In[10]:

men_data.show(view="Bar Chart", x="MONTH", y="Revenue")


# # Month Vs Revenue for white walkers

# In[11]:

white_walkers_data.show(view="Bar Chart", x="MONTH", y="Revenue")


# In[12]:

white_walkers_data


# In[13]:

men_data_products=[men_data['Product'].unique()]


# In[14]:

men_data_products


# In[15]:

white_walkers_data_products=[white_walkers_data['Product'].unique()]


# In[16]:

white_walkers_data_products


# In[17]:

common_products=[x for x in men_data_products[0] if x in white_walkers_data_products[0]]


# In[18]:

common_products


# In[19]:

men_data_product_category_2=[men_data['Product Category 2'].unique()]


# In[20]:

men_data_product_category_2


# In[21]:

white_walkers_data_product_category_2=[white_walkers_data['Product Category 2'].unique()]


# In[22]:

white_walkers_data_product_category_2


# In[23]:

common_product_category_2=[x for x in men_data_product_category_2[0] if x in white_walkers_data_product_category_2[0]]


# In[24]:

common_product_category_2


# In[25]:

men_data_product_category_1=[men_data['Product Category 1'].unique()]


# In[26]:

men_data_product_category_1


# In[27]:

white_walkers_data_product_category_1=[white_walkers_data['Product Category 1'].unique()]


# In[28]:

white_walkers_data_product_category_1


# In[29]:

common_product_category_1=[x for x in men_data_product_category_1[0] if x in white_walkers_data_product_category_1[0]]


# In[30]:

common_product_category_1


# In[31]:

revenue_sum=[]


# In[32]:

men_vietnamese_data=men_data[men_data['Product Category 1']=='vietnamese']


# In[33]:

men_vietnamese_data_revenue_sum=men_vietnamese_data['Revenue'].sum()


# In[34]:

men_vietnamese_data_revenue_sum


# In[35]:

white_walkers_vietnamese_data=white_walkers_data[white_walkers_data['Product Category 1']=='vietnamese']


# In[36]:

white_walkers_vietnamese_data_revenue_sum=white_walkers_vietnamese_data['Revenue'].sum()


# In[37]:

white_walkers_vietnamese_data_revenue_sum


# In[38]:

men_vietnamese_market_share=men_vietnamese_data_revenue_sum/(men_vietnamese_data_revenue_sum+white_walkers_vietnamese_data_revenue_sum)


# In[39]:

men_vietnamese_market_share


# In[40]:

men_indian_data=men_data[men_data['Product Category 1']=='indian']


# In[41]:

men_indian_data_revenue_sum=men_indian_data['Revenue'].sum()


# In[42]:

men_indian_data_revenue_sum


# In[43]:

white_walkers_indian_data=white_walkers_data[white_walkers_data['Product Category 1']=='indian']


# In[44]:

white_walkers_indian_data_revenue_sum=white_walkers_indian_data['Revenue'].sum()


# In[45]:

white_walkers_indian_data_revenue_sum


# In[46]:

men_indian_market_share=men_indian_data_revenue_sum/(men_indian_data_revenue_sum+white_walkers_indian_data_revenue_sum)


# In[47]:

men_indian_market_share


# In[48]:

men_chinese_data=men_data[men_data['Product Category 1']=='chinese']


# In[49]:

men_chinese_data_revenue_sum=men_chinese_data['Revenue'].sum()


# In[50]:

men_chinese_data_revenue_sum


# In[51]:

white_walkers_chinese_data=white_walkers_data[white_walkers_data['Product Category 1']=='chinese']


# In[52]:

white_walkers_chinese_data_revenue_sum=white_walkers_chinese_data['Revenue'].sum()


# In[53]:

white_walkers_chinese_data_revenue_sum


# In[54]:

men_chinese_market_share=men_chinese_data_revenue_sum/(men_chinese_data_revenue_sum+white_walkers_chinese_data_revenue_sum)


# In[55]:

men_chinese_market_share


# In[56]:

men_greek_data=men_data[men_data['Product Category 1']=='greek']


# In[57]:

men_greek_data_revenue_sum=men_greek_data['Revenue'].sum()


# In[58]:

men_greek_data_revenue_sum


# In[59]:

white_walkers_greek_data=white_walkers_data[white_walkers_data['Product Category 1']=='greek']


# In[60]:

white_walkers_greek_data_revenue_sum=white_walkers_greek_data['Revenue'].sum()


# In[61]:

white_walkers_greek_data_revenue_sum


# In[62]:

men_greek_market_share=men_greek_data_revenue_sum/(men_greek_data_revenue_sum+white_walkers_greek_data_revenue_sum)


# In[63]:

men_greek_market_share


# In[64]:

men_korean_data=men_data[men_data['Product Category 1']=='korean']


# In[65]:

men_korean_data_revenue_sum=men_korean_data['Revenue'].sum()


# In[66]:

men_korean_data_revenue_sum


# In[67]:

white_walkers_korean_data=white_walkers_data[white_walkers_data['Product Category 1']=='korean']


# In[68]:

white_walkers_korean_data_revenue_sum=white_walkers_korean_data['Revenue'].sum()


# In[69]:

white_walkers_korean_data_revenue_sum


# In[70]:

men_korean_market_share=men_korean_data_revenue_sum/(men_korean_data_revenue_sum+white_walkers_korean_data_revenue_sum)


# In[71]:

men_korean_market_share


# In[72]:

men_mexican_data=men_data[men_data['Product Category 1']=='mexican']


# In[73]:

men_mexican_data_revenue_sum=men_mexican_data['Revenue'].sum()


# In[74]:

men_mexican_data_revenue_sum


# In[75]:

white_walkers_mexican_data=white_walkers_data[white_walkers_data['Product Category 1']=='mexican']


# In[76]:

white_walkers_mexican_data_revenue_sum=white_walkers_mexican_data['Revenue'].sum()


# In[77]:

white_walkers_mexican_data_revenue_sum


# In[78]:

men_mexican_market_share=men_mexican_data_revenue_sum/(men_mexican_data_revenue_sum+white_walkers_mexican_data_revenue_sum)


# In[79]:

men_mexican_market_share


# In[80]:

def transform(x):
    if x['Product Category 1']=='vietnamese':
        return men_vietnamese_market_share
    elif x['Product Category 1']=='indian':
        return men_indian_market_share
    elif x['Product Category 1']=='chinese':
        return men_chinese_market_share
    elif x['Product Category 1']=='greek':
        return men_greek_market_share
    elif x['Product Category 1']=='korean':
        return men_korean_market_share
    else:
        return men_mexican_market_share


# In[81]:

men_data.apply(transform)


# In[82]:

men_data['men_market_share']=men_data.apply(transform)


# In[83]:

men_data


# In[84]:

def transform1(row):
    return (1-row['men_market_share'])


# In[85]:

men_data['white_walkers_market_share']=men_data.apply(transform1)


# In[86]:

men_data


# In[87]:

men_data.show(view="Line Chart", x="men_market_share", y="white_walkers_market_share")


# In[111]:

men_data.show(view="Line Chart", x="Units sold", y="Revenue")


# In[112]:

men_data.show(view="Line Chart", x="Commission", y="Revenue")


# In[114]:

men_data.show(view="Scatter Plot", x="Revenue", y="men_market_share")


# In[88]:

all_features=['MONTH','Company','Area 1','Area 2','Area 3','Area 3 Classification','Outlet Type','Outlet Name'
              ,'Product Category 1','Product Category 2','Product','Commission']


# In[89]:

train_data,test_data=men_data.random_split(0.8,seed=0)


# In[90]:

revenue_model=graphlab.linear_regression.create(train_data,target='Revenue',features=all_features)


# In[91]:

print revenue_model.evaluate(test_data)


# In[92]:

revenue_model.show()


# In[93]:

test1=test_data[1]


# In[94]:

test1


# In[95]:

revenue_model.predict(test1)


# In[96]:

test1['Revenue']


# In[97]:

test2={'Area 1': 'the crownlands',
 'Area 2': 'stony shore',
 'Area 3': 'dothraki',
 'Area 3 Classification': 'hand of the king',
 'Commission': 2009.9266261751936,
 'Company': 'men',
 'MONTH': 'DEC',
 'Outlet Name': 'viserys ii targaryen',
 'Outlet Type': 'house wylde',
 'Product': 'nonfat ricotta cheese',
 'Product Category 1': 'chinese',
 'Product Category 2': 'fino sherry',
 'Revenue': 120595.5975705116,
 'Units sold': 10.049633130875968,
 'YEAR': 2018L,
 'market_share': 0.6016338870867236}


# In[98]:

revenue_model.predict(test2)


# In[99]:

units_sold_model=graphlab.linear_regression.create(train_data,target='Units sold',features=all_features)


# In[100]:

print units_sold_model.evaluate(test_data)


# In[101]:

print units_sold_model.show()


# In[102]:

units_sold_model.predict(test1)


# In[103]:

test1['Units sold']


# In[104]:

units_sold_model.predict(test2)


# In[105]:

market_share_model=graphlab.linear_regression.create(train_data,target='men_market_share',features=all_features)


# In[106]:

print market_share_model.evaluate(test_data)


# In[107]:

market_share_model.show()


# In[108]:

market_share_model.predict(test1)


# In[109]:

test1['men_market_share']


# In[110]:

market_share_model.predict(test2)


# In[ ]:



