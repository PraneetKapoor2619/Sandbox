"""
Write a lambda function to multiply numbers of two given list.
Input:
List1=[12,34,56]
List2=[2,3,5]
Ouput:
[24,102,280]
"""

mul_list = lambda list1, list2: [list1[i] * list2[i] for i in range(len(list1))]

if __name__ == "__main__" :
        list1 = [12, 34, 56]
        list2 = [2, 3, 5]
        print("List1:", list1, "\nList2:", list2)
        print("Element-wise product of two lists:", mul_list(list1, list2))