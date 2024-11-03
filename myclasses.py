# 基础类Person的创建
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"姓名：{self.name}, 年龄：{self.age}")

# Teacher类的继承
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        super().introduce()
        print(f"教授科目：{self.subject}")

# Student类的继承
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"年级：{self.grade}")

# Course类的创建与管理
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.teacher = None
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def show_course_info(self):
        print(f"课程名称：{self.course_name}")
        if self.teacher:
            print("授课教师：")
            self.teacher.introduce()
        else:
            print("授课教师：暂无")
        print("选修学生列表：")
        for student in self.students:
            student.introduce()