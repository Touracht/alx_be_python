class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._book = []
        """Stores the books"""

    def add_book(self, book):
        """Add the book to the list"""
        adding_book = self._book.append(book)
        return adding_book
    
    def check_out_book(self, title):
        