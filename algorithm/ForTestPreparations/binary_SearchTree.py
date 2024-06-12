"""
5.9
"""
def chmin(a,b):
    if(a > b):
        a=b
        return a, True
    return a, False

def main():
    print("【スライムを合体させるための最小コストを求める】")

    inf = float('inf')

    #N_int=int(input("スライムは何匹？"))
    N_int=10

    a_slime_size=[0]*N_int
    # for i in range(N_int):
    #     a_slime_size[i] = int(input(f"{i+1}番目のスライムの大きさは？"))
    a_slime_size = [4,6,1,2,9,3,2,9,10,2]

    #累積和をとる
    S_slime_size=[0]*(N_int+1)
    for i in range(N_int):
        S_slime_size[i+1] = S_slime_size[i]+ a_slime_size[i]
        print(f"{S_slime_size[i+1]}=S[{i+1}]=S[{i}]+a[{i}]")

    #DP
    dp = [[inf]*(N_int+1) for _ in range(N_int +1)]

    #初期条件
    for i in range(N_int):
        dp[i][i+1] = 0

    #更新
    for bet in range(2, N_int+1):
        print(f"bet={bet}")
        for i in range(N_int+1 - bet):
            print(f" i={i}")
            j = i+bet
            print(f" j={j}")

            #dp[i][j]を更新する
            for k in range(i+1, j):
                print(f"  k={k}")
                dp[i][j], updated = chmin(dp[i][j], dp[i][k] + dp[k][j] + S_slime_size[j] + S_slime_size[i])
                print(f"   dp[{i}][{j}]=chmin(dp[{i}][{j}], dp[{i}][{k}]+dp[{k}][{j}]+S[{j}]+S[{i}])")
                print(f"   dp[{i}][{j}]=chmin({dp[i][j]}, {dp[i][k]+dp[k][j]+S_slime_size[j]+S_slime_size[i]})")

    print(dp)
    print(dp[0][N_int])

if __name__=="__main__":
    main()