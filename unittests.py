"""
usage:
python -m unittest unittest.py
python -m unittest unittest.BookLibraryUnittests
python -m unittest unittests.BookLibraryUnittests.test_book_creation

"""

import unittest
from lib.book_library import BookLibrary
from lib.book import Book

class BookLibraryUnittests(unittest.TestCase):

    def setUp(self):
        self.writer_1 = "Kalle Kirjailija"
        self.book_1 = "Kirja 1"
        self.isbn_1 = "12345"

        self.writer_2 = "Yrjö Yrjänä"
        self.book_2 = "Kirja 1"
        self.isbn_2 = "67890"

    def tearDown(self):
        del self.writer_1
        del self.book_1
        del self.isbn_1

    def test_book_creation(self):
        # create new book
        test_book = Book(self.book_1, self.writer_1, self.isbn_1)
        # check book values
        self.assertEqual(test_book.name, self.book_1)
        self.assertEqual(test_book.writer, self.writer_1)
        self.assertEqual(test_book.ISBN, self.isbn_1)

    def test_book_get_info(self):
        # create new book
        test_book = Book(self.book_1, self.writer_1, self.isbn_1)
        # test print_info-method
        print_info_str = "{0}\t {1}\t {2}" .format(self.book_1, self.writer_1, self.isbn_1)
        self.assertEqual(test_book.get_info(), print_info_str)

    def test_book_sort(self):
        # create test books
        test_book_1 = Book(self.book_1, self.writer_1, self.isbn_1)
        test_book_2 = Book(self.book_2, self.writer_2, self.isbn_2)
        # test sorting
        self.assertTrue(test_book_1 < test_book_2)
        self.assertFalse(test_book_1 > test_book_2)


if __name__ == "__main__":
    unittest.main()