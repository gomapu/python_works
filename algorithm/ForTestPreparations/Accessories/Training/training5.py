str1= "myabcuuu"
str2= "abcjju"
# 最長共通部分列は
# "abcu"

n= len(str1)
m= len(str2)

dp= [[0]*(n+1) for i in range(m+1)]
for i in dp:
    print(i)
print("")

for i in range(m):
    for j in range(n):
        if(str1[j] == str2[i]):
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1]= max(dp[i+1][j], dp[i][j+1])

print(str1)
print(str2)
for i in dp:
    print(i)

print(dp[m][n])