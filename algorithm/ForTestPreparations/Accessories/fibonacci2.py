memo = [0]*40

def fib1(n):
    if n <= 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
 
print(fib1(30)) # 1346269

def fib2(n):
    if n <= 1:
        return 1
    else:
        if memo[n] == 0:
            memo[n] = fib2(n-1) + fib2(n-2)
        return memo[n]
 
print(fib2(30)) # 1346269

def fib3(n):
    a = [1] * (n+1) # a[0] = 1, a[1] = 1
 
    # a[2] 以降の導出
    for i in range(2,n+1):
        print(f"i={i}")
        print(f"a[{i}]=a[{i-1}]+a[{i-2}]")
        a[i] = a[i-1] + a[i-2]
        print(f"a[{i}]={a[i]}")
     
    return a[n]

print(fib3(30)) #1246269