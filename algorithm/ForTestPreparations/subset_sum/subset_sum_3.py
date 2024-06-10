"""
5.4
"""
def chmin(a, b):
    #print(f"   a={a}, b={b}")
    if(a > b):
        a=b

    #print(f"   return={a}")
    return a

if __name__=="__main__":
    print("【N個の正整数からk個以下の整数を選んで総和をWに一致させることができるか】")

    #count = 0

    #N_int = int(input("正の整数の個数"))
    N_int = 4
    
    #W_int = int(input("総和にしたい値"))
    W_int = 14

    #K_int = int(input("何個以下の整数を選べるか"))
    K_int = 14

    N_list = [0]*N_int
    #数列に値を入力
    # for i in range(N_int):
    #     value = int(input(f"数列に入れる値 {i+1}/{N_int} 個目" ))
    #     N_list[i] = value
    N_list = [3,2,6,5]

    #メモ化テーブルの初期化
    memo = [[-1]*(W_int+1) for i in range(N_int+1)]
    memo[0][0] = 0

    for i in range(N_int):
        print(f"i={i}")
        for j in range(W_int):
            print(f" j={j}")
            #a[i]を選ばない場合
            print(f" chmin({memo[i+1][j]},{memo[i][j]})")
            chmin(memo[i+1][j], memo[i][j])

            #a[i]を選ぶ場合
            if(j >= N_list[i]):
                print(f" chmin({memo[i+1][j]},{memo[i][j-N_list[i]]})")
                chmin(memo[i+1][j], memo[i][j-N_list[i]])

    print(memo)
    if(memo[N_int][W_int] <= K_int):
        print("Yes")
    else:
        print("No")