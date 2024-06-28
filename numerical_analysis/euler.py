"""
Euler Method
"""
print("オイラー法\n")

def func(x,y):
    return x*y

a=0
b=1
print(f"区間[{a}≦x≦{b}]")
h=1 #b-a
n=1000 #等分数

h= (b-a)/n
x= a
y= b

print(f"x={x} y={y}")

prev_x= x
prev_y= y
while(x<b):
    prev_x= x
    prev_y= y
    y= y+h*func(x, y)
    x+= h
    print(f"x={x} y={y}")

print("")
print(f"微分方程式dy/dx=x*yの数値解は\nx={prev_x} y={prev_y}")