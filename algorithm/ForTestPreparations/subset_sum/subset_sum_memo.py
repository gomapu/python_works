def func(i, w, a={}, memo={}):
    #ベースケース
    print(f"i={i}, w={w}")
    if(i==0):
        if(w==0):
            return True
        else:
            return False
        
    if(memo[i][w] != -1):
        return memo[i][w]
        
    #a[i-1]を選ばない場合
    print(f"func({i-1},{w})")
    if(func(i-1, w, a, memo)):
        print("True")
        memo[i][w] = True
        return True
    
    #a[i-1]を選ぶ場合
    print(f"func({i-1},{w-a[i-1]})")
    if(func(i-1, w-a[i-1], a, memo)):
        print("True")
        memo[i][w] = True
        return True
    
    #どちらもfalseの場合はfalse
    memo[i][w]= False
    print("False")
    return False

if __name__=="__main__":
    #N_int = int(input("正の整数の個数"))
    N_int = 4
    N_list = [0]*N_int

    #W_int = int(input("総和にしたい値"))
    W_int = 14

    # for i in range(N_int):
    #     value = int(input(f"数列に入れる値 {i+1}/{N_int} 個目" ))
    #     N_list[i] = value
    N_list = [3,2,6,5]

    memo = [[-1]*(W_int+1) for i in range(N_int+1)]

    if(func(N_int, W_int, N_list, memo)):
        print("Yes")
    else:
        print("No")