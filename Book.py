print("***************************************************************************************************************")

print("Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)

book = Book.from_string("Python Programming, John Doe")

print("Title of Book ::", book.title)
print("Author ::", book.author)

print("***************************************************************************************************************")
