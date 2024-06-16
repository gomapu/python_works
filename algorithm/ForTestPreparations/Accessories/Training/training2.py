#n=int(input("n個の整数 n="))
n=5

# a=[]
# for i in range(n):
#     a.append(int(input(f"a[{i}]=")))
a=[7, 12, 5, 1, 6]

w=16 #総和w

dp = [[False]*(w+1) for i in range(n+1)]
dp[0][0]= True
for k in dp:
    print(k)

for i in range(n):
    for j in range(w+1):
        print(f"i={i} j={j}")
        #a[i]を選ばない場合
        if(dp[i][j]):
            dp[i+1][j] = True
        #a[i]を選ぶ場合
        if(j >= a[i] and dp[i][j-a[i]]):
            dp[i+1][j] =True

if(dp[n][w]):
    print("Yes")
else:
    print("No")