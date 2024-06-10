"""
3.6
"""
print("【0≦X,Y,Z≦Kを満たす整数(X,Y,Z)の組であって\n")
print("X+Y+Z=Nを満たすものが何通りあるかを求める】")

K_int = int(input("正の整数K(0≦X,Y,Z≦K)"))
#K_int = 9
N_int = int(input("正の整数N(X+Y+Z=N)"))
#N_int = 12

count = 0

for X in range(K_int):
    for Y in range(K_int):
        Z = N_int - X - Y
        if(0 <= Z):
            print(f"({X},{Y},{Z})")
            if(X <= K_int and Y <= K_int and 0<= Z <= K_int):
                count += 1

print(f"{count}通り")