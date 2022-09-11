

#c Py charm main.py
#c #SECTION  OOP(Object Oriented Programming)
#c class keyword
#c un paradigma para pensar nuestro codigo y estructurarlo
#c


# class BigObject:
#     pass
# #c  we can create as many objects as needed with instanciating the class
#
# obj1 = BigObject() #instanciate
# obj2 = BigObject() #instanciate
# obj3 = BigObject() #instanciate

# example we are working for wizard company and we need to create a class
#c   __init__  is a dunder method a magic method
#c self keyword  this refers to PlayerCharacter makes it dynamic
#
# class PlayerCharacter():
#     # c Class Object Attribute is called membership is static not dynamic set True for all players
#     membership = True
#
#     def __init__(self, name, age):  # this is a constructor function
#         if (self.membership):
#             self.name = name  # attributes
#             self.age = age
#
#     def run(self):
#         print(f'my name is {self.name}')
#         print("run")
#         return 'done'
#
#
# player1 = PlayerCharacter("Cindy", 21);
# player2 = PlayerCharacter("Tom", 35);
# player2.attack = 50
#
# print(player1)
# print(player1.age)
# print(player2.name)
# print(player2.run())


#c EXCERCISE

#Given the below class:
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
#
listcat = []
cat1= Cat("A", 45)
cat2= Cat("J", 40)
cat3= Cat("C", 30)

listcat.append(cat1)
listcat.append(cat2)
listcat.append(cat3)

list2=[]
#
# for i in listcat:
#     print(i.name, i.age)
#     list2.append(i.age)
#     #print(sorted(list2))
#
#
# print(f"la lista ordenada por edad seria",sorted(list2))
#
#
def Oldest(*args):

    return max(args)
#
#
# print(f' The oldest cat is {Oldest(cat1.age, cat2.age, cat3.age)} years old')
#
#
#

def AgeSort(*args):

    return sorted(args)
#
# print (f"La lista de menor a mayor es:  " , AgeSort(cat1.age, cat2.age, cat3.age))
#
#



#c TOPIC is now methods using @classmethod

class PlayerCharacter():
    # c Class Object Attribute is called membership is static not dynamic set True for all players
    membership = True

    def __init__(self, name, age):  # this is a constructor function
        if (self.membership):
            self.name = name  # attributes
            self.age = age


    def run(self):
        print(f'my name is {self.name}')
        print("run")
        return 'done'


    def speak(self):
        print(f"my name is {self.name} and i am {self.age} years old")

    @classmethod
    def adding_things(cls,num1,num2):  #c this cls is like self in class
        return cls('Teddy', num1+num2) # this cls instanciate PlayerCharacter
        #return num1+num2

    @staticmethod   # diference is can not instanciate the class
    def adding_things1(num1, num2):
        return num1+num2

player1 = PlayerCharacter("Cindy", 21)
player2 = PlayerCharacter("Tom", 35)
player3 = PlayerCharacter("Byron", 35)

#
# player2.speak()
player1 = PlayerCharacter("Cindy", 21);
#
#print(player1.adding_things(4,3))  # classmethod can be use without instanciating a class
#
# print(PlayerCharacter.adding_things(5,5)) # is a method of the class
#
player3 = PlayerCharacter.adding_things(2,3)
# print(player3.age)
#


#c 4 pilar of OOP(object Oriented Programming)
#c the idea of ENCAPSULATION , methods an attributes inside the class, multiple objects

#c ABSTRACTION, don't know how method was use just need to implement like call  .count len()
#c  Dont know how those method are build just implement them is abstraction, PRIVATE AND PUBLIC VARIABLE IS PART OF IT

#c INHERITANCE, allow new object to takes properties of existing objects so you can inheritance clases


#c POLYMORPHISM  means many forms, can share same methods but different on what object calls it




class User():

    def __init__(self, email):
        self.email = email


    def sign_in(self):
        print('logged in')

    def powering(self):
        if self.power:
            if self.power >20:
              print("el poder es mayor a 20 puede entrar en batalla")
            else:
                print(f"tiene un poder de apenas {self.power} y necesita entrenar")




