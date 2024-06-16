weight=[11, 4, 2, 1, 3, 5]
value=[15, 4, 3, 2, 1, 8]
w_limit=15

dp = [[0]*(w_limit+1) for i in range(len(weight)+1)]
for i in dp:
    print(i)

for i in range(len(weight)):
    for j in range(w_limit+1):
        if(j < weight[i]):
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = max(dp[i][j], dp[i][j-weight[i]] + value[i])

print("")
for i in dp:
    print(i)
print(dp[len(weight)][w_limit])