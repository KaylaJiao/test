# 基础类Person_t的创建
class Person_t:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introDuce(self):
        print(f"姓名：{self.name}, 年龄：{self.age}")

# Teacher_t类的继承
class Teacher_t(Person_t):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introDuce(self):
        super().introDuce()
        print(f"教授科目：{self.subject}")

# Student_t类的继承
class Student_t(Person_t):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introDuce(self):
        super().introDuce()
        print(f"年级：{self.grade}")

# Course_t类的创建与管理
class Course_t:
    def __init__(self, course_name):
        self.course_name = course_name
        self.teacher = None
        self.students = []

    def add_Student(self, student):
        self.students.append(student)

    def remove_Student(self, student):
        self.students.remove(student)

    def show_Course_Info(self):
        print(f"课程名称：{self.course_name}")
        if self.teacher:
            print("授课教师：")
            self.teacher.introDuce()
        else:
            print("授课教师：暂无")
        print("选修学生列表：")
        for student in self.students:
            student.introDuce()