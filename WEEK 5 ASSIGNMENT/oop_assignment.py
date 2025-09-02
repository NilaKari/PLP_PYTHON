# ==============================
# Assignment 1: Design Your Own Class
# ==============================

# Base class: Book
class Book:
    def __init__(self, title, author, pages, price):
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # Method: Display book details
    def book_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, priced at ${self.price}."

    # Method: Estimate reading time (assuming 1 min per page)
    def reading_time(self):
        return f"Estimated reading time: {self.pages} minutes."


# Subclass: Ebook (inherits from Book)
class Ebook(Book):
    def __init__(self, title, author, pages, price, file_size):
        # Call parent constructor
        super().__init__(title, author, pages, price)
        self.file_size = file_size  # New attribute

    # Overriding book_info() → polymorphism
    def book_info(self):
        return f"E-Book: '{self.title}' by {self.author}, {self.pages} pages, file size {self.file_size}MB, priced at ${self.price}."

    # Extra method: download
    def download(self):
        return f"Downloading '{self.title}'... 📥"


# Example usage of Book & Ebook
normal_book = Book("Things Fall Apart", "Chinua Achebe", 209, 15)
print(normal_book.book_info())
print(normal_book.reading_time())

ebook = Ebook("Becoming", "Michelle Obama", 448, 10, 5)
print(ebook.book_info())
print(ebook.download())