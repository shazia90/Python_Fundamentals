#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Introduction to list data type


# In[3]:


# A list is a collection of items in a particular order
#  A list is a mutable data type, we can able to change/modify and alter the data once it gets assigned


# In[5]:


students=['sharuk', 'veena', 'vivek', 'anu', 'poornima', 'chetan', 'utsav']


# In[6]:


print(students)


# In[7]:


type(students)


# In[8]:


# Itroduction to indexing


# In[9]:


# where exactly the indexing will be starting from -------0,1,2,3----


# In[10]:


#How to access the elements in a list


# In[12]:


#Req: I want to access viveks name int he output


# In[13]:


print(students[2])


# In[14]:


print(students[5])


# In[16]:


#Req: Access the utsav name in the output

print(students[6])


# In[17]:


#Introduction to negative indexing 


# In[18]:


print (students)


# In[21]:


#From where the negative indexing wiil be starting from?-1,-2,-3-----------


# In[22]:


#Req: to achieve the -ve indexing we have to print Utsav again


# In[24]:


print (students[-1]) #-ve indexing


# In[25]:


print (students[-3])


# In[26]:


#Enhancement of code


# In[28]:


print(students[-3].title())


# In[29]:


print(students[-3].upper())


# In[30]:


print(students[-3].lower())


# In[31]:


#Changing, adding and removing elements in a list:


# In[32]:


#Changing /modifying the elements from the list

#Req:want to change Vivek to mohit


# In[33]:


students[2]='mohit'


# In[34]:


print (students)


# In[35]:


#req: Adding elements to the list


# In[36]:


#new students need to add to the list

students.append('Praneeta')


# In[37]:


print(students)


# In[38]:


#req:madhuri to 3 indexing position


# In[39]:


students.insert(3, 'madhuri')


# In[40]:


print(students)


# In[ ]:




