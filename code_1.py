# import tkinter as tk

# window = tk.Tk()
# search = tk.Tk()
# window.title("My App")
# search.title("My App")

# label = tk.Label(window, text="Hello, Kushal!")
# label.pack()

# button = tk.Button(window, text="ENTER")
# button = tk.Button(search, text="please seacrh")
# button.pack()

# window.mainloop()
# search.mainloop()
# Read input from user
# N = int(input("Enter the value of N: "))

# Initialize first two terms
# a = 0
# b = 1

# print("Fibonacci sequence:")

# if N <= 0:
#     print("Please enter a positive integer.")
# elif N == 1:
#     print(a)
# else:
#     print(a, b, end=" ")
    
#     for i in range(2, N):
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c
def DivExp(a, b): 
    assert a > 0, "Value of a must be greater than 0" 
    if b == 0:   # Exception if b = 0 
        raise ZeroDivisionError("Division by zero is not allowed") 
    c = a / b 
    return c 

a = float(input("Enter value for a: ")) 
b = float(input("Enter value for b: ")) 

try: 
    result = DivExp(a, b) 
    print("Result (a/b) =", result) 
except AssertionError as e: 
    print("Assertion Error:", e) 
except ZeroDivisionError as e: 
    print("Exception:", e) 

