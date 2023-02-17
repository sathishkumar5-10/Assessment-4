#!/usr/bin/env python
# coding: utf-8

# write a program to enter number between 1-12 and print the respective month.

# In[2]:


a=int(input("Enter the a number between 1 to 12 and display the month name"))
if(a==1):
    print("January")
elif(a==2):
    print("February")
elif(a==3):
    print("March")
elif(a==4):
    print("April")
elif(a==5):
    print("May")
elif(a==6):
    print("June")
elif(a==7):
    print("July")
elif(a==8):
    print("August")
elif(a==9):
    print("September")
elif(a==10):
    print("October")
elif(a==11):
    print("November")
elif(a==12):
    print("December")
else:
    print("Invalid")


# write the program to enter a number between 1 to 4

# In[5]:


x=int(input("Enter the a number between 1 to 4 =>1.Add,2.Sub,3.Multi,4.Div"))
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
if(x==1):
    print("Addition is",a+b)
elif(x==2):    
    print("Subtraction is",a-b)
elif(x==3):    
    print("Multiplication is",a*b)
elif(x==4):    
    print("Division is",a/b)
else:
    print("Invalid")


# In[ ]:




