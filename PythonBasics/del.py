# from datetime import datetime
# def get_zodiac_sign(birthdate):
#     month, day = birthdate.month, birthdate.day
#     if 3 <= month <= 5 and day < 21:
#         return "Aries"
#     elif 4 <= month <= 6 and day < 21:
#         return "Taurus"
#     elif 5 <= month <= 7 and day < 22:
#         return "Gemini"
#     elif 6 <= month <= 8 and day < 22:
#         return "Cancer"
#     elif 7 <= month <= 9 and day < 23:
#         return "Leo"
#     elif 8 <= month <= 10 and day < 23:
#         return "Virgo"
#     elif 9 <= month <= 11 and day < 23:
#         return "Libra"
#     elif 10 <= month <= 12 and day < 22:
#         return "Scorpio"
#     elif 11 <= month <= 1 and day < 21:
#         return "Capricorn"
#     elif 1 <= month <= 2 and day < 20:
#         return "Aquarius"
#     else:
#         return "Pisces"
# while True:
#     try:
#         birthdate_input = input("请输入您的出生日期（格式：YYYY-MM-DD）：")
#         birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d")
#         zodiac_sign = get_zodiac_sign(birthdate)
#         print("您的星座是：" + zodiac_sign)
#         print("您的出生年份是：" + str(birthdate))
#         break
#     except ValueError:
#         print("输入的出生日期格式不正确，请重新输入。")

# import numpy as np
#
# # 从文件中加载.npz文件
# data = np.load('国民经济核算季度数据.npz')
#
# # 打印文件中的数组
# print(data.files)

# # 访问数组
# array1 = data['arr_0']
# array2 = data['arr_1']
#
# # 打印数组
# print(array1)
# print(array2)
#
# # 绘制四个饼图
# import numpy as np
# import matplotlib.pyplot as plt
# fig, axes = plt.subplots(2, 2, figsize=(12, 12))
#
# for i, data in enumerate([gdp_data_1, gdp_data_2, gdp_data_1_q4, gdp_data_2_q4]):
#     labels = [f"{industry_labels[j]}: {data[j]}" for j in range(len(industry_labels))]
#     colors = ['#FF9999', '#66B2FF', '#99FF99']
#     explode = (0.1, 0, 0)
#     patches, texts, autotexts = axes[i // 2, i % 2].pie(data, labels=labels, colors=colors, autopct='%1.1f%%',
#                                                           startangle=90, pctdistance=0.85, explode=explode)
#     axes[i // 2, i % 2].set_title(quarters[i])
#
#     for text in texts:
#         text.set(color='black', size=10)
#
#     for autotext in autotexts:
#         autotext.set(color='black', size=10, weight='bold')
#
# # 绘制分组条形图
# gdp_1_q1 = data_1[0][0, :3]
# gdp_2_q1 = data_2[0][0, :3]
# quarters = ["第一个年份", "第二个年份"]
# x = np.arange(len(industry_labels))
# width = 0.35
#
# fig, ax = plt.subplots(figsize=(12, 8))
# bar1 = ax.bar(x - width / 2, gdp_1_q1, width, label=quarters[0])
# bar2 = ax.bar(x + width / 2, gdp_2_q1, width, label=quarters[1])
#
# ax.set_ylabel("国民生产总值")
# ax.set_title("不同年份第一季度国民生产总值")
# ax.set_xticks(x)
# ax.set_xticklabels(industry_labels)
# ax.legend()
# # 添加数据标签
# def add_labels(bars):
#     for bar in bars:
#         height = bar.get_height()
#         ax.annotate(f'{height:.2f}',
#                     xy=(bar.get_x() + bar.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')
#
# add_labels(bar1)
# add_labels(bar2)
#
# plt.show()