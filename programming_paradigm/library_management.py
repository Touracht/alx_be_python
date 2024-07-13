class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        _is_checked_out = False

class Library:
    def __init__(self):
        self._book = []
        """Stores the books"""

    def add_book(self, book):
        """Add the book to the list"""
        adding_book = self._book.append(book)
        return adding_book
    
    def check_out_book(self, title):
        if title == book:
            return True
        else:
            return False
    def return_book(self, title):
        if title == book:
            return False
    def list_available_books(self):
        for book in self._book:
            return book

    