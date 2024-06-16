n=5
m=3
a = [9,1,2,3,9]
inf = float("inf")

#区間の平均値を前処理で求める
f = [[0]*(n+1) for i in range(n+1)]
# for i in f:
#     print(i)

for i in range(1,n+1):
    for j in range(i):
        sum=0
        for k in range(j, i):
            #print(f"i={i} j={j} k={k}")
            sum += a[k]
            f[j][i] = sum/(i-j)

for i in f:
    print(i)

#DP
dp=[[-inf]*(m+1) for i in range(n+1)]
dp[0][0] =0
for i in range(n+1):
    for j in range(i):
        for k in range(1, m+1):
            dp[i][k] = max(dp[i][k], dp[j][k-1]+f[j][i])

res = -inf
for i in range(m+1):
    res = max(res, dp[n][m])
print(res)