class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self,  email) # we called the init method of User inside Wizard to have email
        #super().__init__(email)  # or we can use super and remove the self, same results
        self.name = name
        self.power = power

    def attack(self):
        print(f"atacking with the power of {self.power}")

    def run(self):
        print("run really fast")


class Archers(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"{self.arrows} remaining")

    def attack(self):
        print(f"attacking with arrows: arrows left - {self.arrows}")


#c this is multi inheritance take properties from all these objects
class HybridBorg(Wizard, Archers, User):
    def __init__(self, name, power, arrows, email):
        Archers.__init__(self, name, arrows)
        Wizard.__init__(self, name, power, email)
        User.__init__(self, email)


# hb1 = HybridBorg("borgie", 50, 60,"hb1@gmail.com")

# print(hb1.check_arrows())
# print(hb1.attack())
# print(hb1.sign_in())
# print(hb1.powering())





# wizard1 = Wizard("Merlin", 30,  "merlin@gmail.com" )
# arquero1 =Archers("robin", 80)


# wizard1.attack()
# arquero1.attack()
# print(wizard1.email)
# # print(wizard1.sign_in())
# # print(isinstance(wizard1, Wizard))  # returns True
# # print(isinstance(wizard1, User))    # returns True
# # print(isinstance(wizard1, object))   # returns True   because it question if is instance of an object
# # print(wizard1.powering())
#
# #c Introspection
# print(dir(wizard1))   # is a dunder method,return special methods


#c polymorphism

def player_attack(char):
    char.attack()

# player_attack(wizard1)
# player_attack(arquero1)
# for char in [wizard1, arquero1]:
#     char.attack()



 #x EXCERCISE OF PRACTICE


class Pets():
    animals= []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy= True

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def walk(self):
        return f"{self.name} is just walking around"


class Simon(Cat):

    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):

    def sing(self, sounds):
        return f'{sounds}'


class Psss(Cat):

    def sing(self, sounds):
        return f'{sounds}'


# your_cats =[]
#
# cat_simons = Simon("Simon", 20)
# cat_sally = Sally("Sally", 19)
# cat_psss = Psss("Psss", 25)
#
# your_cats.append(cat_simons)
# your_cats.append(cat_sally)
# your_cats.append(cat_psss)
#
#
# my_pets = Pets(your_cats)

# print(cat_psss.age)
# print(my_pets.walk())
# print(cat_psss.sing("shhhhhhhh"))
# print(cat_simons.sing("shhhhhhhhh"))
# print(cat_sally.sing("shhhhhhhhh"))







class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age= age


    def __str__(self):  # we are modifying a dunder method
        return f"{self.color}"


    def __len__(self): # another example change dunder method to return 5 but will work with this
        return 5       #object only


action_figure  = Toy('red', 0)

# print(action_figure.__str__())
# print(str(action_figure))
# print(len(action_figure))


class SuperList(list):
    def __len__(self):
        return 1000

# super_list1 = SuperList()

# print(len(super_list1))
# super_list1.append((5))
# super_list1.append(10)
# print(super_list1[0])
# print(super_list1[1])
#
# print(issubclass(SuperList, list))
# print(issubclass(list, object))



#c MRO - Method Resolution Order
#c is the order in which thing are resolved


class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,C):
    pass

# print(D.num)
#
# print(D.mro())

#c Example
# defined the order but Python over rule this staff with algorithm(Depth First Search)
class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass
# print(M.__mro__)
# #or
# print(M.mro())



#C SECTION  Advanced Python: Functional Programming
#c Pure Function, separation of data
#c 2 rules 1-) same input return same output, 2-) will not produce side effects to code#
#c example

# def multiply_by2(li):
#     new_list=[]
#     for  item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1, 2, 3]))



#functions we are going to check
#c map, filter, zip and reduce            SEE THIS SECTION received iterable no matter what it is

#map allow to simplify code
# my_list =[1, 2, 3]
# def multiply_by1(item):
#     return item*2
#
# my_list2= ["b@gmail.com","a@gmail.com","m@gmail.com "]
#
# def mayuscula(item):
#     return item.capitalize()



# print(list(map(multiply_by1,[1,2,3])))
#or
# print(list(map(multiply_by1, my_list)))
# print(list(map(multiply_by1, {5,10,15}))) # acepta cualquier iterable
# print(my_list)
# print(list(map(mayuscula, my_list2)))


