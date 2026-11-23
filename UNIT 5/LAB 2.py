class Library:
    def __init__(self):
        self.books = ["Python", "Java", "C Programming"]
    def display_books(self):
        print("Available Books:", self.books)
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "borrowed successfully")
        else:
            print("Book is not available")
    def return_book(self, book):
        self.books.append(book)
        print(book, "returned successfully")
lib = Library()
lib.display_books()
lib.borrow_book("Python")
lib.display_books()
lib.return_book("Python")
lib.display_books()
