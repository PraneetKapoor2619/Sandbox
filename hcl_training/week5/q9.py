"""
Write a function to calculate product of elements of a list using lambda and reduce function
only.
"""

from functools import reduce

if __name__ == "__main__" :
        list1 = list(map(int, input("Enter the integer (space-separated): ").split()))
        print("Product of the elements of the list is:",\
        reduce(lambda n1, n2: n1 * n2, list1))