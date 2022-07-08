"""
Write a lambda function that returns square for each value from a number list.
Input:
List1=[12,3,5,7,9]
Output:
List1=[144,9,25,49,81]
"""

square = lambda n: n ** 2

if __name__ == "__main__" :
        list1 = [12, 3, 5, 6, 9]
        print("Input:", list1)
        
        list1 = [square(val) for val in list1]
        print("Output:", list1)