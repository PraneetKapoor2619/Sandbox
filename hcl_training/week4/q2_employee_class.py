class employee:
        """
        Employee class:
        - Stores Name, department, ID, age, and email address
        - ID is automatically generated and incremented with object creation
        """

        total_employees = 0

        def __init__(self, name):
                self.__name = name
                employee.total_employees += 1
                self.__id = employee.total_employees
                self.__department = str()
                self.__age = int()
                self.__email = str()
        
        def set_department(self, department):
                self.__department = department
        
        def set_age(self, age):
                self.__age = age
        
        def set_email(self, email):
                self.__email = email
        
        def print_details(self):
                print("-"*80)
                print("Name:", self.__name,\
                "\nID:", self.__id,\
                "\nDepartment:", self.__department,\
                "\nAge:", self.__age,\
                "\nEmail:", self.__email)
                print("-"*80)

if __name__ == "__main__" :
        emp1 = employee("Praneet Kapoor")
        emp1.set_department("Operating Systems")
        emp1.set_age(23)
        emp1.set_email("kapoorpraneet2619@gmail.com")

        emp2 = employee("Rachit Jain")
        emp2.set_department("Embedded Systems")
        emp2.set_age(22)
        emp2.set_email("rachitjain24@gmail.com")

        emp1.print_details()
        emp2.print_details()