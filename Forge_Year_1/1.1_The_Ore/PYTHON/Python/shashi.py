# def greet(a):
#     def b():
#         print("good morning")
#         print("how are you?")   
#         a()
#         print("thank you")
#         print("have a nice day")
#     return b

# @greet
# def hello():
#     print("hello kishan")

# hello()
class myclass():
 def __init__(self,v):
     self.value=v
 def display(self):
      return self.value
 @property
 def r(self):
    return  self.value[::-1]
 @r.setter
 def r(self,n):
    self.value=n
 def N(self):
    return self.value

k = myclass("kishan")

print(k.display())
print(k.r)
k.r="hello"
print(k.display())
print(k.r)

