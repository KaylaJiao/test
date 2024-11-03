#代码首先定义了Person_t基类和两个继承自Person_t的子类Teacher_t和Student_t。
#然后定义了Course_t类来表示课程信息和学生管理。
#在主程序中，我们创建了两个课程实例、两个教师实例和三个学生实例，并将学生实例添加到相应课程的学生列表中。
#最后，我们演示了如何在课程中添加和移除学生，并使用show_Course_Info方法展示了课程、授课教师和选修学生的完整信息。

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

# 实例化
# 创建课程对象
course_Math = Course_t("数学")
course_Physics = Course_t("物理")

# 创建教师对象
teacher_Math = Teacher_t("陈老师", 45, "数学")
teacher_Physics = Teacher_t("王老师", 38, "物理")

# 为课程分配教师
course_Math.teacher = teacher_Math
course_Physics.teacher = teacher_Physics

# 创建学生对象
student1 = Student_t("张三", 16, "高一")
student2 = Student_t("李四", 17, "高二")
student3 = Student_t("王五", 16, "高一")

# 将学生对象添加到不同课程的students列表中
course_Math.add_Student(student1)
course_Math.add_Student(student3)
course_Physics.add_Student(student2)

# 功能演示
# 演示如何在课程中添加和移除学生
print("添加学生后的课程信息：")
course_Math.show_Course_Info()
course_Physics.show_Course_Info()

# 移除学生
course_Math.remove_Student(student3)
print("\n移除学生后的课程信息：")
course_Math.show_Course_Info()