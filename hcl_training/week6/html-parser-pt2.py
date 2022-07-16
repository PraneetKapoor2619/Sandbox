from html.parser import HTMLParser

class BeautifulParser(HTMLParser):

        def handle_comment(self, data):
                print(">>> ", end = "")
                if ("\n" in data) : print("Multi-line Comment")
                else : print("Single-line Comment")

                print(data)

        def handle_data(self, data):
                if data != "\n" :
                        print(">>> Data")
                        print(data)

if __name__ == "__main__" :

        buffer = ""

        for _ in range(int(input())) :
                buffer += input().strip() + "\n"
        
        parser = BeautifulParser()
        parser.feed(buffer)
        parser.close()