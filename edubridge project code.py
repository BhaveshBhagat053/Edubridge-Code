#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries 

# In[4]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')


# # Loading Dataset

# In[10]:


df = pd.read_csv('hotel_bookings.csv')


# # Exploratory Data Analysis And Data Cleaning

# In[11]:


df.head()


# In[12]:


df.tail()


# In[13]:


df.shape


# In[15]:


df.columns


# In[16]:


df.info()


# In[17]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[18]:


df.info()


# In[19]:


df.describe(include = 'object')


# In[22]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[23]:


df.isnull().sum()


# In[25]:


df.drop(['company','agent'], axis = 1, inplace = True)
df.dropna(inplace = True)


# In[26]:


df.isnull().sum()


# In[27]:


df.describe()


# In[28]:


df['adr'].plot(kind = 'box')


# In[30]:


df = df[df['adr']<5000]


# In[31]:


df.describe()


# # Data Analysis and Visualisaton

# In[33]:


cancelled_perc = df['is_canceled'].value_counts(normalize = True)
cancelled_perc


# In[39]:


plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor = 'r', width = 0.7)
plt.show()


# In[62]:


plt.figure(figsize = (8,4))
ax1= sns.countplot(x= 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[63]:


resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[64]:


city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel ['is_canceled'].value_counts(normalize = True)


# In[65]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[66]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index, city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[67]:


df['month'] = df['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month', hue = 'is_canceled',data = df, palette = 'bright')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[70]:


plt.figure(figsize = (15,8))
plt.title('ADR per month', fontsize = 30)
sns.barplot('month','adr', data = df[df['is_canceled'] ==1].groupby('month')[['adr']].sum().reset_index())
plt.show()


# In[71]:


cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct = '%.2f' , labels = top_10_country.index)
plt.show()


# In[72]:


df['market_segment'].value_counts()


# In[73]:


df['market_segment'].value_counts(normalize = True)


# In[74]:


cancelled_data['market_segment'].value_counts(normalize = True)


# In[77]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot (not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()


# In[79]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') & (cancelled_df_adr['reservation_status_date']<'2017-09')]
not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') & (not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[81]:


plt.figure(figsize =(20,6))
plt.title('Average Daily Rate', fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend(fontsize = 20)


# In[ ]:




