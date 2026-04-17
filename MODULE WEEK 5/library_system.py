class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    
    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print() 

book1 = Book("Python Programming", "John paul", 2026)
book2 = Book("Introduction to Java", "Jay Doe", 2025)
book3 = Book("Web Development Basics", "Mark bull", 2025)

book1.display_book()
book2.display_book()
book3.display_book()