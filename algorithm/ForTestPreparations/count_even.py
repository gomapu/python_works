"""
3.5
"""
print("【「N個の整数が全て偶数ならば2で割った値に置き換える」\n")
print("とき何回の操作を行うことになるか】")

N_int = int(input("整数列の個数"))
#N_int = 6

count = 0
min_count = float('inf')

integer_list =[0]*N_int
for i in range(N_int):
    value = int(input(f"数列に入れる値 {i+1}/{N_int} 個目" ))
    integer_list[i] = value
#integer_list = [8, 12, 15, -32, -24, 8]

for i in range(N_int):
    print(f"{integer_list[i]}を2で割り切れる回数を計算")
    count = 0
    while(integer_list[i] % 2 == 0):
        integer_list[i] = integer_list[i]/2
        count += 1
        print(f"  {integer_list[i]} {count}回")
    if(count < min_count):
        min_count = count

print("\n")
if(min_count == 0):
    print("奇数が含まれているため一度も操作できません。")
elif(min_count > 0):
    print(f"{min_count}回の操作")