#c Filter method
# my_list3 =[1, 2, 3]
# def only_odd(item):  # esta funcion nos filtra si el numero es odd or no
#     return item % 2 != 0

# print(list(filter(only_odd, my_list3))) # filter needs function


#c Zip method
your_list= [10, 20, 30]
# print(list(zip(my_list3, your_list)))  # combine list together as many as need and zip together, no need of function



#c Reduce method
#c is not build in we have to use import it




from functools import reduce

# def accumulator(acc, item):
#     print(acc, item)
#     return acc+item
#
#


# print(reduce(accumulator, my_list3, 0))  #return the accumulator 0 means where the accumulator is going to start


## EXCECISE DE FUNCIONES  map, filter, zip and reduce


from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def A(items):
    return  items.capitalize()


# print(list(map(A, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_string = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# print(list(zip(my_string, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def B(items):
    return items > 50

# print(list(filter(B,scores)))


#4 Combine all of the numbers that are in a list on this file using reduce
# # (my_numbers and scores). What is the total?

def accumulator(acc, item):
     print(acc, item)
     return acc+item


# print(reduce(accumulator, (my_numbers+ scores)))





# lambda expressions
#
# mys_list =[1, 2, 3]
#
# print(list(map(lambda item: item*2, mys_list)))  #similar to function multiply_by2 but not needed with lambda
#
# print(reduce(lambda acc, item: acc+item, mys_list))
#

#excercise

# hacer un ejercicio en lambda q retorne un
#square
# mysi_list= [5,4,3]
# # print (list(map(lambda item: item**2, mysi_list)))
#
#
# #List Sorting
#
# a= [(0,2) , (4,3), (9,9), (10,-1)]
#
# a.sort(key=lambda x: x[1])
# print(a)


# list, set, dictionary
# easy way to create iterables

#EXample code my_list4 =[param for param in iterable]
#
# my_list4 = [char for char in 'Hello']  # can also turn into sets{}
# my_list5= [num for num in range(0,100)]  # can also turn into sets{}
# my_list6=[num*2 for num in range(0,100)]   # can also turn into sets{}
# my_list7 =[num**2 for num in range(0,100) if num % 2 ==0]   # can also turn into sets{}

# print(my_list4)
# print(my_list5)
# print(my_list6)
# print(my_list7)


#EXAMPLE  with dictionaries
simple_dict = {
    'a' : 1,
    'b' : 2
}
# my_dict= {key:value**2  for key,value in simple_dict.items() if value%2 == 0}
# print(my_dict)
#
# my_dict1= {num: num*2 for num in [1, 2, 3]}
# print(my_dict1)


# practice excersice find duplicate with comprenhentions
# some_list= ['a', 'b', 'b', 'c','c', 'd', 'e']
# listing =[]
# duplicates = list(set(char for char in some_list if some_list.count(char)>1)) # i also use {}
# print(duplicates)



# DECORATORS  Pattern  key term in python
#  @classmethod @staticmethod   start with@
# funstion are call like first class citizens

# def hello():
#     print('Helllllooooooooo')
#
# greet= hello()
# print(greet)
# #or
# greet = hello
# print(greet())

# higher order function

# def helo(func):  # is a function that accepts as parameter another function
#     func()
#
# def greet1():
#     def func():
#         return 5
#     return func()
#
#
# # we wil now see what DECORATOR Pattern  is, supercharges our function inhance a function
#
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('**********')
#         func(*args, **kwargs)
#         print('**********')
#     return wrap_func
#
# @my_decorator
# def hello():
#     print('Helllloooo')
# hello()
#
# @my_decorator
# def bye():
#     print('see ya later')
# bye()
#
# #or we can do this but is not neccesary that why we use the @ for the decorator
# hello2= my_decorator(hello)
# hello2()
#
# #other example
# @my_decorator
# def he(greeting):  #to fix this we need parameter in wrap funt
#     print(greeting)
#
# he("Helloooo")
#
# def h(greeting, emoji= ":("):
#     print(greeting, emoji)
#
# h('Hi ')


# vamos a programar un performance decorator para ver q tan rapido mi code runs


from time import time



# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1= time()
#         result = fn(*args, **kwargs)
#         t2= time()
#         print(f'it took {t2-t1} s')
#         return result
#     return wrapper
#
# @performance # this is a decorator to see how my code is running time wize
# def long_time():
#     for i in range(100000000):
#         i*5

# long_time()


#EXCERCISE
# Create an @authenticated decorator that only allows the function to run is user1
# has 'valid' set to True:
user1 = [ {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
},
    {
    'name': 'Sorna',
    'valid': False

    }
]

def authenticated(fn):
    def wrapper(*args,**kwargs):
        if [i for i in user1 if i['valid']]:
        #if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('NO se puede correr')


    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)


# Error handling in Python

#TypeError:

#we can use Error Handling
# commun

# while True:
#   try:  #key
#      age = int(input("Hello what is your age?"))
#      10/age
#   except ValueError:   #key
#     print('please enter a number')
#   except ZeroDivisionError:
#     print('please enter age higher than 0')
#   else:  #key
#       print('Thank you')
#       break
#   finally:   #key
#       print('ok, iam finally done')

# can also use this code ( raise Exception or raise ValueError('Hye print this error ')  )
# this inside the try

def sum(num1, num2):
    try:
        return num1+num2
    except TypeError as err:
        print(f'Something is wrong {err}')

# print((sum("1",2)))



def sum1(num3, num4):
    try:
        return num3/num4
    except (TypeError, ZeroDivisionError)as err:
        print(f"ooops  {err}")

# print((sum1(1,2)))





#c  GENERTORS
#iterable
#iterate
# generators are iterable
# range is a generator


range(100)
list(range(100))

def make_list(num):
    result=[]
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
# print(my_list)


# we are going to define our own generator

def generator_function(num):
    for i in range(num):
        yield i   #keyword yield this instead of returning, pause the function and when told to keep going
                  # will continue
#
g= generator_function(100)
# next(g)  # this call the generator and iterate once
# print (g) # this return the generator object
# for item in generator_function(1000):
#     print(item)



#IMPORTANCE  od generators

