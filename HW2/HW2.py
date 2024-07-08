#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as figure


# In[2]:


#Intermediate insertion sort for bucket sort
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i>=0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


# In[3]:


#Implementation of bucket sort for sorting empirical CDF values
def bucketSort(A):
    B = []
    num_buckets = 10
    
    for i in range(num_buckets):
        B.append([])
        
    for i in A:
        index_B = int(num_buckets * i)
        B[index_B].append(i)
    
    for i in range(num_buckets):
        B[i]=insertionSort(B[i])
    
    k=0
    for i in range(num_buckets):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A


# In[4]:


#First Set of Randomly Generated Numbers
bounda1=1.0
boundb1=3.0
random.seed(0)
set1=[]
for i in range(10000):
    set1.append(random.uniform(0,1))


# In[5]:


#Second Set of Randomly Generated Numbers
bounda2=2.0
boundb2=7.0
random.seed(1)
set2=[]
for i in range(10000):
    set2.append(random.uniform(0,1))


# In[6]:


#Third Set of Randomly Generated Numbers
bounda3=11.0
boundb3=18.0
random.seed(2)
set3=[]
for i in range(10000):
    set3.append(random.uniform(0,1))


# In[7]:


#Q1(iii) - Part1 : Generate three sequences Xi={xi,1, xi,2, xi,3, … , xi,n}, where i=1,2,3, of numbers (n=10000 samples each) uniformly distributed over the intervals (ai,bi).
#Using the inverse transformation to generate the 3 required sets.
trans_set1=[]
for i in range(0,len(set1)):
    trans_set1.append((set1[i]*(boundb1-bounda1))+bounda1)
    
trans_set2=[]
for i in range(0,len(set2)):
    trans_set2.append((set2[i]*(boundb2-bounda2))+bounda2)
    
trans_set3=[]
for i in range(0,len(set3)):
    trans_set3.append((set3[i]*(boundb3-bounda3))+bounda3)


# In[8]:


#Original Sequence 1 sorted. We use bucket sort for this.
set1_sorted=bucketSort(set1)

#Original Sequence 2 sorted.
set2_sorted=bucketSort(set2)

#Original Sequence 3 sorted.
set3_sorted=bucketSort(set3)


# In[9]:


#Q1(iii) - Sampling k values. We choose k as 50. Taking different samples to do the curve sketching of Empirical CDF
#subsets of sequence1
set1_subset1 = set1_sorted[0:50]
set1_subset2 = set1_sorted[5000:5050]
set1_subset3 = set1_sorted[9950:10000]

#subsets of sequence2
set2_subset1 = set2_sorted[0:50]
set2_subset2 = set2_sorted[5000:5050]
set2_subset3 = set2_sorted[9950:10000]

#subsets of sequence3
set3_subset1 = set3_sorted[0:50]
set3_subset2 = set3_sorted[5000:5050]
set3_subset3 = set3_sorted[9950:10000]


# In[10]:


#Q1(iii) - Part2 (2nd half till the end of this program) : Plot their empirical CDFs Fi(e)(xj), where j=1,2,3, … , k. 
#Assume k << n.
#Transforming the subsets of set 1 using Inverse transform method.
trans_set1_subset1=[]
for i in range(0,len(set1_subset1)):
    trans_set1_subset1.append((set1_subset1[i]*(boundb1-bounda1))+bounda1)
    
trans_set1_subset2=[]
for i in range(0,len(set1_subset2)):
    trans_set1_subset2.append((set1_subset2[i]*(boundb1-bounda1))+bounda1)
    
trans_set1_subset3=[]
for i in range(0,len(set1_subset3)):
    trans_set1_subset3.append((set1_subset3[i]*(boundb1-bounda1))+bounda1)

#Transforming the subsets of set 2 using Inverse transform method.
trans_set2_subset1=[]
for i in range(0,len(set2_subset1)):
    trans_set2_subset1.append((set2_subset1[i]*(boundb2-bounda2))+bounda2)
    
trans_set2_subset2=[]
for i in range(0,len(set2_subset2)):
    trans_set2_subset2.append((set2_subset2[i]*(boundb2-bounda2))+bounda2)
    
trans_set2_subset3=[]
for i in range(0,len(set2_subset3)):
    trans_set2_subset3.append((set2_subset3[i]*(boundb2-bounda2))+bounda2)
    
#Transforming the subsets of set 3 using Inverse transform method.
trans_set3_subset1=[]
for i in range(0,len(set3_subset1)):
    trans_set3_subset1.append((set3_subset1[i]*(boundb3-bounda3))+bounda3)
    
trans_set3_subset2=[]
for i in range(0,len(set3_subset2)):
    trans_set3_subset2.append((set3_subset2[i]*(boundb3-bounda3))+bounda3)
    
