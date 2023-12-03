# # hello
# print('Hello')
# print(1,2,3, sep='-', end='\n')
# # end='\n' перенос строки
##==============================================
# i=3
# print(type(i))
# f=2.3
# print(type(f))
# b= True
# print(type(b))
# s='text'
# print(type(s))
# n=None
# print(type(n))
#
# a=b=v=4
# print(a, b, v)
##==============================================
# # претворити рядок в чмсло, якщо там цифра
# num = '22'
# int1=int(num)
# print(type(int1))
##==============================================
# a=0
# a+=1
# b=2
# print('a =',1)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b) #запише те що ціле
# print(a%b) #остача від ділення
# print(4**b) # степінь
# print(456**98)
##==============================================
# # щоб вивело рядок , повертає стрінгу
# num = input('Enter number:')
# print(num)
##==============================================
# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a==b) # print(a is b)
# print(a!=b) # print(a not is b)
##==============================================
# # чи належить до якогось типу
# a='ss'
# print(isinstance(a, int))
##==============================================
# num=input('Enter num: ')
# num=int(num)
#
# if num > 5:
#     print('Yes')
# elif num == 5:  #els if
#     print('=')
# else:
#     print('no')
# # тернарник
# res = 'yes' if num>5 else 'no'
##============================================== списки
l=[1,2,3,4,5]
l2=[7, 55]
# print(l[-2]) #4
# l[2]=34 #замінити
# del l[3]
# print(len(l)) #lengs
# l.append(7) #add in and arr
# l.insert(2,66) #66 стане на місце 2 індексу і все посунеться
# l.pop() #видаляє 1 елемент з кінця і його повертає
# l.pop(3)
# l.remove(4)  #видаляє по значенню, перше знайдене
# l+=l2 #concat
# l.index(4)
# l.reverse() #змінює список
# l.sort()
# l.sort(reverse=True) #сортує в зворотньому порядку
# l.count(7) # скільки 7 в масиві
#
# l3 =l.copy() # копіювати, якщо є вкладеності, то зробить посилання
# sub = l[0,4] #split
# sub1 = l[:5] # до 5 індекса
# sub2 = l[:5:2] # до 5 індекса кожен другий
# sub3 = l[:2] # кожен другий
##============================================== кортежі не змінюються
# my_tuple =(1,2,3,4,2)
# print(my_tuple[3])
# print(my_tuple.count(2))
# print(my_tuple.index(3))
# asd = type(l) # список в кортеж
##==============================================  list of airports
# airports = [
#     ("O’Hare International Airport", 'ORD'),
#     ('Los Angeles International Airport', 'LAX'),
#     ('Dallas/Fort Worth International Airport', 'DFW'),
#     ('Denver International Airport', 'DEN')
# ]
#
# for airport in airports:
#     (airport_name, code) = airport
#     print('The code for {0} is {1}.'.format(airport_name, code))

##============================================== словники
# dictionary = {
#     # my_tuple:'Max',
#     'age': '33',
#     'status': 'True'
# }
# print(dictionary['age']) #якщо викликати чого немає, то впаде помилка
# get = dictionary.get('name', 'not name') #якщо викликати чого немає, то поверне деолтне значення, або можна не вказувати, тоді нан
# print(get)
# del dictionary['status']   #del
# dictionary.pop('age')  #del

# print(dictionary.items()) # [((1, 2, 3, 4, 2), 'Max'), ('age', 33), ('status', True)]
# print(dictionary.keys()) #[(1, 2, 3, 4, 2), 'age', 'status']
# print(dictionary.va  lues()) #['Max', 33, True]
# dictionary.popitem() #del last writed
# dictionary.setdefault('adress', 'dnipro') # створить запис, якщо такий ключ є пропустить
# dictionary_2 = {
#     'adress': 'Lviv',
#     'home': '34'
# }
# dictionary.update(dictionary_2) #concate
# print(dictionary)

