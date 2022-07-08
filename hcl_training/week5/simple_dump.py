import pickle

vowel_dict = {1: 'a', 2: 'e', 3: 'i', 4: 'o', 5: 'u', 6: 'y'}

# serialization
with open("dump.bin", "wb+") as outfile :
        pickle.dump(vowel_dict, outfile)

# deserialization
with open("dump.bin", "rb") as infile :
        reconstructed_dict = pickle.load(infile)

print(reconstructed_dict)