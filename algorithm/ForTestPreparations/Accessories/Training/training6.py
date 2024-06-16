n=4
w=[2, 3, 4, 5]
v=[3, 4, 5, 6]
w_limit=5

dp= [[0]*(w_limit+1) for _ in range(n+1)]
for i in dp:
    print(i)
print("")

for i in range(n):
    for j in range(w_limit+1):
        if(w[i] > j):
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]]+v[i])

for i in dp:
    print(i)
print(dp[n][w_limit])