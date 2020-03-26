#!/usr/bin/env python
# coding: utf-8

# In[1]:


students=['sri', 'mujeeb', 'arun', 'poonam', 'abhishek', 'ram']


# In[2]:


print(students)


# In[3]:


#req:to count how many elements are there in our list


# In[4]:


len(students)


# In[5]:


#req: appreciate the studentsfor completing the practise regularly
#Terminology for understanding the fro loop
#main variable------>students
#temp variable------>student--->abc


# In[7]:


print (students)


# In[12]:


for abc in students:
 print(abc)


# In[13]:


#Enhancement  of the for loop with actual req: 


# In[19]:


for abc in students:
    print(f"{abc}, keep up the good work !")


# In[21]:


for ice in students:
    print(f"{ice}, keep up the good work")


# In[22]:


# making numerical list by using for loop
#builtin method:range()#start value & stop value


# In[25]:


for value in range(1, 15):# last value is always exclusive
    print (value)


# In[31]:


for value in range(4, 100, 10):
  print(value)


# In[51]:


numbers=list(range(1,8))
print(numbers)


# In[ ]:


#Req: i want to print only even num from 1-50


# In[53]:


even_numbers=list(range(2, 50,2))

print(even_numbers)


# In[54]:


odd_numbers=list(range(1, 50,2))

print(odd_numbers)


# In[55]:


min(odd_numbers)


# In[56]:


max(odd_numbers)


# In[57]:


sum(odd_numbers)


# In[58]:


#Slicing of list


# In[59]:


my_students=['anu', 'veena', 'divya', 'utsav', 'majeeb', 'sharuk', 'vikram', 'chandana']


# In[60]:


print(my_students)


# In[61]:


type(my_students)


# In[62]:


#Slicing

print(my_students[0:2])


# In[63]:


print(my_students[2:4])


# In[ ]:




