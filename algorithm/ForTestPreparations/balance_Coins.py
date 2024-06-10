import random
import math

def Find_LightCoin(N_int, base_coins=[]):
    print(f"\nbase_coins={base_coins}")
    N_adjust = N_int//2
    print(f"N_adjust={N_adjust}")
    coins_arr1 = []
    coins_arr2 = []

    if(N_int == 1):
        return base_coins[0][1]

    if(N_int % 2 == 1):
        print("奇数")
        coins_arr1 = base_coins[:N_adjust]
        coins_arr2 = base_coins[N_adjust:N_int-1]
    else:
        print("偶数")
        coins_arr1 = base_coins[:N_adjust]
        coins_arr2 = base_coins[N_adjust:]

    print(f"coins_arr1={coins_arr1}")
    print(f"coins_arr2={coins_arr2}")

    sum_arr1 = sum(coin[0] for coin in coins_arr1)
    sum_arr2 = sum(coin[0] for coin in coins_arr2)

    if(sum_arr1 == sum_arr2):
        return base_coins[N_int-1][1]
    elif(sum_arr1 < sum_arr2):
        return Find_LightCoin(len(coins_arr1), coins_arr1)
    else:
        return Find_LightCoin(len(coins_arr2), coins_arr2)

print("【N枚のコインの中から1枚だけ重さの軽い偽コインを見つける】\n")

N_int = int(input("何枚のコイン？"))
#N_int = 11
base_coins = [[10,i] for i in range(N_int)]
coin_location= int(random.random()*N_int)

base_coins[coin_location][0]=5

print(f"{[coin[0] for coin in base_coins]}の重さ5を見つける。")

result = Find_LightCoin(N_int, base_coins)
print(f"偽コインの位置は{result+1}")