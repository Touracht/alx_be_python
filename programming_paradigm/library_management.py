class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if self._is_checked_out == False:
            self._is_checked_out = True

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False

class Library:
    def __init__(self):
        self._books= []
        """Stores the books"""

    def add_book(self, Book):
        """Add the book to the list"""  
        self._books.append(Book)

    # def check_out_book(self, title):
    #     for book in self._books:
    #         if title == book.title
    
    def list_available_books(self):
        for book in self._books:
            print(f"{book.title} by {book.author}")
            
            


               
               