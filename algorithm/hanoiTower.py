
'''
#引数：段数，移動元，移動先，経由, 回数
def hanoi(count, n, source, to, work ):
    if n > 1:
        hanoi(count, n-1, source, work, to)  #再帰
        print(str(count) + '回 ' + str(n)+ '段 ' + source + '->' + to)
        hanoi(count+1, n-1, work, to, source)  #再帰
    else:
        print(str(count) + '回 ' + str(n)+ '段 ' + source + '->' + to)
        return count +1
        
count = 1
n = int(input('ハノイの段数 >> '))
hanoi(count , n, 'a', 'c', 'b')
'''

#引数：段数，移動元，移動先，経由, 回数
def hanoi(n, source, to, work ):
    print(source, to, work)
    if n > 1:
        hanoi(n-1, source, work, to)  #再帰
        print(str(n)+ '段 ' + source + '->' + to)
        hanoi(n-1, work, to, source)  #再帰
    else:
        print(str(n)+ '段 ' + source + '->' + to)
        

n = int(input('ハノイの段数 >> '))
hanoi(n, 'a ', 'c ', 'b ')