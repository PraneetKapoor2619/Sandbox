class Book:
        """
        Class Book
        - Attributes are name and price of the book
        - Attributes to be initialized either with the default or user
        specified values
        - print_details() prints details of the book on the scren
        - + operator is overloaded, allowing the user to sum up the total 
        price of the books
        """
        def __init__(self, name = "", price = 1.0):
                self.__name = name
                self.__price = price
        
        def __add__(self, obj):
                return Book(price = (self.get_price() + obj.get_price()))
        
        def get_name(self):
                return self.__name
        
        def get_price(self):
                return self.__price
        
        def change_name(self, name):
                self.__name = name
        
        def change_price(self, price):
                self.__price = price
        
        def print_details(self):
                print("{:s}\t\tINR {:.2f}"\
                .format(self.get_name(), self.get_price()))

def new_entry():
        print("Creating a new record...")
        name = input("Name: ").strip()
        price = int(input("Price: "))
        obj = Book(name, price)
        book_record.append(obj)

def edit_entry():
        print("Editing a record...")
        name = input("Name of the book: ").strip()
        obj = [book for book in book_record if book.get_name() == name]
        if len(obj) != 1 :
                print("Book not found or corrupted records")
                return 1
        
        obj = obj[0]
        obj.print_details()
        name = input("Enter new name of the book (Press Enter if no changes are req.): ").strip()
        if (len(name) > 0) : obj.change_name(name)
        price = input("Enter new price of the book (Press Enter if no changes are req.): ").strip()
        if (len(price) > 0) : obj.change_price(int(price))
        obj.print_details

def print_details():
        print("Record")
        for book in book_record :
                book.print_details()

def compute_total_price():
        obj = Book(price = 0)
        for book in book_record :
                obj += book

        print("Total price of all the books in the record is INR",\
        obj.get_price())

if __name__ == "__main__" :
        book_record = []
        while True :
                print("-" * 80)
                print("1. Create new entry\n2. Edit existing entry",\
                "\n3. Print details\n4. Compute total price\n5. Exit")
                option = int(input(">> "))
                print("")
                if option == 1 : new_entry()
                elif option == 2 : edit_entry()
                elif option == 3 : print_details()
                elif option == 4 : compute_total_price()
                elif option == 5 : exit()
                else : print("\aInvalid option!")