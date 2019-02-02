"""
    Class BookLibrary: stores library information, reads data from file and writes it back to same file
    Uses Book class to create books stored in BookLibrary
"""

from lib.book import Book

class BookLibrary(object):

    books = []

    def __init__(self, filename):
        # store filename
        self.filename = filename

        # read file
        with open(filename) as f:
            content = f.read().splitlines()
        f.close()

        # create books
        for line in content:
            book_information = line.split("\t")
            if(len(book_information) == 3):
                self.add_book(book_information[0],book_information[1],book_information[2])

    def print_books(self):
        self.books = sorted(self.books)
        print("--------------------------------------------------------------------------------")
        for library_book in self.books:
            library_book.print_info()
        print("--------------------------------------------------------------------------------")

    def add_book(self, book, writer, isbn):
        self.books.append(Book(book, writer, isbn))

    def write_db_to_file(self):
        # sort books
        self.books = sorted(self.books)
        with open(self.filename, "w") as f:
            for library_book in self.books:
                f.write(library_book.get_info()+"\n")
        f.close()