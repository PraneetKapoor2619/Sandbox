"""
Write a python program to find common elements from two given list.
Input:
X=[12,34,56]
Y=[11,12,15]
Output:
Z=[12]
"""

if __name__ == "__main__" :
        X = [12, 34, 56]
        Y = [11, 12, 15]
        
        # just use list comprehension, and 'in' keyword
        Z = [X[i] for i in range(len(X)) if X[i] in Y]

        print("X:", X, "\nY:", Y, "\n\nZ:", Z)