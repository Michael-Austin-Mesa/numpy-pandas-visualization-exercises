#!/usr/bin/env python
# coding: utf-8

# In[72]:


import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# ### Q1

# In[73]:


count = 0
for i in range(len(a)):
    if a[i] < 0:
        count += 1
print(f'{count} negative numbers')


# In[74]:


len(a[a<0])


# ### Q2

# In[75]:


count = 0
for i in range(len(a)):
    if a[i] > 0:
        count += 1
print(f'{count} positive numbers')


# In[76]:


len(a[a>0])


# ### Q3

# In[77]:


count = 0
for i in range(len(a)):
    if a[i] > 0 and a[i]%2 == 0:
        count += 1
print(f'{count} positive even numbers')


# In[78]:


posnums = a[a>0]
len(posnums[posnums % 2 ==0])


# ### Q4

# In[79]:


count = 0
for i in range(len(a)):
    if (a[i]+3) > 0:
        count += 1
print(f'{count} positive numbers')


# In[80]:


posnums = a+3
posnums = posnums[posnums>0]
len(posnums)


# ### Q5

# In[81]:


print(np.mean(a**2))
print(np.std(a**2))


# ### Q6

# In[82]:


print(f'Pre-centered mean: {np.mean(a)}')
print((a - np.mean(a)))
print(f'Centered mean: {np.mean(a - np.mean(a))}')


# ### Q7

# In[83]:


zscore = (a - np.mean(a))/np.std(a)
print(zscore)


# ### Q8

# In[98]:


import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a)/len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for i in range(len(a)):
    product_of_a *= a[i]
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = []
for i in range(len(a)):
    squares_of_a.append(a[i] ** 2)
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = []
for i in range(len(a)):
    if a[i]%2 == 1:
        odds_in_a.append(a[i])

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = []
for i in range(len(a)):
    if a[i]%2 == 0:
        evens_in_a.append(a[i])
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

b = np.array(b)
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)
print(np.sum(b,0))
# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
print(np.minimum(b[0],b[1]))
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
print(np.maximum(b[0],b[1]))

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
print(np.mean(b))
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
#for row in b:
#    for number in row:
#        product_of_b *= number
print(np.prod(b))
# Exercise 6 - refactor the following to use numpy to find the list of squares 
#squares_of_b = []
#for row in b:
#    for number in row:
#        squares_of_b.append(number**2)
print(np.square(b))
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
#for row in b:
#    for number in row:
#        if(number % 2 != 0):
#            odds_in_b.append(number)

for i in range(len(b)):
    if (b[0][i] % 2 != 0):
        odds_in_b.append(b[0][i])
    if (b[1][i] % 2 != 0):
        odds_in_b.append(b[1][i])
print(odds_in_b)        
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
#for row in b:
#    for number in row:
#        if(number % 2 == 0):
#            evens_in_b.append(number)

for i in range(len(b)):
    if (b[0][i] % 2 == 0):
        evens_in_b.append(b[0][i])
    if (b[1][i] % 2 == 0):
        evens_in_b.append(b[1][i])
print(evens_in_b)
# Exercise 9 - print out the shape of the array b.
print(np.shape(b))
# Exercise 10 - transpose the array b.
print(np.transpose(b))
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
print(np.reshape(b, (1,6)))
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
print(np.reshape(b, (6,1)))
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_c = np.minimum(c[0],c[1])
min_c = np.minimum(min_c, c[2])
print(min_c)

max_c = np.maximum(c[0],c[1])
max_c = np.maximum(max_c, c[2])
print(max_c)

print(np.sum(c))

print(np.prod(c))
# Exercise 2 - Determine the standard deviation of c.
print(np.std(c))
# Exercise 3 - Determine the variance of c.
print(np.var(c))
# Exercise 4 - Print out the shape of the array c
print(np.shape(c))
# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))
# Exercise 6 - Get the dot product of the array c with c. 
print(np.dot(c,c))
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(np.sum(c*np.transpose(c)))
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
print(np.prod(c)*np.prod(np.transpose(c)))

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d=np.array(d)
# Exercise 1 - Find the sine of all the numbers in d
print(np.sin(d))
# Exercise 2 - Find the cosine of all the numbers in d
print(np.cos(d))
# Exercise 3 - Find the tangent of all the numbers in d
print(np.tan(d))
# Exercise 4 - Find all the negative numbers in d
print(d[d<0])
    
# Exercise 5 - Find all the positive numbers in d
print(d[d>0])
# Exercise 6 - Return an array of only the unique numbers in d.
print(np.unique(d))
# Exercise 7 - Determine how many unique numbers there are in d.
print(len(np.unique(d)))
# Exercise 8 - Print out the shape of d.
print(np.shape(d))
# Exercise 9 - Transpose and then print out the shape of d.
print(np.shape(np.transpose(d)))
# Exercise 10 - Reshape d into an array of 9 x 2
print(np.reshape(d, (9, 2)))

