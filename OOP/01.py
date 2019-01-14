
"""
定义一个学生类，用来形容学生
"""
# 定义一个空类
class Student():
    pass

# 实例化一个对象
xingchen =Student()

# 再定义一个类，用来描述听Python课的学生
class PythonStudent():
    # 不确定的值使用None赋值，否则报错
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进
    # 2. 系统默认一个self参数
    def doHomework(self):
        print("在做作业 ")

        # 推荐在函数末尾使用return
        return None

# 实例化一个叫yueyue的学生
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()