"""
Monte Carlo Method
"""
import random

print("モンテカルロ法")

#乱数を生成
random_list= []
for i in range(10):
    random_list.append(random.uniform(1,6)) #1から6までの乱数を生成
print(random_list)