# contacts = {
#     'Json': ['123-45-67', '098-76-54'],
#     'Cat': '567-89-01'
#     }
#
# if 'Json' in contacts.keys():
#     print("Json's phone number is:")   #Json's phone number is:
#     print(contacts['Json'][0])         #123-45-67
#
# print('567-89-01' in contacts.values()) #True
# #--------------------------------
# for person, phone in contacts.items():
#     print('The number for{0} is{1}'.format(person, phone))
#     #The number forJson is['123-45-67', '098-76-54']
#     #The number forCat is567-89-01
##==============================================  facts dictionary
# def printInfo(peopleFact):
#     for person in pipel:
#         print('{0} : {1}'.format(person, pipel[person]))
#
# pipel = {
#     'Jeff': 'Is afraid of clowns',
#     'David': 'Plays the piano',
#     'Jason': 'Can fly an airplane'
# }
# printInfo(pipel)
# pipel['David']='Plays the gitar'
# pipel['Jill']= 'Can hula dance'
#
# print('-'*15)
# printInfo(pipel)
##============================================== set значення без дублівб неможна взяти по індексу
# l= [1,2,3,4,1,1,3]
# s_1 = set(l)  #{1, 2, 3, 4}
# s_1.add(5)  # додати значенняб тільки якого немає в сеті
# s_0 = set() # пустий сет
# print(s_0)
# set_2 = {1,2,3}
# s_1.issuperset(set_2) # чи 2 належить 1
# s_1.issubset(set_2)  # чи 1 належить 2
# s_1.isdisjoint(set_2)  # чи значення всі різні
# s_1.union(set_2)  # оюєднати, створить новий
# s_1.update(set_2)  # обєднати, змфнить 1
# s_1.intersection(set_2)  # виведе спільне
# s_1.symmetric_difference(set_2)  # виведе не спільне
#
# s_1.remove(32) # видалить, немає помилка
# s_1.discard(22) # видалить, немає пропустить
# s_1.pop() # видалить рандомно
##============================================== string 'ddd', "hjkj"
# stars = '?'*8 #????????
# name='Max'
# age=12
#
# string = 'Hello my name ai '+ name + ', I\'m ' + str(age)
# print(string)
##============================================== to_do_list
# to_do_list = []
# finished = False
# while not finished:
#     task = input('Enter a task for your to do list.')
#     if len(task) == 0:
#         finished =True
#     else:
#         to_do_list.append(task)
#         print('Task added.')
#
#     print()
#     print('Your To-Do List:')
#     print('-'*20)
#     for task in to_do_list:
#         print(task)
##============================================== file
# file = open('filex.txt')
# file.read() # read
# file.rstrip() # read
# file.seek(0) # start file
# file.seek(5)   # 5 bites file
# file.tell()   # position file
# file.close()
# # /r          # end line
# # /n          # start new line
# with open('filex.txt', 'w') as file_write:
#     file_write.write('new line info')  # remove old info and write new
# with open('filex.txt', 'a') as file_write:
#     file_write.write('\nnew line info\r')  # add new info
# with open('filex.txt') as file:
#     line_number = 1
#     for line in file:
#         print('{0}: {1}'.format(line_number, line.rstrip()))
#     line_number += 1
# animals = []
#
# with open('animals.txt', 'r+') as file:
#     for line in file:
#         animals.append(line.strip())
#     animals.sort()
#     file.seek(0)
#     file.truncate()
#     file.seek(0)
#     for animal in animals:
#         file.write(animal+'\n')
#
#
# print(animals)
##============================================== class
class ItSpecialist:
    def __init__(self, name, speciality, salary):
        self.name = name
        self.speciality = speciality
        self.salary = salary
    def tell_about_yourself(self):
        return f'Hi! My name is {self.name}. I\'m a {self.speciality}. My salary is {self.salary}'

carl = ItSpecialist('Carl','DA',120)
print(carl.tell_about_yourself())
