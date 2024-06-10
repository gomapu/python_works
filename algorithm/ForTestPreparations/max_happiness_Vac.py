"""
5.1
"""
print("【N日間の幸福度の最大値をO(N)で求める】")

def chmax(a, b):
    #print(f"   a={a}, b={b}")
    if(a < b):
        a=b

    #print(f"   return={a}")
    return a

def main():
    #N_days = int(input("何日間"))
    N_days = 5

    # a = []
    # for i in range(N_days):
    #     # 各日の幸福度を3つの値として入力
    #     a.append(list(map(int, input().split())))
    a = [[4, 5, 2], [5, 7, 3], [5, 8, 2], [1, 2, 3], [6, 7, 3]]
    print(a)

    dp = [[0]*3 for _ in range(N_days+1)]
    print(dp)

    #i日目からi+1日目へ
    for i in range(N_days):
        print(f"i={i}")
        #i日目の状態はj、i+1日目の状態はk
        for j in range(3):
            print(f" j={j}")
            for k in range(3):
                print(f"  k={k}")
                if(j==k):
                    continue

                print(f"  chmax({dp[i+1][k]}, {dp[i][j]+a[i][k]})")
                dp[i+1][k] = chmax(dp[i+1][k], dp[i][j]+a[i][k])
                print(f"   {dp}")

    res = 0
    for j in range(3):
        res=chmax(res, dp[N_days][j])
    print(res)

if __name__=="__main__":
    main()