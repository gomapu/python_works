"""
Simpson Method
"""
import numpy as np
import math

def integration_func(x):
    return math.e**(-x)

b = 1
a = 0

n=10
h=(b-a)/(2*n)

s1=0
for i in range(1,2*n-1+1,2):
    x= a+h*i
    s1+= 4*integration_func(x)

s2=0
for i in range(2,2*n-2+1, 2):
    x=a+h*i
    s2+= 2*integration_func(x)

s=(s1+s2+integration_func(a)+integration_func(b))*h/3
print(s)