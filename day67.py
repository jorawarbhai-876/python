# write a library class with no of books as two instance variables. write a program to create a library from this library class and how you can print all the books, add a book and get the number of books using diffrent methods. show that your program dosen't persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books=[]

def addBooks(self, book):
    self.books.append(book)
    self.nobooks = len(self.books)

def showInfo(self):
    print(f"The library has (self.noBooks)books.The books are") 
    for book in self.books:
        print(book) 
l1 = Library()
l1.addbook("Harry Potter1")
l1.addbook("Harry Potter2")
l1.addbook("Harry Potter3")

l1.showInfo()