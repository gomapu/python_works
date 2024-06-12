"""
5.7
"""
def chmax(a,b):
    if(a < b):
        a=b
    return a

def chmin(a,b):
    if(a > b):
        a=b
    return a

def main():
    print("【最小共通部分列LCSを求める】")

    S_str = "stereotype" #固定観念
    T_str = "mosterstrike" #モンスターストライク
    #"sterte"が最長の部分文字列になる？

    N_S_int = len(S_str)
    N_T_int = len(T_str)

    print(f"{S_str}の長さは{N_S_int}で\n{T_str}の長さは{N_T_int}である")

    dp = [[0]*(N_T_int+1) for i in range(N_S_int+1)]
    print(dp)

    for i in range(N_S_int+1):
        print(f" i={i}")
        for j in range(N_T_int+1):
            print(f"  j={j}")
            #Sのi文字目とTのj文字目が等しい時
            if(i>0 and j>0):
                if(S_str[i-1] == T_str[j-1]):
                    dp[i][j]= chmax(dp[i][j], dp[i-1][j-1]+1)
                    print(f"  dp[{i}][{j}]=chmax({dp[i][j]}, {dp[i-1][j-1]+1})")
                else:
                    dp[i][j]=chmax(dp[i][j], dp[i-1][j-1])
                    print(f"  dp[{i}][{j}]=chmax({dp[i][j]}, {dp[i-1][j-1]})")

            #Sに1文字追加
            if(i>0):
                dp[i][j]= chmax(dp[i][j], dp[i-1][j])
                print(f"  dp[{i}][{j}]=chmax({dp[i][j]}, {dp[i-1][j]})")

            #Tに1文字追加
            if(j>0):
                dp[i][j]= chmax(dp[i][j], dp[i][j-1])
                print(f"  dp[{i}][{j}]=chmax({dp[i][j]}, {dp[i][j-1]})")

            print(f"jループ\n{dp}") 
        print(f"iループ\n{dp}")
    
    #LCS
    print(dp[N_S_int][N_T_int])

if __name__=="__main__":
    main()