import pickle

class datatype:

        def __init__(self, name, id):
                self.__name = name
                self.__id = id

        def print_datatype(self):
                print("Name:", self.__name, "\nID:", self.__id)

obj1 = datatype("Praneet Kapoor", 4115604918)
obj1.print_datatype()

# serialization 
with open("datatype-dump.bin", "wb+") as outstream :
        pickle.dump(obj1, outstream)

# de-serialization
with open("datatype-dump.bin", "rb") as instream :
        reconstructed_obj = pickle.load(instream)

reconstructed_obj.print_datatype()