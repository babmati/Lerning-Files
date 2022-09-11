# c data types
# print (type(2+4))
# print (4-2)
# print (2*4)
# print (type(4/2))
# print (type({1,2,3}))
# print(type((1,2,3)))
# print(type([1,2,3]))

# Int
# Float
# Bool
# Str
# List
# Tuple
# Set
# Dict

# c example

# print(type('hi hello there 24'))
# username = 'supercoder'
# password= 'supersecret'
# long_string= """
# wow
# o o
# ---
# '''
# """

# print(long_string)
# first_name='Byron'
# last_name='Arias Bonilla'
# full_name= first_name + ' ' + last_name
# print(full_name )

# string concatenation
# print('hello' + 'Byron')
# print('hello'+ ' ' +str(5))
#
# a = str(100)
# b = int(a)
# c = type(b)
# print(c)


# c Escape Sequence
# #c error exampleweather = 'It's sunny'
# weather = "it\'s \"kind of \" sunny"
# weather1 = "\t it\'s \"kind of \" sunny"
# weather2 = 'Hello today is \n sunny'
# print (weather)
# print (weather1)
# print (weather2)

# c #math Functions
# print(round(3.1))
# print (abs(-20)) # returns the absolute of a number

# c operator precedence
# c order is this
# c()   brackets
# c **  power of
# c * /  muliple, division
# c + -  sum, substraction
# print(20+3*4)


# c #data type: complex
# print(bin(5))
# print(int('0b101',2))


# c CONSTANTS= things that are mean
# c never to change
# c Example

# #c selfish[::1] give default start and stop
# #c selfish[::-1] give default start and stop, go backwards

# #example string methods
# hi= "Hola COMO estas"
# print(hi.upper())
# print(hi.casefold())
# print(hi.replace('estas','vas'))


# #booleans
# #can be true or false

# name = 'Byron'
# is_cool= False
# is_cool = True

# #c 0 False 1 True
# print (bool(1))
# print (bool(0))


# type conversion
# name ='Byron Arias'
# age = 50
# relationship_status= 'single'
# relationship_status= 'It\'s complicated'
# print(name+ ' '+ relationship_status)
# print(f"{name} tiene {age-25} años y {relationship_status} ")


# birth_year= input('what year were you born')
# age = 2022- int(birth_year)
# print('Your age is' +' ' + str(age))
# print(f'your age is: {age}')


# password checker

# input()
# input()

# example  print('username {username your }password{*****})is {6} letters long')


# username = input("favor indique su usuario")
# password= input("favor indique su contraseña")
#
# password_lenght = len(password)
# hidden_password = ('*'* password_lenght)



# c  LISTS
# c example
# c  .count(), nos cuenta duplicates en la lista


# c List Slicing
# c  list are mutabble
# amazon_cart =["notebook",
#               "sunglasses",
#              "toys",
#              "grapes"]
# print(amazon_cart)
# print(amazon_cart[0:2])
# print(amazon_cart[0::2])
# print(amazon_cart[::-1])
#
# amazon_cart[0]='Laptop'
# new_cart = amazon_cart[0:3] # if you use range[:] creates a copy and not replace it
# new_cart[0] ='honda'
# print(amazon_cart[0:3])
# print(amazon_cart)
# print(new_cart)
#
# amazon_cart.insert(0,"kawa")
# print(amazon_cart)


# #c  Matrix
# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
#
# print(matrix [0][1], matrix[2][0])


# c build in methods

# c adding
# basket =[1,2,2,3,4,5,5,5,6]
# print(len(basket))
# print(basket)
# new_list = basket.append(100)
# new_list= basket.insert(2,30)
# new_list= basket.extend([300])
# print(basket)

# #c removing

# basket.pop()  # removes the last digits of list
# basket.remove(30)
# print(basket)
# #basket.clear() # removes everything fromthe list
# print(basket)


# print(basket.count(5))
# print(basket.index(5))
# print(basket.index(5 , 0, 6))
# basket_2 = ['a','b','c','d','e','z','s','m']
# print ( 'e' in basket_2) # return true
# print(sorted(basket_2))
# #or
# basket_2.sort()
# print(basket_2)
# basket_2.reverse()
# print(basket_2)

# print (list(range(0,101)))


# sentence ='! '
# new_sentence = sentence.join(['hi','my','name','is','b'])
# print(new_sentence)


# #c Lists unpacking

