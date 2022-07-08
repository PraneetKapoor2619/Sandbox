"""
Write a lambda function to filter even numbers from a given number list
"""

isEven = lambda num: num % 2 == 0

if __name__ == "__main__" :
        num_list = list(map(int,\
         input("Enter the list of numbers (seperated by space): ").split()))
        filtered_list = list(filter(isEven, num_list))
        print("List of even numbers is:", filtered_list)