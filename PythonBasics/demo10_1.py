class Student:
    def __init__(self, student_id, name, gender, dormitory_number, phone_number):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.dormitory_number = dormitory_number
        self.phone_number = phone_number

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def modify_student(self, student_id, name, gender, dormitory_number, phone_number):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.gender = gender
                student.dormitory_number = dormitory_number
                student.phone_number = phone_number
                break

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                break

    def get_all_students_by_name(self):
        sorted_students = sorted(self.students, key=lambda x: x.name)
        return sorted_students

    def get_all_students_by_id(self):
        sorted_students = sorted(self.students, key=lambda x: x.student_id)
        return sorted_students

def display_menu():
    print("欢迎使用学生宿舍管理系统")
    print("功能菜单：")
    print("1. 添加学生信息")
    print("2. 修改学生信息")
    print("3. 查询学生信息")
    print("4. 删除学生信息")
    print("5. 查询全部学生信息（姓名从低到高）")
    print("6. 查询全部学生信息（学号从低到高）")

# 使用示例
if __name__ == "__main__":
    student_system = StudentManagementSystem()

    while True:
        display_menu()
        choice = input("请输入功能对应的数字（1-6），输入 'q' 退出：")

        if choice == '1':
            # 添加学生信息
            student_id = input("请输入学号：")
            name = input("请输入姓名：")
            gender = input("请输入性别：")
            dormitory_number = input("请输入宿舍号：")
            phone_number = input("请输入手机号：")
            student = Student(student_id, name, gender, dormitory_number, phone_number)
            student_system.add_student(student)
            print("学生信息添加成功！")

        elif choice == '2':
            # 修改学生信息
            student_id = input("请输入要修改信息的学生学号：")
            name = input("请输入修改后的姓名：")
            gender = input("请输入修改后的性别：")
            dormitory_number = input("请输入修改后的宿舍号：")
            phone_number = input("请输入修改后的手机号：")
            student_system.modify_student(student_id, name, gender, dormitory_number, phone_number)
            print("学生信息修改成功！")

        elif choice == '3':
            # 查询学生信息
            student_id = input("请输入要查询的学生学号：")
            student_info = student_system.find_student_by_id(student_id)
            if student_info:
                print(f"学生信息：{student_info.name}, {student_info.gender}, {student_info.dormitory_number}, {student_info.phone_number}")
            else:
                print("未找到该学生信息")

        elif choice == '4':
            # 删除学生信息
            student_id = input("请输入要删除信息的学生学号：")
            student_system.delete_student(student_id)
            print("学生信息删除成功！")

        elif choice == '5':
            # 查询全部学生信息（姓名从低到高）
            students_sorted_by_name = student_system.get_all_students_by_name()
            for student in students_sorted_by_name:
                print(f"姓名从低到高：{student.name}")

        elif choice == '6':
            # 查询全部学生信息（学号从低到高）
            students_sorted_by_id = student_system.get_all_students_by_id()
            for student in students_sorted_by_id:
                print(f"学号从低到高：{student.student_id}")

        elif choice.lower() == 'q':
            print("程序已退出，谢谢使用！")
            break

        else:
            print("无效的输入，请输入1到6的数字选择功能或输入 'q' 退出。")
