
class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        list_of_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                list_of_contracts.append(contract)
        return list_of_contracts
    
    def books(self):
        list_of_books = []
        for contract in Contract.all:
            if contract.author == self:
                list_of_books.append(contract.book)
        return list_of_books
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties
        return total 


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        list_of_contracts = []
        for contract in Contract.all:
            if contract.book == self: 
                list_of_contracts.append(contract)

        return list_of_contracts
    
    def authors(self): 
        list_of_authors = []
        for contract in Contract.all:
            if contract.book == self:
                list_of_authors.append(contract.author)
        return list_of_authors
        

class Contract:
    all  = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Invalid author instance")
        self._author = value
    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value): 
        if not isinstance(value, Book):
            raise Exception("Invalid book instance")
        self._book = value
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str): 
            raise Exception("Date must be a string")
        self._date = value
    @property
    def royalties(self):
        return self._royalties 
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Must be an integer")
        self._royalties = value


    @classmethod
    def contracts_by_date(cls, date):

        matching_contracts = [contract for contract in cls.all if contract.date == date]
        return matching_contracts
        