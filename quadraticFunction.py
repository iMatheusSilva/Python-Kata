#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Plots a Quadratic Equation 

import numpy as np 
from matplotlib import pyplot as plt

#calculates a quadratic function
def f(x, a, b, c):return (a*(x*x))+(b*x)+c 

#plots quadratic function graph in a given interval 
def plotfn(a,b,c,interval):
  x = np.linspace(interval[0],interval[1])  
  plt.plot(x, f(x, a, b, c)) 
  plt.grid()


#params: a, b, c, function plot interval
plotfn(1, 0, 0, [-10,10])







