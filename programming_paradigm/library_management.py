class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out = False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
            return False

    def return_book(self):
        if self._last_checked_out:
            self._last_checked_out._is_checked_out = False
            self._last_checked_out = None
            return True
        return False

    def list_available_books():
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
