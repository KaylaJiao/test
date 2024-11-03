#代码首先定义了Person基类和两个继承自Person的子类Teacher和Student。
#然后定义了Course类来表示课程信息和学生管理。
#在主程序中，我们创建了两个课程实例、两个教师实例和三个学生实例，并将学生实例添加到相应课程的学生列表中。
#最后，我们演示了如何在课程中添加和移除学生，并使用show_course_info方法展示了课程、授课教师和选修学生的完整信息。

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

# 实例化
# 创建课程对象
math_course = Course("数学")
physics_course = Course("物理")

# 创建教师对象
math_teacher = Teacher("陈老师", 45, "数学")
physics_teacher = Teacher("王老师", 38, "物理")

# 为课程分配教师
math_course.teacher = math_teacher
physics_course.teacher = physics_teacher

# 创建学生对象
student1 = Student("张三", 16, "高一")
student2 = Student("李四", 17, "高二")
student3 = Student("王五", 16, "高一")

# 将学生对象添加到不同课程的students列表中
math_course.add_student(student1)
math_course.add_student(student3)
physics_course.add_student(student2)

# 功能演示
# 演示如何在课程中添加和移除学生
print("添加学生后的课程信息：")
math_course.show_course_info()
physics_course.show_course_info()

# 移除学生
math_course.remove_student(student3)
print("\n移除学生后的课程信息：")
math_course.show_course_info()