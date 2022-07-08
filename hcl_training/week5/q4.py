import pickle

class Employee:
        """
        Class: Employee
        Attributes:     __name
                        __id
                        __email_id
        Methods:
                        __init__
                        get_details
                        set_name
                        set_id
                        set_email_id
                        print_details
        """
        
        def __init__(self, name, id = "NA", email_id = "NA"):
                self.__name = name
                self.__id = id
                self.__email_id = email_id
        
        def get_details(self):
                return self.__name, self.__id, self.__email_id
        
        def set_name(self, name):
                self.__name = name
        
        def set_id(self, id):
                self.__id = id
        
        def set_email_id(self, email_id):
                self.__email_id = email_id
        
        def print_details(self):
                print("Name:", self.__name, "\nID:", self.__id,\
                "\nEmail ID:", self.__email_id)

if __name__ == "__main__" :

        # define a few class objects
        emp1 = Employee("Praneet Kapoor")
        emp2 = Employee("ABCD EFGH", id = 47)
        emp1.set_id(29)
        emp1.set_email_id("kapoorpraneet2619@gmail.com")
        emp2.set_email_id("mail1@mailservice.com")

        # serialize the object and dump into a binary file
        emp_record = [emp1, emp2]
        with open("employee_record.bin", "wb+") as outstream :
                pickle.dump(emp_record, outstream)
        outstream.close()

        # read from the file, deserialize the bytes, and reconstruct the objects
        with open("employee_record.bin", "rb") as instream :
                reconstructed_emp_record = pickle.load(instream)
        instream.close()
        
        # print the details
        reconstructed_emp_record[0].print_details()
        reconstructed_emp_record[1].print_details()