class newdata:
        offset = 10

        def __init__(self):
                self.x = int()
                self.arr = list()
        
        def setit(self, x, arr):
                self.x = x
                self.arr = arr
        
        def operation(self):
                self.arr = [(element * self.x) + newdata.offset for element in self.arr]
                print(self.arr)

obj1 = newdata()
obj2 = newdata()

obj1.offset = 15        # new instance variable is added to obj1
print(newdata.offset, obj1.offset)              

obj1.setit(20, [1, 2, 3, 4])
obj2.setit(-10, [15])

obj1.operation()
obj2.operation()

print(obj1.x, obj1.arr)
print(obj2.x, obj2.arr)