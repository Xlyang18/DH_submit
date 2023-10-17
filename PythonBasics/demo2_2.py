from datetime import datetime

# 获取用户输入的生日日期
birthday_str = input("请输入您的生日（格式：年-月-日，例如：2000-01-01）：")

# 将生日日期字符串转换为日期对象
try:
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d")
except ValueError:
    print("输入的生日格式不正确，请按照年-月-日的格式输入。")
    exit()

# 判断输入日期的合法性
if birthday > datetime.now():
    print("输入的生日晚于当前日期，请输入一个正确的生日日期。")
    exit()

# 根据星座的规则输出用户的星座信息
if birthday.month == 12 and birthday.day >= 22:
    constellation = "摩羯座"
elif birthday.month == 1 and birthday.day <= 19:
    constellation = "水瓶座"
elif birthday.month == 2 and birthday.day <= 18:
    constellation = "双鱼座"
elif birthday.month == 3 and birthday.day <= 20:
    constellation = "白羊座"
elif birthday.month == 4 and birthday.day <= 19:
    constellation = "金牛座"
elif birthday.month == 5 and birthday.day <= 20:
    constellation = "双子座"
elif birthday.month == 6 and birthday.day <= 20:
    constellation = "巨蟹座"
elif birthday.month == 7 and birthday.day <= 22:
    constellation = "狮子座"
elif birthday.month == 8 and birthday.day <= 22:
    constellation = "处女座"
elif birthday.month == 9 and birthday.day <= 22:
    constellation = "天秤座"
elif birthday.month == 10 and birthday.day <= 23:
    constellation = "天蝎座"
elif birthday.month == 11 and birthday.day <= 21:
    constellation = "射手座"

# 输出用户的星座信息
print(f"您的星座是：{constellation}")
