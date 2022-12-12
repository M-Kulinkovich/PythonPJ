""""Example simple Class"""


class Dog():
    def __init__(self, name, age):
        """Initialize attributes name and age"""

        self.name = name
        self.age = age
        print('Dog is created')

    def sit(self):
        print(self.name.title() + ' success')

    def jump(self):
        print(self.name.title() + 'jump')


my_dog2 = Dog('fex', 21)
print(my_dog2.name, my_dog2.age)
my_dog2.sit()
print('---------------------------------------------------------------------')
""""--------Example regular expression------------"""
import re

s = "a/a/a/aa/a/fa/fa/af/ds/dg/sdg/dg/vdsb/dfb/df/bsf/bdf/bdf/bsdga/vsd/bs/b/sdv/ds/v"
result1 = re.match('fa', s)  # find in start of line
print(result1)
result2 = re.search('aa', s)  # find first position of symbol in string
print(result2)
result3 = re.findall('sdg', s)  # find symbol and create list
print(result3)
result4 = re.split('/', s)  # разделение строки по ключу в лист
print(result4)
print(len(result4))
result5 = re.sub('a', '12', s)  # replace symbol
print(result5)
result6 = re.fullmatch('a/', s)  # equal or not strs
print(result6)
print('---------------------------------------------------------------------')
""""""""""Regular example""""""""""""

str = '+_I love you --- /// 1000 15 octbr BRAziLisansa'
result1 = re.search(r"\d", str)  # find num
print('1', result1)

result2 = re.search(r"\D", str)  # find symbl
print('2', result2)

result3 = re.search(r"\s", str)  # find backspace
print('3', result3)

result4 = re.search(r"\S", str)  # find symbol too, not backspace
print('4', result4)

result5 = re.search(r"\w", str)  # Num Symbl or _  (Любая цифра, буква или нижнее подчр)
print('5', result5)

result6 = re.search(r"\W", str)  # Все кроме цифры, буквы, нижн подчркв _
print('6', result6)

result7 = re.search(r"\blove", str)  # Начало или конец слова
print('7', result7)

result8 = re.search(r"\Blov", str)  # Проверка стоит ли в середине слова
print('8', result8)

result9 = re.search(r"\d{,3}", str) # не меньше чем повторений  # {1, } <- минимум 1 цифр
print(result9)

result10 = re.findall(r"[lB]\w+", str)

"""""""""""""""""""""""""Lambda function, анонимная функция, однострочная функция"""""""""""""""""""""""""""
print('---------------------------------------------------------------------')
print((lambda a, b: a * b)(12, 1))
print((lambda a, b: a if a > b else b)(25, 11))
print((lambda a: a ** 4)(2))
print((lambda a, b, c: (a + b + c) / 3)(3, 3, 3))
print('---------------------------------------------------------------------')
"""""""""Map filter zip reduce""""""""""'"""
from functools import reduce

a = map(lambda x: x + 15, (2, 4, 5, 12))  # применчет функцию к списку чисел
print(list(a))

a1 = filter(lambda x: (x % 2 == 0), (2, 4, 5, 1, 22))
print(list(a1))

print(reduce(lambda a, b: a * b, (50, 60, 78, 1)))  # перемножает все эл-ты

a = [1, 2, 3, 4, 5, 6, 7, 0]
b = 'abcdefgkl'
result = zip(a, b)  # объеденяет элементы в котреж
print(list(result))
print('---------------------------------------------------------------------')
"""""""""# *args **Kwatgs """""""""""""""""""""


def summ(*args):  # позиционный аргументы
    print(sum(args))


summ(7, 8, 2, 1, 2, 4, 1, 0)


def brands(**kwargs):  # именованные аргументы
    for x, y in kwargs.items():
        print(x, ':', y)


brands(a='apple', s='samsung', c='sitroen')

""""""""""""""  # Generators List SET Dictonary"""""""""""""""""""

print(sum([i ** 3 for i in range(1, 21)]))

s1 = [i ** 2
      if i > 0
      else i ** 3
      for i in range(-10, 10)
      if i % 2 == 0]

print(s1)

se = [7, 8, 9, 12, 11, 22]
sets = {i for i in se}
print(sets)

dict = {i: i ** 2 for i in se}
print(dict)
print('---------------------------------------------------------------------')
""""""""""""  # Вложенные функции и замыкания""""""""""""
# встроенные переменные, зарезервированные
import builtins

print(dir(builtins))
# Глобальные переменные в модуле
y = 2


def diss(x):
    return x ** y


print(diss(4))


# Локальные переменные, создаются и используются внутри функции

def degree(x):
    y = 2
    return x ** y


print(degree(4))


# Mloading
def des(x):
    y = 2

    def des_two():
        return y ** x

    return des_two()


print(des(4))


# encapsulation example
def message(num):
    def print_msg(y):  # print_msg не доступна в глобальной области видимости
        return num, y

    return print_msg


d = message(4)
print(d(5))
# print(print_msg())  -- не видит функцию эту!
""""""""""""""""""""""""""""""""""""""""""
print("-------------------------------------------------------")


################## First Decorator funciton example ############################
def decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')

    return wrapper


def my_func():
    print('Function')


my = decorator(my_func)
my()


################## Second example ############################
def decorator(func):
    def wrapper(x):
        print('start')
        func(x)
        print('end')

    return wrapper


@decorator
def my_func(num1):
    print(num1 ** 2)


my_func(11)
####################### вложенные декораторы #####################
# @decorator1
# @decorator2
# def funct():                                   Как работают вложенные декораторы
#     a = decorator1(decorator2(funct))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""'"""


class Cats():
    def __new__(cls, *args, **kwargs):
        print('__new__')
        return super().__new__(cls)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = 1
        self.y = 2

    def sit(self):
        print(self.name + ' ' + 'is name' + ' ' + str(self.age) + ' ' + 'years old')


myCat = Cats('Max', 11)
myCat.sit()

'"""""""""""""""""""""""""""""" __new__ method Class''''''''''''''''''''''''''''''''' \
 \
 \
    class DataBase:
        __instance = None

        def __new__(cls, *args, **kwargs):
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)
            return cls.__instance

        def __del__(self):
            DataBase.__instance = None

        def __init__(self, user, pasw, port):
            self.user = user
            self.pasw = pasw
            self.port = port

        def connected(self):
            print(f'connection with DB: {self.user}, {self.pasw}, {self.port}')

        def close(self):
            print('Close connection with DB')

        def read(self):
            return 'data on DB'

        def write(self, data):
            print(f'Write data to DB {data}')


db = DataBase('root', '1234', 800)
db1 = DataBase('root', '124124', 8010)
print(id(db), id(db1))
db.connected()
db1.connected()
""""""""""""""""""""""""""  # @classmethod and @ staticmethod""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


class Vector():
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod  # метод класса для работы с атребутами класса
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # Независимая функция от класса
    def norm2(x, y):
        return x * x + y * y


v = Vector(21, 11)
print(Vector.norm2(5, 6))
print(v.get_coord())
""""""""""""""""""""""""""  # Режимы доступа атребутов _ __ """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Hello():
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_core(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('cords do numbers')

    def get_core(self):
        return self.__x, self.__y


pt = Hello()
pt.set_core(12, 20)
print(pt.get_core())
