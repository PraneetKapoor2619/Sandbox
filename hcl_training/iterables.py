sequence = "Hello world"
seq = ([ch.upper() for ch in sequence])

pairs = zip(sequence, seq)
print("Is pairs an iterable object?", hasattr(pairs, '__iter__'))

for pair in pairs:
        print(pair)
        break

print("Is pairs an iterator object?", hasattr(pairs, "__next__"))

while True:
        try:
                print(pairs.__next__())
        except:
                break