# def factorial(n):
#     if n == 0 or n == 1:
#         return (1)
#     else:
#         return n*factorial(n-1)
# print(factorial(int(input("Enter the number to find the factorial : "))))


# def Fibonacci(n):
#     if n <= 0:
#         return "Incorrect / invalid input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(int(input("Enter the number to find the Fibonacci series : "))))

# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def info(self):
#         print(f"{self.name} is {self.age}years old")
# class employee(person):
#     def __init__(self,name,age,language,job):
#         super().__init__(name,age)
#         self.language=language
#         self.job=job
#     def info(self):
#         super().info()
#         print(f"{self.name} knows {self.language} and works as a {self.job}")   
        
# a=employee(input("enter name : "),int(input("enter ur age : ")),input("enter your language : "),input("enter your job : "))
# a.info()


# for x in range(100):
#     print(f"kusjal is donkey")

# import sqlite3

# conn = sqlite3.connect("database.db")
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
# id INTEGER PRIMARY KEY,
# name TEXT,
# email TEXT,
# password TEXT
# )
# """)

# conn.commit()
# conn.close()

# print("Table created successfully")

# Read input from user
N = int(input("Enter the value of N: "))

# Initialize first two terms
a = 0
b = 1

print("Fibonacci sequence:")

if N <= 0:
    print("Please enter a positive integer.")
elif N == 1:
    print(a)
else:
    print(a, b, end=" ")
    
    for i in range(2, N):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
