#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# Reading the CSV file
trxn = pd.read_csv('Retail_Data_Transactions.csv')

# Displaying the dataframe
print(trxn)


# In[8]:


response= pd.read_csv('Retail_Data_Response.csv')
response


# In[9]:


df= trxn.merge(response, on='customer_id', how='left')
df


# In[10]:


#features
df.dtypes
df.shape
df.head()


# In[11]:


#features
df.dtypes
df.shape
df.tail()


# In[12]:


df.describe()


# In[13]:


#MISSING VALUES
df.isnull().sum()


# In[14]:


df=df.dropna()
df


# In[ ]:


#change dtypes
df['trans_data']=pd.to_datetime(df['trans_date'])
df['response']=df['response'].astype('int64')


# In[16]:


df


# In[17]:


set(df['response'])


# In[18]:


df.dtypes


# In[19]:


#check for outliers
#Z-SCORE
from scipy import stats
import numpy as np

# Assuming df is your DataFrame and 'tran_amount' is the column you want to check for outliers

# Calculate Z-scores
z_scores = np.abs(stats.zscore(df['tran_amount']))

# Set a threshold
threshold = 3

# Identify outliers
outliers = z_scores > threshold

# Print the outliers
print(df[outliers])


# In[20]:


#check for outliers
#Z-SCORE
from scipy import stats
import numpy as np

# Assuming df is your DataFrame and 'tran_amount' is the column you want to check for outliers

# Calculate Z-scores
z_scores = np.abs(stats.zscore(df['response']))

# Set a threshold
threshold = 3

# Identify outliers
outliers = z_scores > threshold

# Print the outliers
print(df[outliers])


# In[21]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=df['tran_amount'])
plt.show()


# In[ ]:


#creating new columns
df['month']= df['trans_date'].dt.month


# In[23]:


df


# In[24]:


# Which 3 months have had the highest transaction amounts?

monthly_sales = df.groupby('month')['tran_amount'].sum()
monthly_sales = monthly_sales.sort_values(ascending=False).reset_index()
# Display the top 3 months with the highest transaction amounts
top_3_months = monthly_sales.head(3)
print(top_3_months)



# In[25]:


# Customers having highest number of orders

customer_counts = df['customer_id'].value_counts().reset_index()
customer_counts.columns = ['customer_id', 'order_count']

print(customer_counts)

# Sort and get top 5 customers with the highest number of orders

top_5_cus = customer_counts.sort_values(by='order_count', ascending=False).head(5)
print(top_5_cus)


# In[26]:


sns.barplot(x='customer_id', y='order_count', data=top_5_cus)


# In[27]:


# Customers having highest value of orders

customer_sales= df.groupby('customer_id')['tran_amount'].sum().reset_index()
customer_sales


# Sort 

top_5_sal = customer_sales.sort_values(by='tran_amount', ascending=False).head(5)
print(top_5_sal)


# # ADVANCED ANALYTICS 

# # TIME SERIES ANALYSIS
# 

# In[29]:


import matplotlib.dates as mdates
df['month_year']= df['trans_date'].dt.to_period('M')
monthly_sales = df.groupby('month_year')['tran_amount'].sum()
monthly_sales.index= monthly_sales.index.to_timestamp()

plt.figure(figsize=(12,6))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.xlabel ('Month-Year')
plt.ylabel ('Sales')
plt.title ('Monthly Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[30]:


df


# # Cohort Segmentation

# In[35]:


import pandas as pd

# Recency: Time since the last transaction
recency = df.groupby('customer_id')['trans_date'].max()

# Frequency: Total number of transactions
frequency = df.groupby('customer_id')['trans_date'].count()

# Monetary: Total transaction amount
monetory = df.groupby('customer_id')['tran_amount'].sum()

# Combine into RFM DataFrame
rfm = pd.DataFrame({'recency': recency, 'frequency': frequency, 'monetory': monetory})

# Display the rfm DataFrame
print(rfm)



# In[36]:


#customer segmentation 
def segment_customer(row):
    if row['recency'].year>=2012 and row['frequency']>=15 and row['monetory']>1000:
        return 'p0'
    elif (2011<=row['recency'].year<2012) and (10<row['frequency']<15) and (500<=row['monetory']<=1000):
        return'P1'
    else:
        return'P2'
rfm['Segment']= rfm.apply(segment_customer, axis=1)
rfm


# # Churn Analysis

# In[38]:


#count the numbers of churned and active customers
churn_counts= df['response'].value_counts()
#Plot
churn_counts.plot(kind='bar')


# # Analysing Top Customers
# 

# In[39]:


top_5_cus= monetory.sort_values(ascending=False).head(5).index

top_customers_df= df[df['customer_id'].isin(top_5_cus)]

top_customer_sales= top_customers_df.groupby(['customer_id','month_year'])['tran_amount'].sum().unstack(level=0)
top_customer_sales.plot(kind='line')


# In[40]:


df.to_csv('MainData.csv')


# In[41]:


rfm.to_csv('AddAnlys.csv')

