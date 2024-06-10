"""
3.3
"""
print("【リスト内の最小値と二番目に小さい値を見つける】")

N_int = int(input("整数列の個数"))
#N_int = 6
MIN_value= float('inf')
SecMin_value= float('inf')

integer_list =[0]*N_int
for i in range(N_int):
    value = int(input(f"数列に入れる値 {i+1}/{N_int} 個目" ))
    integer_list[i] = value

for j in range(N_int):
    print(f"{integer_list[j]} < {MIN_value}")
    if(integer_list[j] < MIN_value):
        MIN_value = integer_list[j]
        print(f"MIN_value = {MIN_value}")
    for k in range(N_int):
        print(f"  {integer_list[k]} > {MIN_value} and {integer_list[k]} < {SecMin_value}")
        if(integer_list[k] > MIN_value and integer_list[k] < SecMin_value):
            SecMin_value = integer_list[k]
            print(f"  SecMIN_value = {SecMin_value}")

print("\n")
print(f"一番目に小さい値は{MIN_value}") #I have adopted an unnatural phrasing to fit the text below.
print(f"二番目に小さい値は{SecMin_value}")