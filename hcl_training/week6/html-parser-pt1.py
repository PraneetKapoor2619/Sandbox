from html.parser import HTMLParser

class BeautifulParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
                print("Start :", tag)
                if attrs :
                        for element in attrs :
                                print("->", element[0], ">", element[1])

        def handle_endtag(self, tag):
                print("End   :", tag)

        def handle_startendtag(self, tag, attrs):
                print("Empty :", tag)
                if attrs :
                        for element in attrs :
                                print("->", element[0], ">", element[1])


if __name__ == "__main__" :

        buffer = ""

        for _ in range(int(input())) :
                buffer += input()

        parser = BeautifulParser()
        parser.feed(buffer)
        parser.close()