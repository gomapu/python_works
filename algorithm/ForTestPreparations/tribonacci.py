"""
4.1
"""
print("【トリボナッチ数列の第N項を求める】")

n = int(input("トリボナッチ数列の第何項を求めますか？"))
#n = 10

tribo_list = [-1]*10

def Tribonacci(n):
    print(f"Tribonacci({n})を呼び出しました。")
    if(tribo_list[n] != -1):
        return tribo_list[n]

    if(n==0):
        tribo_list[n]=0
        return 0
    elif(n==1):
        tribo_list[n]=0
        return 0   
    elif(n == 2):
        tribo_list[n]=1
        return 1
    
    result = Tribonacci(n-3) + Tribonacci(n-2) + Tribonacci(n-1)
    print(f"第{n+1}項:{result}")
    tribo_list[n]=result
    return result

value = Tribonacci(n-1)
print(tribo_list)
print(f"第{n}項の値={value}")