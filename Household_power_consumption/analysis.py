#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('household_power_consumption.txt', sep=';', na_values='?')
df.head()
df.info()
df.describe()


# In[2]:


#Handling the missing values and coversion of datatype
df.dropna(inplace=True)
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'],format='%d/%m/%Y %H:%M:%S')
df.set_index('DateTime', inplace=True)
df['Global_active_power'] = pd.to_numeric(df['Global_active_power'])


# In[3]:


#Total and average energy consumed
total_consumption=df['Global_active_power'].sum()
average_consumption=df['Global_active_power'].mean()
print(f'Total={total_consumption},Average={average_consumption}')


# In[5]:


#Maximum and minimum energy consumption
maximum_consumption=df['Global_active_power'].max()
minimum_consumption=df['Global_active_power'].min()
print(f"Maximum={maximum_consumption},Minimum={minimum_consumption}")


# In[7]:


#Daily,weekly,monthly energy consumption patterns
daily_consumption=df['Global_active_power'].resample('D').sum()
weekly_consumption=df['Global_active_power'].resample('W').sum()
monthly_consumption=df['Global_active_power'].resample('M').sum()


# In[8]:


#Daily consumption visual
import matplotlib.pyplot as plt

daily_consumption.plot(figsize=(15,5), title="Daily Energy Consumption")
plt.ylabel("kW")
plt.show()


# In[9]:


#Peak hours visual
df['hour'] = df.index.hour
hourly_avg = df.groupby('hour')['Global_active_power'].mean()
hourly_avg.plot(kind='bar', title="Average Hourly Energy Consumption")
plt.ylabel("kW")
plt.show()


# In[11]:


#Which day of the week has the highest average consumption?
df['dayofweek'] = df.index.dayofweek  
weekday_avg = df.groupby('dayofweek')['Global_active_power'].mean()
weekday_avg.plot(kind='bar', title="Average Consumption by Day of Week")
plt.ylabel("kW")
plt.show()


# In[12]:


#Is there a correlation between voltage and power consumption?
correlation = df['Global_active_power'].corr(df['Voltage'])
print(f"Correlation: {correlation}")


# In[13]:


#Unusually high consumption periods
high_usage = df[df['Global_active_power'] > df['Global_active_power'].quantile(0.99)]
print(high_usage)


# In[14]:


#new measure i.e is_weekend
df['is_weekend'] = df['dayofweek'] >= 5


# In[15]:


#Saving the cleaned and processed data 
df.to_csv('cleaned_energy_consumption.csv')


# In[ ]:




