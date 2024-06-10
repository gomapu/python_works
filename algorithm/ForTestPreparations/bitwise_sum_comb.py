"""
3.7
"""
print("【入力された数値の各桁の組み合わせに対して全ての可能な加算方法を探索しその合計を計算する】")

S_string = input("各桁の値が1以上9以下の数値のみである整数")
#S_string = "125"
N_length = len(S_string)

result = 0
for bit in range(1<<(N_length - 1)):
    print(f"bit={bit}")
    tmp = 0
    for i in range(N_length-1):
        print(f" i={i}")
        tmp *= 10
        print(f"  tmp={tmp}, S_string[i]={S_string[i]}")
        tmp += int(S_string[i]) - 0
        print(f"  tmp={tmp}")

        if(bit & (1 << i)):
            result += tmp
            print(f"   result={result}")
            tmp = 0
        
    tmp *= 10
    tmp += int(S_string[-1]) -0
    result += tmp

print(f"合計は{result}")