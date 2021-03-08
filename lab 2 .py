#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Check whether a number is even or odd


# In[12]:


a = int(input("Enter the number")) 

if a % 2 == 0:
   print(a , "is even")
else:
   print(a, "is odd")


# In[ ]:


Check whether an entered year is leap year or not.


# In[16]:


year = int(input("Enter the yaer: "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year")
        else: 
            print("It is not a leap year")
    else: 
            print("It is not a leap year")
else: 
            print("It is not a leap year")    


# In[ ]:


3. Write a program to check whether a character is vowel or consonants.


# In[17]:


ch = input("Enter a character: ")

if(ch=='A',"E",'I','O','U') :
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


# In[ ]:


4.Write a program to find the smallest of two numbers.


# In[18]:


a = int(input("Enter the number: ")) 
b = int(input("Enter the number: "))
if a > b:
    print("a is greater ")
else:
    print("b is greater")


# In[ ]:


Find the Factorial of a Number


# In[19]:


num = 7

num = int(input("Enter a number: "))

factorial = 1


if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[ ]:


6. Write a program to print this patterns
         *
     *     *
  *    *     *
         *   *     *     *  


# In[23]:


print("     *     ")
print("   *   *   ")
print("  *  *  *  ")
print(" *  *  *  *")


# In[25]:


num1 = int(input("Enter the lower no")) 
num2 = int(input("Enter the higher no")) 

print("Prime numbers between", num1, "and", num2, "are:")

for num in range(num1, num2 + 1):
  
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:


7.Write a program to print this series
             1 1 2 3 5 8 13 


# In[32]:


x=0
y=1

while y<20:
    print(y)
    x,y = y,x+y


# In[ ]:


8.Check whether a number is prime or not


# In[36]:


num = int(input("Enter the number "))
 

if num > 1:
 
    
    for i in range(2, int(num/2)+1):
 
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
 
else:
    print(num, "is not a prime number")


# In[ ]:


Make a Simple Calculator.


# In[1]:


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input(str("Enter the opertor(A,S,M,D): "))
        
if operator == 'A':
    print(num1, "+", num2, "=", (num1 + num2))

elif operator == 'S':
    print(num1, "-", num2, "=", (num1 - num2))

elif operator == 'M':
    print(num1, "*", num2, "=", (num1 * num2))

elif operator == 'D':
    print(num1, "/", num2, "=", (num1 / num2))
  
else:
    print("Invalid Input")

