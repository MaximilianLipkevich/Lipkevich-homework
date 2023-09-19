class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        return book

    def group_by_author(self, author):
        books_author = []
        for book in self.books:
            if book.author == author:
                books_author.append(book)
        return books_author

    def group_by_year(self, year):
        books_year = []
        for book in self.books:
            if book.author == year:
                books_year.append(book)
        return books_year

    def __repr__(self):
        return f'Library(name="{self.name}", books={self.books}, authors={self.authors})'

    def __str__(self):
        return f'Library: {self.name}'

class Book:
    total = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.total += 1

    def __repr__(self):
        return f'Book(name="{self.name}", year={self.year}, author={self.author})'

    def __str__(self):
        return f'Book: {self.name}'

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Author(name="{self.name}", country="{self.country}", birthday="{self.birthday}")'

    def __str__(self):
        return f'Author: {self.name}'

l1 = Library('Knygarnya')
a1 = Author('Dostoyevsky', 'Russia', 1800)
a2 = Author('Rowling', 'United Kingdom', 1970)
l1.new_book('Harry Potter', 2000, a2)
l1.new_book('Crime and Punishment', 1800, a1)
l1.new_book('Idiot', 1800, a1)
print(l1.group_by_author(a1))