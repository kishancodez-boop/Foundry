# marks = [10,23,45,43,67,56,34,75,56,90]
# for kishan,mark  in  enumerate(marks): 
#     print(f"the index of mark {mark} is {kishan+1}")
#     if mark == 45:
#         marks.seek(4)
#         print ("this s my fav num")
#         print(marks.tell())

# from functools import reduce


# l=[1,2,3,4,5]
# l1 = list(map(lambda x : x*x , l))
# print(l1)



# l2 = list(filter(lambda x : x> 3 ,l))
# print(l2)


# l3 = reduce(lambda x ,y: x+y , l)
# print(l3)


# a = {1,2,3,4,5}
# b = {1,3,4,2,5}
# print( a is b)
# print( a == b)



# class books:
#     def __init__(self,book1,book2):
#         self.book1 = book1
#         self.book2 = int( book2 )
#         print(f"the book1 and book2 are {self.book1} and {self.book2}\n")
# try:
#     # a = books("kishan's story","the beginning of the all")
#     b = books("haaaaa", 100)
#     c = ()
# except Exception as e:
#     print("enter the books name in string format only")







# def greet(fx):
#     def mfx(*argv,**kwargv):
#         print("hello good morning")
#         result = fx(*argv,**kwargv)
#         print("thank you for using this function")
#         return result
#     return mfx

# @greet
# def sim():
#     print("this is a simple function")
# sim()


# @greet
# def add(a):
#     return a*a*a
# print(add(3))
# print(add(4))
# print(add(5))






# class employee:
#     def __init__ (self ,name,age):
#         self.name = name
#         self.age = age
#     @property
#     def show(self):
#         return self.name,self.age
        
#     @show.setter
#     def show(self,kishan):
#         newname,newage = kishan
#         self.age = newage
#         self.name = newname
# a = employee("kdishan",19)
# print(a.show)
# a.show = ("kishan",18)
# print(a.show)



# class haa:
#     name = "kishan"
#     def __call__(self):
#         return len(self.name)
# e = haa()
# print(e())


# class Vector:
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self,x):
#         return Vector(self.i + x.i , self.j + x.j , self.k + x.k)
# V1 = Vector(1,5,6)
# print(V1)
# V2 = Vector(3,2,8)
# print(V2)
# V3 =V1 + V2
# print(type(V3))
# print(V3)
# K = type(V3)
# print(K)


# class Animal:
#     def __init__(self,species):
#         self.species = species
#     def sound_made_by(self,sound):
#         self.sound = sound
#         return "ikikiki"
# class cat(Animal):
#     def __init__(self,name):
#         self.name = name
#     def sound_made_by(slef):
#         return "meoww"
# a = Animal("cat")
# print(a.sound_made_by(""))
# c = cat("haa")
# print(c.sound_made_by())



# import time
# def whilee():
#     i=0
#     while(i<5000):
#         i=i+1
#         print(i)
# def forr():
#     for i in range(5000):
#         print(i)
# start = time.time()
# whilee()
# end = time.time()
# x = end-start
# start = time.time()
# forr()
# end = time.time()
# print(end-start)
# time.sleep(5)
# print(x)
# time.sleep(10)
# print("kushal was late of 10 seconds")





# import time
# t=time.localtime()
# print(t)
# print(time.strftime("%Y-%m-%d %H-%M-%S-%A-%a",t))


# foods = list()
# while(food := input("enter the foods you like : "))!="quit":
#     foods.append(food)
   
# for i,x in enumerate(foods):
#     print(i,x)
# #     i=i+1
# import shutil
# shutil.rmtree("kishnagfdfg")

# import requests
# x = requests.get("https://google.com")
# print(x.text)    

# def gen():
#     for x in range(200+1):
#         yield x
# g = gen()
# for i in g:
#     print(i)

# from functools import lru_cache
# import time
# @lru_cache()
# def x(n):
#     time.sleep(3)
#     return n*5
# print(x(5))
# print("this is for 5")
# print(x(10))
# print("this is for 10")
# print(x(15))
# print("this is for 15")
# print()
# time.sleep(2)
# print(x(5))
# print("this is for 5")

# import requests
# import json
# query = input("what NEWS do u want")
# url = f"https://newsapi.org/v2/everything?{query}&from=2026-01-23&sortBy=publishedAt&apiKey=API_KEY"
# r = requests.get(url)
# news = json.loads(r.text)
# print(news.type(news)


a={"name":123,"vdwwr":234,"etgbv":765}
for key,values in a.items():
    print(key,values)