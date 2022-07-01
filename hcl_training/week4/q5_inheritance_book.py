class basic_details_class:
        """
        Class basic_details_class
        - defines attributes which gives the most basic info about 
        a company or a person
        - defines method for getting, editing and printing the information
        """        
        def __init__(self, name = "NA"):
                self.__name = name
                self.__street_no = "NA"
                self.__city = "NA"
                self.__state = "NA"
                self.__country = "NA"
                self.__pincode = -1
        
        def get_name(self):
                return self.__name
        
        def get_address(self):
                return self.__street_no, self.__city, self.__state,\
                self.__country, self.__pincode
        
        def change_name(self):
                print("Old name: {:s}".format(self.__name))
                name = input("New name (Enter if same): ").strip()
                if (len(name) > 0) :
                        self.__name = name
        
        def change_address(self):
                print("Old street no.:", self.__street_no)
                street_no = input("New street no. (Enter if same): ").strip()
                if (len(street_no) > 0) :
                        self.__street_no = street_no
                
                print("Old city: {:s}".format(self.__city))
                city = input("New city (Enter if same): ").strip()
                if (len(city) > 0) : self.__city = city
                
                print("Old state: {:s}".format(self.__state))
                state = input("New state (Enter if same): ").strip()
                if (len(state) > 0) : self.__state = state
                
                print("Old country: {:s}".format(self.__country))
                country = input("New country (Enter if same): ").strip()
                if (len(country) > 0) : self.__country = country
                
                print("Old pincode: ", end = "")
                if (self.__pincode == -1) : print("NA")
                else : print(self.__pincode)
                
                pincode = input("New pincode (Enter if same): ").strip()
                if (len(pincode) > 0) : self.__pincode = int(pincode)

class Publisher():
        """
        Class Publisher
        - attributes are the name and address of the publisher
        - attributes and methods are derived from the parent class, basic_details_class
        """
        def __init__(self, name):
                self.__publisher = basic_details_class(name)

        def get_name(self):
                return self.__publisher.get_name()

        def get_address(self):
                return self.__publisher.get_address()

        def change_name(self):
                print("Changing publisher name...")
                self.__publisher.change_name()
        
        def change_address(self):
                print("Changing publisher address...")
                self.__publisher.change_address()

        def show(self):
                print("Publisher: {:s}\nAddress: {:s}, {:s}, {:s}, {:s}\nPincode: {:d}"\
                .format(self.__publisher.get_name(),
                *self.__publisher.get_address()))        


class Author():
        """
        Class Author
        - attributes are the name and the address of the author
        - attributes and methods are derived from the parent class, basic_details_class
        """
        def __init__(self, name):
                self.__author = basic_details_class(name)
                print(self.__author.get_name())
        
        def get_name(self):
                return self.__author.get_name()
        
        def get_address(self):
                return self.__author.get_address()

        def change_name(self):
                print("Changing author name...")
                self.__author.change_name()
        
        def change_address(self):
                print("Changing author address...")
                self.__author.change_address()

        def show(self):
                print("Author: {:s}\nAddress: {:s}, {:s}, {:s}, {:s}\nPincode: {:d}"\
                .format(self.__author.get_name(),
                *self.__author.get_address()))

class Book(Author, Publisher):
        """
        Class Book
        - attributes include name and price of the book
        - other attributes and methods have been inherited from the parent classes: Author 
        and Publisher
        """
        def __init__(self, name, author_name = "NA", publisher_name = "NA", price = 1.0):
                self.__name = name
                self.__price = price
                Author.__init__(self, author_name)
                Publisher.__init__(self, publisher_name)
        
        def get_name(self):
                return self.__name
        
        def get_price(self):
                return self.__price
        
        def get_publisher_name(self):
                return Publisher.get_name(self)
        
        def get_publisher_address(self):
                return Publisher.get_address(self)
        
        def get_author_name(self):
                return Author.get_name(self)
        
        def get_author_address(self):
                return Author.get_address(self)
        
        def change_name(self):
                print("Old name: {:s}".format(self.__name))
                name = input("Enter new name (Enter if same): ").split()
                if (len(name) > 0) : self.__name = name
        
        def change_price(self):
                print("Old price: {:d}".format(self.__price))
                price = input("Enter the new price (Enter if same): ").split()
                if (len(price) > 0) : self.__price = int(price)
        
        def change_author_name(self):
                Author.change_name(self)
        
        def change_author_address(self):
                Author.change_address(self)
        
        def change_publisher_name(self):
                Publisher.change_name(self)
        
        def change_publisher_address(self):
                Publisher.change_address(self)

        def show(self):
                print("Book name: {:s}\nPrice: INR {:d}".format(self.__name, self.__price))

        def show_all(self):
                Book.show(self)
                Author.show(self)
                Publisher.show(self)

if __name__ == "__main__" :
        book = Book(name = "Surely your're joking Mr. Feynman", price = 450,\
         author_name = "Richard Feynman, Ralph Leighton", publisher_name = "W.W. Norton")
        book.change_author_address()
        book.change_publisher_address()
        book.show_all()                # displays everything related to the book