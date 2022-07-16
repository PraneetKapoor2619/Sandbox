from html.parser import HTMLParser

class BeautifulParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
                print(tag)
                self.handle_attrs(attrs)

        def handle_endtag(self, tag):
                pass

        def handle_startendtag(self, tag, attrs):
                print(tag)
                self.handle_attrs(attrs)
        
        def handle_attrs(self, attrs):
                for attribute in attrs :
                        print("->", attribute[0], ">", attribute[1])

if __name__ == "__main__" :

        buffer = ""

        for _ in range(int(input())) :
                buffer += input().strip() + "\n"
        
        parser = BeautifulParser()
        parser.feed(buffer)
        parser.close()