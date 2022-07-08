"""
Use list comprehension to add each element of a list, say x to each element of other list, say
y.
Input:
X=[12,34,56]
Y=[11,12,15]
Output:
Y=[11,12,15,12,34,56]
"""

if __name__ == "__main__" :
        X = [12, 34, 56]
        Y = [11, 12, 15]
        print("X:", X, "\nY:", Y)

        # using list comprehension to add each element of a list to another
        Y = [Y[i] if i < len(Y) else X[i - len(Y)] for i in range(len(X) + len(Y))]
        print("\nY after inclusion of elements from X:", Y) 