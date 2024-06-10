"""
5.3
"""
def func(i, w, a={}, memo={}):
    #ベースケース
    print(f"i={i}, w={w}")
    if(i==0):
        if(w==0):
            return True
        else:
            return False
    
    #メモ化テーブルの確認
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
    count = 0

    N_int = int(input("正の整数の個数"))
    #N_int = 4
    
    W_int = int(input("総和にしたい値"))
    #W_int = 14

    N_list = [0]*N_int
    #数列に値を入力
    for i in range(N_int):
        value = int(input(f"数列に入れる値 {i+1}/{N_int} 個目" ))
        N_list[i] = value
    #N_list = [3,2,6,5]

    #メモ化テーブルの初期化
    memo = [[-1]*(W_int+1) for i in range(N_int+1)]

    # 1からW_intまでの値について、総和がその値に一致するかを判定
    for w in range(1, W_int+1):
        #総和ができる(関数がTrueを返す)ときカウント+1
        if(func(N_int, w, N_list, memo)):
            count += 1

    #結果を出力
    print(f"結果は{count}通り")