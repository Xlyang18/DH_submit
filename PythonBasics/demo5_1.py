max_value = lambda x, y, z: x if x >= y and x >= z else (y if y >= z else z)

a = input("请输入第一个数字：")
b = input("请输入第二个数字：")
c = input("请输入第三个数字：")
result = max_value(a, b, c)
print(result)  # 输出：3
