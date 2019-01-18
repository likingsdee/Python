
"""
定义一个学生类，用来形容学生
"""
# 定义一个空类
class Student():
    name = None
    age = 16
    __littleName = None
    def say(self):
        self.name = "xingchen"
        self.age = 22
        print("My name is {0}".format(self.name))
        print("My age is {0}".format(self.age))
        return None
    def sayAgain(self):
        print("{0}".format(__class__.name))
    def __getattr__(self, item):
        print("{0}属性未找到".format(item))

class Animel():
    def __init__(self):
        print("I am a Animel")



class PaxingAni(Animel):
    def __init__(self,name):
        print("I am a PaxingAni {0}".format(name))




class Dog(PaxingAni):
    # _init_就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print("I am init in dog")

class Cat(PaxingAni):
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
#基类，人
class Peraon():
    name = None
    age = 18
    gander = "man"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sleep(self):
        pass

class Teacher(Peraon):
    pass
# 实例化一个叫yueyue的学生
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
yueyue.doHomework()
print(PythonStudent.__dict__)
xingchen.say()
Student().say()
print(Student.__dict__)
print(Teacher.__dict__)
D = Dog()
C = Cat("cat")
print(xingchen.addr)