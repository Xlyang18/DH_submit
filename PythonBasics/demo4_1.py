def add():
    name = input("请输入姓名：")
    id = input("请输入学号")
    city = input("请输入所在城市：")
    days = input("请输入到校日期")
    studentsData = {"name": name, "id": id, "city": city, "days": days}
    return studentsData

def delData():
    students_dict = {}
    return students_dict
def check():
    i_data = input("输入查询学生姓名：")
    for key, i_data in studentsData.items():
        # 如果键是"name"，则打印值
        if key == "name":
            print(studentsData)

def change():
    name = input("请输入姓名：")
    id = input("请输入学号")
    city = input("请输入所在城市：")
    days = input("请输入到校日期")
    studentsData = {"name": name, "id": id, "city": city, "days": days}
    return studentsData


print("欢迎")
print("2023020131008-刘佳祺")
print("------------")
print("1.添加 2.删除 3.查询 4.修改 5.退出系统")
print("------------")
studentsData= {"name": "刘佳祺", "id": "2023020131008", "city": "武汉", "days": "2023-11-01"}
chose1 = input("输入功能序列：")
if chose1 == "1":
    studentsData = add()
    print("添加成功")
elif chose1 == "2":
    studentsData = delData()
    print("删除成功")
elif chose1 == "3":
    check()
    print("查询成功")
elif chose1 == '4':
    change()
    print("修改成功")
elif chose1 == "5":
    print("退出成功")
    exit()





