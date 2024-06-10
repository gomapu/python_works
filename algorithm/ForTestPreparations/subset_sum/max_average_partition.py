"""
5.8
"""
import sys
input = sys.stdin.read

def chmax(a, b):
    if a < b:
        return b, True
    return a, False

INF = float('inf')

def main():
    #N_int = int(input("正の整数の個数"))
    N_int = 5

    #M_int = int(input("分けたい連続する区間の個数"))
    M_int = 3

    # a = [0]*N_int
    # for i in range(N_int):
    #     a[i] = int(input(f"数列に入れる値 {i+1}/{N_int} 個目"))
    a = [9,1,2,3,9]
    print(a)

    #区間の平均値の前処理
    f = [[0.0] * (N_int+1) for _ in range(N_int+1)]
    
    for i in range(1, N_int+1):
        print(f"i={i}")
        for j in range(i):
            print(f" j={j}")
            sum_val = sum(a[j:i])
            print(f" sum_val = sum(a[{j}:{i}]) = {sum_val}")
            f[j][i] = sum_val / (i - j)
            print(f" f[{j}][{i}] = {sum_val}/{i-j}")

    # DP
    dp = [[-INF] * (M_int+1) for _ in range(N_int+1)]
    dp[0][0] = 0
    for i in range(N_int+1):
        print(f"i={i}")
        for j in range(i):
            print(f" j={j}")
            for k in range(1, M_int+1):
                print(f"  k={k}")
                dp[i][k], updated = chmax(dp[i][k], dp[j][k-1] + f[j][i])
                print(f"  dp[{i}][{k}],updated = chmax({dp[i][k]}, {dp[j][k-1] + f[j][i]})")
    
    res = -INF
    for m in range(M_int+1):
        res, updated = chmax(res, dp[N_int][m])
    
    print(f"{res:.10f}")

if __name__ == "__main__":
    main()