# a,b,c, *other= [1,2,3,4,5,6,7,8,9]
#
# print(a)
# print(b)
# print(c)
# print(other)

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)


# c None
# weapons = None
# print(weapons)


# #c Dictonaries

# dictionary= {
# 'a':1,
# 'b':2
# }
#
# print(dictionary['b'])
#
# dictionary1= {
# 'a':[1,2,3,4],
# 'b':'Hello',
# 'c': True
# }
#
# print(dictionary1)
#
# # for i in dictionary1.values():
# #     print(i , "\n")

# dictionary2=[
# {
# 'a':[1,2,3,4],
# 'b':'Hello',
# 'c': True
# },
# {
# 'd':[5,6,7,8],
# 'b':'Byron',
# 'c': True
#
# }
# ]
# print(dictionary2[1] ['d'][1] )

#
# user ={
# #names are called keys in dictonaries to access the data
# 'basket': [1,2,3],
# 'greet': 'Hello',
#   'age': 20
# }
#
# user2 = dict(name='By')
# print(user.get('age', 55))
# print(user2)
# print('basket' in user)
#
#
# #c  Dictonaires2
# #method keys check the keys
# print("greet" in user.keys())
# print("Hello" in user.values())
# print(user.pop('age')) # remove the key we indicate
# print(user.items())
# print(user.update({'age':55}))
# print (user)


# c  Tuple are inmmutable lists
# c   only two methods count()  index()

# my_tuple= (1,2,3,4,5,5)
# #also can declare the tuple like this
# x,y,z, *other= (5,6,7,8,9,10)
# print (x , other)
# # my_tuple[1]='z'   can't do this
# print(my_tuple[1])
# print(5 in my_tuple)
# #c   can be slice
# new_tuple = my_tuple[1:3]
# print(new_tuple)
# print(my_tuple.count(5))
# print(my_tuple.index(4))



# c  SET  set

# order collection of unique objects, no duplicates

# my_set= {1,2,3,4,5}
# my_set1= {1,2,3,3,4,4,5,5}
# print (my_set)
# print(my_set1) # will not duplicate the 5
#
# my_set.add(100)
# my_set.add(2)
# print(my_set)

# # we can also use it like this
# new = set(my_set1)
# print(new)
# #or
# print(set(my_set1))# nos devuelve el array como set
# #can't access like this
# #print(my_set[1])  #error
# print (1 in my_set)
# print(len(my_set))
# #c convert into a list
# print(list(my_set)) # converted into a list
# .copy() y .clear()

# c SET methods
# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubnet()
# .isuperset()
# .union()
# print(" vamos a ver set methods")
# my_set2 = {1, 2, 3, 4, 4, 5, 5,7}
# your_set = {2, 3, 6, 8, 8, 9}
#
# my_set3 = {1, 2, 3}
# yours_set = {1, 2, 3, 4, 5, 6,9}
# print(my_set2.difference(your_set))
# #solo imprime la diferencia del q se aplica el metodo osea 1,4,5
# print(my_set2.discard(5)) # remueve el 5
# print(my_set2)
# print(my_set2.difference_update(your_set))
# print(my_set2)

# print(my_set2.intersection(your_set)) # retorna los valores iguales del my_set2
# c  same as intersection
# print(my_set2 & your_set)
# print(my_set2.isdisjoint(your_set))return false xq #c  si tiene en comun


# print(my_set2.union(your_set)) # returns a union set with duplicate removed
# #c  same as union  |
# print(my_set2 | your_set)
# print(my_set2)


# print(my_set2.issubset(your_set))
# print(my_set3.issubset(yours_set))
# #c  this is asking if esta dentro osea contiene lo mismo
# print(my_set3.issuperset(yours_set))
# print(yours_set.issuperset(my_set3))


# c  CONDITIONAL
# c we have True and False
# c Example

# is_old= False
# is_licensed= True
#
#
# if is_old:
#   print("you are old enough to drive!")
# elif is_licensed:
#   print('you can drive now')
# else:
#   print('you are not of age')


# print("okko")

# if is_old and is_licensed:
#   print('you can drive and have a license')


# c  Truthly and Falsy

# is_old= bool(5)
# is_licensed= bool('Hello')
# #c  returns true because if we have the if condition if conver the value into Bool
# print(is_old)
# print(is_licensed)


# c Ternary Operator
# c Example
# c  condition_if_True if condition else condition_if_false

# is_friend= False
# can_message="message allowed" if is_friend else "not allow to message"
# print(can_message)


