#!/usr/bin/env python
# coding: utf-8

# In[36]:


import calendar  
from datetime import date,timedelta


# In[37]:


today=date.today()
name=str(input("Enter your name:"))
year = int(input('Enter a year:'))
month = int(input('Enter a month:'))
day = int(input('Enter a date:'))
dob = date(year, month, day)
birthday = date(dob.year, dob.month, dob.day)
day_name=date(int(today.year), int(dob.month), int(dob.day))
ps = 'You were born on {0}\nThis year your birthday is on: {1}'.format(birthday.strftime("%A"), day_name.strftime("%A"))
print(ps)


# In[38]:


no_of_days_spent_on_this_world=(today-dob).days
print(no_of_days_spent_on_this_world)


# In[29]:



remainingdays = (birthday-today)


# In[39]:


f_date =date(int(today.year), int(today.month), int(today.day)) #2020-04-19
l_date = date(2021,int(dob.month), int(dob.day))            #2021-01-01
print(f_date)
print(l_date)
countdown = (l_date - f_date)
print(countdown.days)


# In[34]:


print(remainingdays)


# In[ ]:


age=date(today.year,today.month,today.day)-date(year,month,day)


# In[ ]:


print(age)


# In[ ]:


years=age/365


# In[ ]:


print(today.year)
print(year)
print(today.month)
print(today.day)
print(month)


# In[40]:


def calculate_age(born):
    today = date.today()
    return today.year - year - ((today.month, today.day) < (month, day))

age = calculate_age(dob)
print(age)


# In[ ]:





# In[ ]:




