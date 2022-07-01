class student:
        """
                Student class
                - Student entry is made by instantiating an object with a name and roll no.
                - Other attributes are address, email id, and phone number
        """
        def __init__(self, name, roll_no):
                self.name = name
                self.roll_no = roll_no
                self.house_addr = "NA"
                self.city = "NA"
                self.state = "NA"
                self.pincode = "NA"
                self.country = "NA"
                self.email = "NA"
                self.phone = "NA"

        def change_name(self):
                self.name = input("Name: ")

        def change_roll_no(self):
                self.roll_no = input("Roll no.: ")
        
        def change_address(self):
                self.house_addr = input("House no.: ")
                self.city = input("City: ")
                self.state = input("State: ")
                self.pincode = int(input("Pincode: "))
                self.country = input("Country: ")
        
        def change_email(self):
                self.email = input("Email id: ")

        def change_phone(self):
                self.phone = int(input("Phone no.: "))
        
        def print_details(self):
                print("Name:", self.name, "\nRoll. No.:", self.roll_no)
                print("Address:", self.house_addr + ",", self.city\
                 + ",", self.state + ",", self.country)
                print("Pincode:", self.pincode)
                print("Email:", self.email)
                print("Phone:", self.phone)


def new_entry():
        print("Creating new entry...")
        name = input("Enter name: ")
        roll_no = int(input("Enter roll no.: "))
        for i in student_details :
                if i.roll_no == roll_no :
                        print("Roll no. already in the system")
                        return
        obj = student(name, roll_no)
        student_details.append(obj)
        student_details.sort(key = lambda x: x.roll_no)

def roll_in_check():
        roll_no = int(input("Enter roll no.: "))

        obj = [i for i in student_details if i.roll_no == roll_no]
        if len(obj) != 1 :
                print("Invalid roll no. or possible faulty record")
                return -1
        print("Record found!")
        obj = obj[0]
        return obj

def edit_entry():
        obj = roll_in_check()
        if obj == -1 :
                return
        
        while True :
                print("1. Edit name\n2. Edit roll no.\n3. Edit address"\
                "\n4. Edit email id\n5. Edit phone no.\n6. Exit")
                option = int(input(">> "))
                if option == 1 :
                        obj.change_name()
                elif option == 2 :
                        obj.change_roll_no()
                elif option == 3 :
                        obj.change_address()
                elif option == 4 :
                        obj.change_email()
                elif option == 5 :
                        obj.change_phone()
                elif option == 6 :
                        return
                else :
                        print("\aInvalid option!!")

def print_entry():
        obj = roll_in_check()
        obj.print_details()

if __name__ == "__main__" :
        # Main body of the code
        student_details = []

        while True :
                print("-"*80)
                print("1. New entry\n2. Edit existing entry\n3. Print entry\n4. Exit")
                option = int(input(">> "))
                print("\n")

                if option == 1 :
                        new_entry()
                
                elif option == 2 :
                        edit_entry()

                elif option == 3 :
                        print_entry()
                
                elif option == 4 :
                        exit()
                else :
                        print("\a{:d} is not a valid option!!".format(option))