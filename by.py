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
# print(f"la lsita ordenada por edad seria",sorted(list2))
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
# print(player1.adding_things(4,3))  # classmethod can be use without instanciating a class
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


hb1 = HybridBorg("borgie", 50, 60,"hb1@gmail.com")

# print(hb1.check_arrows())
# print(hb1.attack())
# print(hb1.sign_in())





wizard1 = Wizard("Merlin", 30,  "merlin@gmail.com" )
arquero1 =Archers("robin", 80)


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


your_cats =[]

cat_simons = Simon("Simon", 20)
cat_sally = Sally("Sally", 19)
cat_psss = Psss("Psss", 25)

your_cats.append(cat_simons)
your_cats.append(cat_sally)
your_cats.append(cat_psss)


my_pets = Pets(your_cats)

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

super_list1 = SuperList()

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

print(D.num)

print(D.mro())

#c Example
# defined the order but Python over rule this staff with algorithm(Depth First Search)
class X: pass
class Y: pass
class Z: pass
class A(X, Y): pass
class B(Y, Z): pass
class M(B, A, Z): pass
print(M.__mro__)
#or
print(M.mro())