# c short circuiting

# is_Friend = True
# is_User=  True
#
# if is_Friend or is_User:
#   print('best friends forever')
# print('a' > 'A')
# #c google circuiting
# print(1<2<3<4<5)
# print(1<2<3>4<5)  # return false
# # c we have seen operators
# # c   < > ==  >= <= !=
# # c and or not  key words
# print (not(True))
# print(not (1==1))

# c Excersise

# is_magician = True
# is_expert = True
# c  1-check if magician AND expert: " you are a master magician"
# c   2-check if magician but not expert: "  at leats you're getting there"
# c  3-if you're not a magician: "you need magic powers"


# if is_magician and is_expert:
#   print("you are a master magician")

# elif is_magician and  not is_expert:
#   print("At least you're getting there")

# elif not is_magician:
#   print("You need magic powers")


# print (int == bool)
# #print (10 ==10.0)
# print ([] == [])
#
# print ([] is [])
# print (int is bool)
# print (10 is 10)


# c LOOPS

# c Example for item in "zero to masterry":

# for item in (1,2,3,4,5):  #tuple
#   print(item)

# for item in [1,2,3,4,5]: #list
#   print(item)

# for item in {1,2,3,4,5}: #set
#   print(item)

# for i in (1,2,3,4,5):
#   for x in ('a','b','c'):
#     print(i,x)


# c iterable term
# c  means an object or collection that can be iterate over
# c lists, dictionary, tuple, set, string
# iterate check one by one item


# user = {
#     'name': 'Golem',
#     'age': 5006,
#     'can_swin': False
# }

# for item in user:  # or user.keys() this only print the key of dictonaire
#   print(item)
#
# for item in user.items():  # this return the keys and values
#   print(item)


# for item in user.values():  # this return the values only
#   print(item)


# for item in user.items():
#   key, value = item
#   print(key, value)
# #c or
# for key, value in user.items():
#   print(key, value)

# for item in user.keys():
#   print (item)


# c EXCERCISE
# c counter
# c sum the list
# my_list= [1,2,3,4,5,6,7,8,9,10]
# counter= 0
# for item in my_list:
#   counter+=item
# print(counter)

# c RANGE

# print (range(0,100))
# print(list(range(0,30)))


# for number in range(0,10):
#   print(number)

# for number in range(0,10,2):  # third value step over
#   print(number)
#
# for _ in range(3):
#   print(list(range(10)))


# c ENUMERATE

# for i,char in enumerate("helloooo"):
#   print (i,char)

# for i,char in enumerate([1,2,3,4]):
#   print (i,char)

# for i,char in enumerate({1,2,3,4}):
#   print (i,char)


# for i,char in enumerate(list(range(100))):
#   if char ==50:
#     print(f'index of 50 is {i}')


# c WHILE Loop

# c while condition do something

# i = 0
# while i < 50:
#   i+=1
#   print(i)
#   #c  ifthere was break here it will not print
# else:
#   print('se cumplio la condicion')

# #c when use while or For
# #c
#
# while True:
#   response = input('say something')
#   if(response =='bye'):
#     break


# my_list = [1, 2, 3]

# for item in my_list:
#    #c still thinking for exmple
#   pass    #allows you to pass instead of error

# for item in my_list:
#   print(item)
#   continue

# i=0
# while i < len(my_list):
#    i+=1
#    print(i)


# #c vamos a recorrer la lista Matriz?
# #c vamos a hacer un condicional q la recorra
# def show_tree():
#   picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
#  ]
#   for image in picture:
#    for j in image:

#     if j ==1:
#       print('*', end=' ')
#     else:
#       print(' ', end=' ')
#    print(' ')

# print(show_tree());
# c clean
# c readability
# c predictability
# c Do not repeat your self



# mitad
# for i in list1:
#  if i == ((len(list1)//2)+1):
#   print(10)
#  else:
#    print(i)


# list = [
#     [1, 2, 3, 4, 5, 6, 7],
#     [1, 2, 3, 4, 5, 6, 7],
#     [1, 2, 3, 4, 5, 6, 7],
#     [1, 2, 3, 4, 5, 6, 7],
#     [1, 2, 3, 4, 5, 6, 7],
#     [1, 2, 3, 4, 5, 6, 7]
# ]
# x =(len(list) //2)+1

# # print (x)


# for i in list:
#   for j in i:

#     if ((len(list)//2)+1)==j :
#       print('10', end=' ')
#     else:
#       print(j, end= ' ')
#   print(' ')


