class Author:

    def __init__(self,name):
        self.name = name
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self,book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid book: must be an instance of Book.")
        if not isinstance(date, str):
            raise Exception("Invalid date: must be a string.")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties: must be an integer.")

        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        total = 0
        for contract in self.contracts():
            total += contract.royalties 
        return total

class Book:
    def __init__(self,title):
        self.title = title
        pass

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all=[]
    def __init__(self,author, book, date, royalties):
        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception
        
        if isinstance(book,Book):
            self.book = book
        else:
            raise Exception
        
        if isinstance(date,str):
            self.date = date
        else:
            raise Exception
        
        if isinstance(royalties,int):
            self.royalties = royalties
        else:
            raise Exception
        
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]