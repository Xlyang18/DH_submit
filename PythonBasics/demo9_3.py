class StudentManagementSystem:
    def __init__(self):
        self.studentsData = {
            "name": "熊路阳",
            "id": "2023020131033",
            "city": "武汉",
            "days": "2023-11-01"
        }

    def add_student(self):
        name = input("请输入姓名：")
        id = input("请输入学号：")
        city = input("请输入所在城市：")
        days = input("请输入到校日期：")
        self.studentsData = {"name": name, "id": id, "city": city, "days": days}
        print("添加成功")

    def del_student(self):
        self.studentsData = {}
        print("删除成功")

    def check_student(self):
        i_data = input("输入查询学生姓名：")
        for key, value in self.studentsData.items():
            if key == "name" and value == i_data:
                print(self.studentsData)
                return
        print("未找到该学生信息")

    def change_student(self):
        name = input("请输入姓名：")
        id = input("请输入学号：")
        city = input("请输入所在城市：")
        days = input("请输入到校日期：")
        self.studentsData = {"name": name, "id": id, "city": city, "days": days}
        print("修改成功")

    def start_system(self):
        print("欢迎")
        print("2023020131033-熊路阳")
        print("------------")
        print("1.添加 2.删除 3.查询 4.修改 5.退出系统")
        print("------------")

        while True:
            choice = input("输入功能序列：")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.del_student()
            elif choice == "3":
                self.check_student()
            elif choice == "4":
                self.change_student()
            elif choice == "5":
                print("退出成功")
                break
            else:
                print("请输入正确的功能序号")


# 创建一个学生信息管理系统对象并启动系统
sms = StudentManagementSystem()
sms.start_system()