trans_set3_subset3=[]
for i in range(0,len(set3_subset3)):
    trans_set3_subset3.append((set3_subset3[i]*(boundb3-bounda3))+bounda3)    


# In[11]:


#Theoretical CDF values over the bounds of set 1 i.e.(1,3).
X1=[]
for i in range(0,10000):
    X1.append(random.uniform(bounda1,boundb1))
    
Y1=[]
for i in X1:
    Y1.append((i-bounda1)/(boundb1-bounda1))


# In[12]:


fig, axs = plt.subplots(3, figsize = (15,15))
#fig.tight_layout()

axs[0].plot(trans_set1_subset1,set1_subset1)
axs[0].set_title('Empirical CDF plot for subset 1 of set 1 uniformly distributed over (1,3)')

axs[1].plot(trans_set1_subset2,set1_subset2)
axs[1].set_title('Empirical CDF plot for subset 2 of set 1 uniformly distributed over (1,3)')

axs[2].plot(trans_set1_subset3,set1_subset3)
axs[2].set_title('Empirical CDF plot for subset 3 of set 1 uniformly distributed over (1,3)')


# In[13]:


fig, axs = plt.subplots(1,1, figsize = (10,10))
plt.plot(X1,Y1,'r',label='Theoretical CDF')
plt.plot(trans_set1_subset1,set1_subset1,'g',label='Empirical CDF of subset 1 of set 1')
plt.plot(trans_set1_subset2,set1_subset2,'g',label='Empirical CDF of subset 2 of set 1')
plt.plot(trans_set1_subset3,set1_subset3,'g',label='Empirical CDF of subset 3 of set 1')
plt.legend()
plt.title('Theoretical CDF and Empirical CDFs of set1 overlayed on one plot to do the comparison')


# In[14]:


#Theoretical CDF values over the bounds of set 2 i.e. (2,7).
X2=[]
for i in range(0,10000):
    X2.append(random.uniform(bounda2,boundb2))
    
Y2=[]
for i in X2:
    Y2.append((i-bounda2)/(boundb2-bounda2))


# In[15]:


fig, axs = plt.subplots(3, figsize = (15,15))
#fig.tight_layout()

axs[0].plot(trans_set2_subset1,set2_subset1)
axs[0].set_title('Empirical CDF plot for subset 1 of set 2 uniformly distributed over (2,7)')

axs[1].plot(trans_set2_subset2,set2_subset2)
axs[1].set_title('Empirical CDF plot for subset 2 of set 2 uniformly distributed over (2,7)')

axs[2].plot(trans_set2_subset3,set2_subset3)
axs[2].set_title('Empirical CDF plot for subset 3 of set 2 uniformly distributed over (2,7)')


# In[16]:


fig, axs = plt.subplots(1,1, figsize = (10,10))
plt.plot(X2,Y2,'r',label='Theoretical CDF')
plt.plot(trans_set2_subset1,set2_subset1,'g',label='Empirical CDF of subset 1 of set 2')
plt.plot(trans_set2_subset2,set2_subset2,'g',label='Empirical CDF of subset 2 of set 2')
plt.plot(trans_set2_subset3,set2_subset3,'g',label='Empirical CDF of subset 3 of set 2')
plt.legend()
plt.title('Theoretical CDF and Empirical CDFs of set 2 overlayed on one plot to do the comparison')


# In[17]:


#Theoretical CDF values over the bounds of set 2 i.e. (11,18).
X3=[]
for i in range(0,10000):
    X3.append(random.uniform(bounda3,boundb3))
    
Y3=[]
for i in X3:
    Y3.append((i-bounda3)/(boundb3-bounda3))


# In[18]:


fig, axs = plt.subplots(3, figsize = (15,15))
#fig.tight_layout()
axs[0].plot(trans_set3_subset1,set3_subset1)
axs[0].set_title('Empirical CDF plot for subset 1 of set 3 uniformly distributed over (11,18)')

axs[1].plot(trans_set3_subset2,set3_subset2)
axs[1].set_title('Empirical CDF plot for subset 2 of set 3 uniformly distributed over (11,18)')

axs[2].plot(trans_set3_subset3,set3_subset3)
axs[2].set_title('Empirical CDF plot for subset 3 of set 3 uniformly distributed over (11,18)')


# In[19]:


fig, axs = plt.subplots(1,1, figsize = (10,10))
plt.plot(X3,Y3,'r',label='Theoretical CDF')
plt.plot(trans_set3_subset1,set3_subset1,'g',label='Empirical CDF of subset 1 of set 3')
plt.plot(trans_set3_subset2,set3_subset2,'g',label='Empirical CDF of subset 2 of set 3')
plt.plot(trans_set3_subset3,set3_subset3,'g',label='Empirical CDF of subset 3 of set 3')
plt.legend()
plt.title('Theoretical CDF and Empirical CDFs of set 3 overlayed on one plot to do the comparison')

