from myclasses import Course_t, Teacher_t, Student_t
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