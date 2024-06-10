"""
4.5
"""
print("【N以下の753数が何個あるかを求める】")

count=0

def func(N, current, use, count):
    if(current > N):
        return
    
    if(use == 0b111):
        count[0] += 1
    
    print(f"{N},{current*10+7},{use}|{0b001},{count}")
    func(N, current*10+7, use | 0b001, count)
    print(f"{N},{current*10+5},{use}|{0b010},{count}")
    func(N, current*10+5, use | 0b010, count)
    print(f"{N},{current*10+3},{use}|{0b100},{count}")
    func(N, current*10+3, use | 0b100, count)

if __name__=="__main__":
    N_int = int(input("K以下の753数が何個あるか"))
    #N_int=753
    count = [0]
    func(N_int, 0, 0, count)
    print(f"{N_int}以下の753数は{count[0]}個ある")