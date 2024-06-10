"""
5.5
"""
def chmax(a, b):
    if(a < b):
        return b
    else:
        return a

def chmin(a, b):
    if(a > b):
        return b
    else:
        return a

def main():
    # Input
    N_int = int(input("正の整数の個数"))
    W_int = int(input("目指す総和"))
    a = []
    for i in range(N_int):
        a.append(int(input("数列に入れる値{i}/{N_int} 個目")))
    print(a)

    # DP Table
    dp = [[False] * (W_int + 1) for _ in range(N_int + 1)]
    print(dp)

    # Initial condition
    dp[0][0] = True

    # Loop
    for i in range(N):
        for j in range(W + 1):
            if dp[i][j]:
                dp[i + 1][j] = True
            if j >= a[i] and dp[i][j]:
                dp[i + 1][j - a[i]] = True

    # Answer
    if dp[N][W]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
