numbers = input("在此输入一组数：")
num_list = numbers.split()
num_list = [float(num) for num in num_list]

# 计算最大值、最小值、平均值、方差、标准差
max_value = max(num_list)
min_value = min(num_list)
avg_value = sum(num_list) / len(num_list)
variance = sum([(num - avg_value) ** 2 for num in num_list]) / len(num_list)
std_value = variance ** 0.5

# 输出结果
print("最大值为：", max_value)
print("最小值为：", min_value)
print("平均值为：", avg_value)
print("方差为：", variance)
print("标准差为：", std_value)
