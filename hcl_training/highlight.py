def highlight(func):

        def __highlight__():
                print(50 * '+')
                func()
                print(50 * '+')
        
        return __highlight__

def standard():
        print("Hello world")

@highlight
def cowsay_hello():
        print("Hello young Padawan!!")

print_1 = highlight(standard)
print_1()

cowsay_hello()