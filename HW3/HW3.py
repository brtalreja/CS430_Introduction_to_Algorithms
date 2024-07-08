#!/usr/bin/env python
# coding: utf-8

# #Without Memoization (Recursive Top-Down Procedure)

# In[22]:


#Recursive Top-Down implementation of Fib()
def Fib(n):
    if n < 0:
        print("incorrect input") #negative input
    elif n == 0 or n == 1:
        return n #base case
    else:
        return Fib(n-1) + Fib(n-2) #By definition of fibonacci series, Fib() calls Fib(n-1) and Fib(n-2)


# In[36]:


#Taking input from the user to calculate the nth Fibonacci term.
n = int(input("What fibonacci term would you like to get in a fibonacci sequence?\n"))

#Calling the Fib() and Displaying the nth term.
Fib(n)


# #Updating the Fib() for part(d) to calculate the number of calls.

# In[12]:


#Same recursive top-down function as above, we just added the functionality to calcuate the number of recursive calls.
def Fib(n):
    if n < 0:
        print("incorrect input") #negative input
    elif n == 0:
        return (0,1) #1st base case takes 1 call
    elif n == 1:
        return (1,1) #2nd base case takes 1 call
    else:
        prev_term1, n_calls_prev1 = Fib(n-1) #(n-1)th term and its corresponding number of recursive calls
        prev_term2, n_calls_prev2 = Fib(n-2) #(n-2)th term and its corresponding number of recursive calls
        return prev_term1 + prev_term2, n_calls_prev1 + n_calls_prev2 + 1
        #(n)th term and its corresponding number of recursive calls including the first call to the function (i.e. +1 term)


# In[14]:


#Calculating the number of recursive calls made by the Fib() in a dictionary.
#Testing n=9 to n=22.
k_v_dict = {k:0 for k in range(9,23)}

#iterating over the dictionary to calucate the nth term and number of calls for that n.
for k,v in k_v_dict.items():
    nth_Fib, n_calls = Fib(k)
    k_v_dict[k] = n_calls
    print(f"Fibonacci term {k} is {nth_Fib}")
    print(f"Number of calls: {n_calls}")


# #With Memoization (Iterative Bottom-Up Procedure)

# In[25]:


#Iterative Bottom-Up implementation of Fib(), we call it as Better_Fib()
def Better_Fib(n):
    
    mem=[0,1] #storing two bases in an array for the memoization.
    
    for i in range(2,n+1):
        mem.append(mem[i-1] + mem[i-2]) #calculating and appending the nth fibonacci term in the array created for memoization
    return mem[n] #looking up the nth term in the array


# In[43]:


#Taking input from the user to calculate the nth Fibonacci term.
n = int(input("What fibonacci term would you like to get in a fibonacci sequence?\n"))

#Calling the Better_Fib() and displaying the nth term.
Better_Fib(n)

