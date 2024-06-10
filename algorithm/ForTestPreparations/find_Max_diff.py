"""
3.4
"""
print("【リスト内の二つの値の差が最大のものを見つける】")

N_int = int(input("整数列の個数"))
# N_int = 6
MAX_diff = -float('inf')
diff = 0

integer_list =[0]*N_int
for i in range(N_int):
    value = int(input(f"数列に入れる値 {i+1}/{N_int} 個目" ))
    integer_list[i] = value
# integer_list = [4, 12, 2, -4, -1, 9]

for i in range(N_int):
    for j in range(N_int):
        print(f"({integer_list[i]})-({integer_list[j]})")
        diff = integer_list[i] - integer_list[j]
        abs(diff)
        print(diff)
        if(diff > MAX_diff):
            MAX_diff = diff

print("\n")
print(f"差の最大値は{MAX_diff}")
