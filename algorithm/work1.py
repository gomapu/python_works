def max_avg_sum(nums):
    n = len(nums)
    
    # 累積和を計算する
    cum_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        cum_sum[i] = cum_sum[i - 1] + nums[i - 1]
    
    print("累積和:", cum_sum)
    
    # 3つの連続した区間の平均値の総和を最大化する
    max_sum = float('-inf')
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            print("i=", i, " j=", j)

            # 区間の合計値
            sum1 = cum_sum[i] - cum_sum[0]
            sum2 = cum_sum[j] - cum_sum[i]
            sum3 = cum_sum[n] - cum_sum[j]
            
            print("sum1:",sum1, " sum2:",sum2, " sum3:",sum3)
            
            # 区間の平均値の総和を計算
            avg_sum = (sum1 / i) + (sum2 / (j - i)) + (sum3 / (n - j))
            print("avg_sum:", avg_sum, "\n")
            
            # 平均値の総和が最大の場合、更新する
            if avg_sum > max_sum:
                max_sum = avg_sum
    
    return max_sum

nums = [9, 1, 2, 3, 9]
result = max_avg_sum(nums)
print("最大の平均値の総和:", result)