"""
    main program: uses BookLibrary to store book information
    usage: python main.py <file>
"""

import sys
from lib.book_library import BookLibrary

# get arguments from commandline
arguments = sys.argv

# check argument count
if(len(arguments) == 2):
    filename = sys.argv[1]
    library = BookLibrary(filename)
else:
    print ("Wrong number of arguments!")
    sys.exit(0)

def main():
    response = input("Please select operation 1) Add new book, 2) Print current database content, Q) Exit the program: ")

    # add new book
    if (response == "1"):
        writer = input("Give writer: ")
        name = input("Give book name: ")
        ISBN = input("Give ISBN number: ")
        print("{0}\t {1}\t {2}" .format(writer, name, ISBN))
        confirm = input("Do you want to update book to database? (y/n)")

        # if confirmed add book
        if(confirm == "y"):
            library.add_book(name, writer, ISBN)    # add book to library
            library.write_db_to_file()              # write updated library information db to file

    # print all books
    elif(response == "2"):
        library.print_books()

    # quit program
    elif(response == "Q"):
        sys.exit(0)

while(True):
    main()