def performance(fn):
    def wrapper(*args, **kwargs):
        t1= time()
        result = fn(*args, **kwargs)
        t2= time()
        print(f'it took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(10000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5

# long_time()
# long_time2()


# this is how for loop works

def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            next(iterator) #if i want to see valie print this line
        except StopIteration:
            break

# print(special_for([1, 2, 3]))

# this is how range work

class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last= last


    def __iter__(self):  ## this dunder allow me to iterate in my function
        return self

    def __next__(self):     ## this allow me to use netx in my function  which for loop needs
        if  MyGen.current< self.last:
            num= MyGen.current
            MyGen.current+=1
            return num
        raise  StopIteration

gen = MyGen(0,100)

# for i in gen:
# #     print (i)


#
# def fib(number):
#         value =0
#         total=1
#
#         for i in range(number):
#            yield value
#            temp= value
#            value = total
#            total = temp+total
#
# for x in fib(21):
#     print(x)
#
#
#
#
def fib2(number):
    a =0
    b=1
    result =[]
    for i in range(number):
        result.append(a)
        temp=a
        a=b
        b=temp+b

    return result
#
# print(fib2(21))



## MODULES
## How to Organize Code
# how to use the utility module in main.py
import utility

print(utility.multiply(4,5)) # we have exported here the utility function if we need to


import shopping.shopping_cart  ## this eill import package like folder name first.file name

print(shopping.shopping_cart.buy('apple'))

## Created a Project modules to see modules topic

# now more ways to import a package

## we are going to see main  in the module project


## The POwer of Python -- has a package system we can borrow, build in modules
# Python organization you can go to documentation  and go to global modules to find them all
#can check Python module for specific software
# we will test random build in modules

# import random
# # can also use this to import the method
# #import random as oulala and call the method with this name
#
# # print(random) # will return theinfo of the module we are importing
# # help(random)  ##this will tell what the method does and info
# # print(dir(random)) ## this will show me all methods we have available
# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1,2,3,4,5]))
# my_list=[1,2,3,4,5]
# random.shuffle(my_list)
# print(my_list)

#
# import sys

# sys.argv  # this let use in console and run another py file


##wwe will now learn how to install other packages that have been use by other developers, found in pypi
## in the modules project






#C SECTION  Advanced Python: Functional Programming





##### we are going t check usefull modules found in Python Module Index

from collections import Counter, defaultdict, OrderedDict

# li= [1,1,2,3,4,5,6,7,7]
# sentence= 'bla bla bla bla thinking about python'
# print(Counter(li))
# print(Counter(sentence))
#
#
# dictionary= defaultdict(lambda : 'does not exist',{'a': 1, 'b':2})
# print(dictionary['b'])

# d = OrderedDict()
# d['a']= 1
# d['b']= 2
# #  Python has made Dictionaries ordered by default!,,you no longer need to use ordered dict,
# d2= OrderedDict()
# d2['a']= 1
# d2['b']= 2
#
# print(d2 ==d)
#
#
# import datetime
#
# print(datetime.time(5,45,42))
# print(datetime.datetime.now())
# print(datetime.date.today())
#
#
# from array import array
#
# arr= array('i', [1,2,3])
#
# print(arr)


##### Fundamentals Pros and Cons of libraries
# not always good to use packages, created by developers, could be buggy, has to be popular in pypi



###### debugging
# we want to use linting(allow us to detect isues with out code) included in pycharm
# example
#num+4
# use ide/ editor
# be able to read errors
#Use pdb(python debugger) is a build in module
#pdb type help to see all
# step= allow to move forward one line
# a= return the arguments values
# w= gives the context of current line executing
# exit= to get out
#next = let me move to next

import pdb
def add(num1, num2):
    #print(num1, num2)
    # pdb.set_trace() ### allow you to interact in console like type num1 or num2
    #in the console when pdb can type help to see commands, example help list
    t=4*5
    return num1+num2

# print(add(4,5))




####### File I/O
# we run this in Visual Studio this video pratice
#stands for input/output
# created a test file in the desktop
# with open('test.txt', mode='r+w') as my_fyle:  # r for read, w for write, a for append to end
#     text = my_fyle.write('hey it\'s me!')
#     print(my_fyle.readline())
#
# my_fyle.close()
#
# ####### File I/O
# #stands for input/output
# # # created a test file in the desktop
# # my_file= open('test.txt')
# # print(my_file.readlines())
#
# # my_file.close()
#
# with open('test.txt', mode='r') as my_file:    # w for write, r for read, a for append
#      print(my_file.readlines())
#     # text = my_file.write('Logramos file class')
#     # print(text)


##CMD commands
## cd folder name to get inside
# cd .. to move out of folder
#mkdir to create a file or folder    cambiamos la direcion when opening file /


#####Handle Errors  in IO
# try:
#
#     with open('app/test.txt', mode='x') as my_file:    # w for write, r for read, a for append
#       print(my_file.readlines())
# except FileNotFoundError as err:
#     print('Files doesn\'t exist')
#     raise err
# except IOError as err:
#     print('Files doesn\'t exist')
#     raise err




#####Translate excercise
## we have to download  translate 3.6.1
# pip install translate

# from translate import Translator
#
# translator = Translator(to_lang="ja")
#
# try:
#
#     with open('app/test.txt', mode='r') as my_file:  # w for write, r for read, a for append
#         text = my_file.read()
#         translation = translator.translate(text)
#         print(translation)
#         with open('app/test-ja.txt', mode='w', encoding="utf-8") as my_file2:
#             my_file2.write(translation)
# except FileNotFoundError as e:
#     print('Check the file path silly')
#
# with open('app/test-ja.txt', mode='r', encoding="utf-8") as my_file:  # w for write, r for read, a for append
#
#     print(my_file.readline())




#######Regular Expressions

import re

pattern = re.compile('this')

string= 'search this inside of this text please'

print('search' in string)
#hot to use instead of this

# print(re.search('this',string))
a = re.search('this',string)
print(a.span())  # return positions in the string as a tuple
print(a.start()) # return start position
print(a.group()) # return the pattern if found
print(a.end()) # return position end in string

a = pattern.search(string)
print(a.group()) # return the pattern if found
b = pattern.findall((string)) # return all patterns in the string
print(b)
c= pattern.fullmatch(string) # we would need to have the whole string to compare re.compile('full string')
print(c)

