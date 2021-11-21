class ILIbraryUser:
    def AddBook(self):
        pass
    def RemoveBook(self):
        pass
    def BookInfo(self):
        pass
    def BooksCount(self):
        pass

class LibraryUser(ILIbraryUser):
    FirstName="User firstname"
    LastName="User lasrname"
    id="User id"
    __Phone="User phone"
    BookLimimt=3
    BookList=[]
    def __init__(self, FirstName,LastName, id, Phone,BookLimimt,):
        self.FirstName=FirstName
        self.LastName = LastName
        self.id = id
        self.Phone = Phone
        self.BookLimimt = BookLimimt
    def AddBook(self, book):
        if self.BooksCount()<3:
            self.BookList.append(book)
        else:
            print("не можем добавити")

    def RemoveBook(self):
        self.BookList.remove()
    def BookInfo(self):
        for i in self.BookList:
            print(i)
    def BooksCount(self):
        return len(self.BookList)
    def RemoveBook(self, book):
        self.BookList.remove(book)


libraruuser=LibraryUser("Harry", "Potter", 0.1, 971826, 3)
libraruuser.AddBook("car")
libraruuser.AddBook("book")
libraruuser.AddBook("fire")
libraruuser.AddBook("wather")

libraruuser.BookInfo()
print("--------------")
libraruuser.RemoveBook("book")
libraruuser.BookInfo()





