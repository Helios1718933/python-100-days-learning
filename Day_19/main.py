#可见性和属性装饰器
##在很多面向对象编程语言中，对象的属性通常会被设置为私有（private）或受保护（protected）的成员，简单的说就是不允许直接访问这些属性;
##对象的方法通常都是公开的（public），因为公开的方法是对象能够接受的消息，也是对象暴露给外界的调用接口，这就是所谓的访问可见性。;
##例如，可以用__name表示一个私有属性，_name表示一个受保护属性;
class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
#print(stu.__name)  # AttributeError: 'Student' object has no attribute '__name'
#属性__name相当于是私有的，在类的外面无法直接访问，但是类里面的study方法中可以通过self.__name访问该属性。
##用stu._Student__name的方式仍然可以访问到私有属性__name，有兴趣的读者可以自己试一试。

#动态属性
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
stu.sex = '男'  # 给学生对象动态添加sex属性

class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

#对于Student类来说，可以在类中指定__slots__ = ('name', 'age')，这样Student类的对象只能有name和age属性，如果想动态添加其他属性将会引发异常
stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
#stu.sex = '男'

#静态方法和类方法
##静态方法和类方法就是发送给类对象的消息
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod #staticmethod装饰器声明了is_valid方法是Triangle类的静态方法
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod #如果要声明类方法，可以使用classmethod装饰器
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
      

if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter()}')
    print(f'面积: {t.area()}')
else:
    print('无效的边长!!!')

#对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。



#我们可以给上面计算三角形周长和面积的方法添加一个property装饰器（Python 内置类型），这样三角形类的perimeter和area就变成了两个属性，不再通过调用方法的方式来访问，而是用对象访问属性的方式直接获得
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


if Triangle.is_valid(3, 4, 5):
    t = Triangle(3, 4, 5)
    print(f'周长: {t.perimeter}')
    print(f'面积: {t.area}')
else:
    print('无效的边长!!!')

#主要区别就一个：perimeter 和 area 从“方法调用”变成了“计算属性”，调用时不加括号了——t.perimeter 而不是 t.perimeter()，看起来像在访问一个普通属性。
#@property 把方法包装成属性：访问 t.perimeter 时，Python 会自动执行那个函数并返回结果，你感觉不到它是个函数。所以类内部也同步改了——area 里原来是 p = self.perimeter() / 2，现在是 p = self.perimeter / 2（不加括号，取到的已经是算好的值）。
"""
括号 = 执行。 加括号才是调用；不加括号只是拿到对象本身，代码不运行。
python
t.perimeter      # 方法对象（没执行），形如 <bound method ...>
t.perimeter()    # 执行方法，拿到返回值 12
普通方法：必须加括号才会执行；漏了括号是常见 bug。
@property 属性：写 t.perimeter 就自动执行、直接返回值，别再加括号（加了会报 'float' object is not callable）。
类名同理：Triangle 是类本身，Triangle(3, 4, 5) 加括号 = 执行实例化。
记忆点：函数名/方法名/类名 = 菜谱；括号 = 照着做。菜谱放那不出菜，加了括号才动手。
"""

#继承和多态

#基于A类创建B类，A类提供继承信息（父类），B类被继承信息（子类）
##class A:
##class B(A):
##在子类的初始化方法中，我们可以通过super().__init__()来调用父类初始化方法

class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eat(self):
        print(f'{self.name}正在吃饭.')
    
    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生"""
    
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title
    
    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')



stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')