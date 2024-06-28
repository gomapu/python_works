"""
Trapezoid Method
"""
import numpy as np
import math

def integration_func(x):
    return math.e**(-x)

b = 1
a = 0

for k in range(1,11):
    n= 2**k #分割数n=2^k(=1,2,3,...,10)
    h=(b-a)/n
    s=0
    for i in range(1,n):
        #for文の前にx=aを与えx+=hとしたいが累積誤差を考慮しこうする
        x= a+ h*i 
        s += 2*integration_func(x)
    
    s= 0.5*(s+ integration_func(a)+ integration_func(b))*h
    print(f"n=2^{k}のときの定積分は{s}")

