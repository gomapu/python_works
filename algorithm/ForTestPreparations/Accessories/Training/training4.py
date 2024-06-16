n=5

a=[
    [3, 1, 2],
    [2, 5, 3],
    [1, 2, 2],
    [6, 1, 2],
    [0, 5, 3]
]

#DP
dp = [[0]*3 for i in range(n+1)]
for i in dp:
    print(i)

#i日目からi+1日目へ
for i in range(n):
    for j in range(3):
        for k in range(3):
            if(j==k):
                continue
            dp[i+1][k]= max(dp[i+1][k], dp[i][j] + a[i][k])

print("")
for i in dp:
    print(i)