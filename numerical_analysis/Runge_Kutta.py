"""
Runge Kutta Method
"""
print("ルンゲ・クッタ法\n")

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

    k1=func(x,y)
    k2=func(x+h/2.0, y+k1*h/2.0)
    k3=func(x+h/2.0, y+k2*h/2.0)
    k4=func(x+h, y+k3*h)

    y= y+h*(k1+ 2.0*k2+ 2.0*k3+ k4)/6 #ルンゲ・クッタ公式
    x+= h
    print(f"x={x} y={y}")

print("")
print(f"微分方程式dy/dx=x*yの数値解は\nx={prev_x} y={prev_y}")