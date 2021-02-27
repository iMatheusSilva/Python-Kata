#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Plot a Linear Function 

import numpy as np 
from matplotlib import pyplot as plt

#calculates a linear function
def f(x, a, b):return a*x+b 

#plots linear function graph in a given interval 
def plotfn(a,b,interval):
  x = np.linspace(interval[0],interval[1])  
  plt.plot(x, f(x, a, b)) 
  plt.grid()


#params: a, b, function plot interval
plotfn(4, -1, [0,10])


#