# c  EXCERSICEcheck for duplicates in list:

# some_list= ['a','b','c','b','d','m','n','n']


# duplicates=[]

# for i in some_list:
#  if some_list.count(i)> 1:
#    if i not in duplicates:
#     duplicates.append(i)
# print(duplicates)


# #c  FUNCTIONS
# show_tree()

# #c this is called default parameters in function
# def say_hello(name="Anakin", emoji=":-("):
#   print(f'Hello {name}  {emoji}')
#
#
#  #c it is print default parameter but can receive new ones
# say_hello()


# #c can receive default parameters
# def say_some(name,emoji):
#   print(f"Hello {name} {emoji}")

# say_some("Byron",":-)")


# c Arguments are actual values we provide to a function
# c positional arguments
# say_some('Byron', ':-p')
# say_some('Byron', ':-p')
# say_some('Byron', ':-p')

# #c key arguments is bad practice
# say_some(emoji=':-p', name='Byron')

# Lista_amigo= ['wendy','nico', 'ka','ma']
#
# for i in Lista_amigo:
#   say_some(i,':-p')

# #c Example 1
# def sum1(num1, num2):
#   num1+num2
# # c para funcionar necesita un RETURN
# print(sum1(4,3))

# #c Example 2
# def sum(num1, num2):
#    return num1+num2
# # c para funcionar necesita un return
# print(sum(4,3))

# #c Example 3
# def sum2(num1, num2):
#   print("la suma es: ")
#   return num1+num2
# # c para funcionar necesita un return
# print(sum2(4,3))


# EXCERCISE TESTLA CON FUNCTION

# def car_drive(age):
#   if age >= 18:
#     print(f"Ya eres mayor de edad tienes {age} y puedes conducir")
#   else:
#     print(f"No tienes la edad suficiente para conducir apenas tienes {age}")

# Testla = input("me podrias indicar que edad tienes?")
# car_drive(int(Testla))


# c   METHODS VD FUNCTIONS
# c build in
# list()
# print()
# max()
# min(0)
# input()


# c DOCSTRING nos da info de lo q hace la funcion
# c se necesit ''' comment  '''
# def test(a):
#   '''
#    Info: this function test and prints param a
#   '''
#   print(a)


# test('Python Job in Canada')

# c podemos usar help para ver la info de la funcion

# help(test)
# #c or
# print(test.__doc__)


# c
# c  *args= can receive any arguments
# c  **kwargs= this receive keyword args
# def super_func(*args):
#   print(args)
#   return sum(args)
#
# # super_func(1,2,3,4,5)
# print(super_func(1,2,3,4,5))


# def super_func2(*args, **kwargs):
#   total =0
#   for items in kwargs.values():
#     total+= items
#   return sum(args)+ total
#
#
# print(super_func2(1,2,3,4,5, num0= 10, num2=7))

# #c  order for functions=
# #c RULE: params, *args, default parameters, **kwargs
# #c Example

#



# c Excercise
# c create a function called highed_even(list) q va tomar
# c una lista

def higest_even(*args):
    list = []

    for items in args:
        if items % 2 == 0:
            list.append(items)
            list.sort()

    print(list[-1])

  #c tambien se puede usar la funcion max(list)


higest_even(20, 10,8,7,9,11,17,4,3)




# c Walrus Operator   :=
#
# b = 'Helloooooooooo'
# if (len(b)> 10):
#   print(f'too long {len(b)} elements')
#
#
# a = 'Helloooooooooo'
# if ((n := len(a)) > 10): # n is assgined to len of a
#   print(f'too long {n} elements')


# while((n:= len(a)) >1 ):
#   print(n)
#   a = a[:-1]

# print(a)


# c SCOPE - mean what variables do i have access to?
# c  1- Starts with local
# c  2- Parent local?
# c  3- global
# c   4- build in python function
# a= 1
# def parent():
#   a=5
#   def confusion():
#     return a
#   return confusion()
# print(a)
# print(parent())


# c otro ejercicio

# total = 0

# def count():
#   global total#global let use the global variable total
#   total+=1
#   return total

# count()
# print(count())


# c nonlocal keyword


# def outer():
#   x="local"
#   def inner():
#     nonlocal x
#     x="non local"
#     print("inner:", x)
#
#   inner()
#   print("outer", x)
#
# outer()

# x = 5
# print(x)
#
# print(bool("abc"))

## Hello git



























































































































































