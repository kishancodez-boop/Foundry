class library:
    def __init__(self,books =[],n=0):
        self.books=books
        self.n=n
    def dispalybooks(self):
        for book in self.books:
            print(book)
    def addbooks(self,book):
        self.books.append(book)
        print(f"the bookk {book} has been added ")
    @staticmethod
    def add(a,b):
        return a+b
B=library(["python","c++","java"],int(input("enter the number of books : ")))
B.dispalybooks()
B.addbooks("javascript")
B.dispalybooks()
print(B.add(5,10))