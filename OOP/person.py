from datetime import datetime

class Person(object): # 从object继承
    # 构造方法,无需return
    def __init__(self,name,age):
        self.name = name # 类属性
        self.age =age

    # 类方法，常用于factory method,类似java的override构造方法
    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name, datetime.now().year - year)

    # 静态方法，常用于utility function
    @staticmethod
    def isAdult(age):
        return age > 18

p1 = Person('Alex',33) #没有new关键字
p2 = Person.fromBirthYear('Tom',1999)
print(p1.age,p2.age)
print(Person.isAdult(22))