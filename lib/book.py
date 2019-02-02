"""
    Class Book: stores individual book information and returns it
"""

class Book(object):

    def __init__(self, name, writer, ISBN):
        self.name = name.strip()
        self.writer = writer.strip()
        self.ISBN = ISBN.strip()

    def print_info(self):
        print("{:<30} {:<30} {:<30}" .format(self.writer, self.name, self.ISBN))

    def get_info(self):
        return ("{0}\t {1}\t {2}" .format(self.name, self.writer, self.ISBN))

    def __eq__(self, other):
        return self.writer == other.writer

    def __lt__(self, other):
        return self.writer < other.writer