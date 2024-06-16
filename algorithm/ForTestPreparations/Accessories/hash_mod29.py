"""
ハッシュ関数(x mod 29)
"""
def hash_original(x=[]):
    hashed_values=[]

    x_num = len(x)
    for i in range(x_num):
        hashed_value = x[i] % 29
        hashed_values.append(hashed_value)
        print(f"x[{i}]={x[i]} -> hash(x[{i}]={hashed_value})")
    return hashed_values

def main():
    S=[1,7,14,24,39,46,56,62,76,83,93,100,105,121,126,135,145,155,157,175,178]

    S_after=hash_original(S)
    print("Original:\n",S)
    print("hashed:\n",S_after)

if __name__=="__main__":
    main()