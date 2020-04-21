#!/usr/bin/env python
# coding: utf-8
#Authors:Anirudha S Gudi,Aniketh Deshpande


import calendar
#Calendar module allows output calendars like the program and provides additional useful functions related to the calendar.
from datetime import date,timedelta
#The datetime module supplies classes for manipulating dates and times in both simple and complex ways.
#Timedelta object represents a duration, the difference between two dates or times.

#PROGRAM
print("BIRTHDAY INFO")

print("Enter the user details")
name=str(input("Enter your name:"))
year = int(input('Enter a year:'))
month = int(input('Enter a month:'))
day = int(input('Enter a date:'))
today=date.today()
dob = date(year, month, day)
birthday = date(dob.year, dob.month, dob.day)
day_name=date(int(today.year), int(dob.month), int(dob.day))
ps = 'You were born on {0}\nThis year your birthday is on: {1}'.format(birthday.strftime("%A"), day_name.strftime("%A"))
print(ps)


no_of_days_spent_on_this_world=(today-dob).days
print(no_of_days_spent_on_this_world)


remainingdays = (birthday-today)




f_date =date(int(today.year), int(today.month), int(today.day)) #2020-04-19
l_date = date(2021,int(dob.month), int(dob.day))                #2021-01-01
print(f_date)
print(l_date)
countdown = (l_date - f_date)
print(countdown.days)


# In[34]:


print(remainingdays)



print(today.year)
print(year)
print(today.month)
print(today.day)
print(month)



#Age function
def calculate_age(born):
    today = date.today()
    return today.year - year - ((today.month, today.day) < (month, day))

age = calculate_age(dob)
print(age)

