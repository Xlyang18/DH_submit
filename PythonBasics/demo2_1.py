# 获取用户输入的字符串
input_str = input("请输入一个字符串：")

# 初始化一个字典来存储每个字符及其出现的次数
char_count = {}

# 遍历字符串中的每个字符
for char in input_str:
    # 如果字符已经在字典中，则将其出现次数加1
    if char in char_count:
        char_count[char] += 1
    # 否则，将其添加到字典中，并将其出现次数设为1
    else:
        char_count[char] = 1

# 输出每个字符及其出现次数
for char, count in char_count.items():
    print(f"字符 '{char}' 出现了 {count} 次")
