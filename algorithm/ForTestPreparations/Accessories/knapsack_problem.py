def Sushi_choice(cost_list, kcal_list, limit):
    list_len = len(kcal_list)
    dp_table = [[0 for j in range(limit+1)] for i in range(list_len)]

    # dp_tableの初期状態を表示
    for row in dp_table:
        print(row)

    #1品目を食べるか食べないか
    for j in range(limit+1):
        if(kcal_list[0] <= j):
            dp_table[0][j] = cost_list[0] #食べるとき

    for i in dp_table:
        print(i)

    #2品目以降を食べるか食べないか
    for i in range(1, list_len):
        print(f"i={i}")
        for j in range(limit+1):
            print(f" j={j}")
            tmp_not_choice= dp_table[i-1][j]
            if (kcal_list[i]>j): #カロリーオーバー
                dp_table[i][j] = tmp_not_choice #食べられない
            else:
                tmp_choice= dp_table[i-1][j - kcal_list[i]] + cost_list[i]
                dp_table[i][j] = max(tmp_choice, tmp_not_choice)

            # dp_tableの状態を表示
            for row in dp_table:
                print(row)
    
    return dp_table[list_len -1][limit]

def main():
    cost= [120,150,140,110,100] #それぞれの寿司の値段
    kcal= [8,10,7,6,7] #それぞれの寿司のカロリー
    limit_kcal=30

    ans = Sushi_choice(cost, kcal, limit_kcal)
    print(ans)

if __name__=="__main__":
    main()