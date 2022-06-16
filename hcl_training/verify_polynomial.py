import re

def lexer(expression):
        terms = re.findall("[^\-\+]+", expression)
        signs = re.findall("[\-\+]+", expression)
        if len(signs) < len(terms):
                signs.insert(0, "+")
        terms = list(zip(terms, signs))
        return terms

def process(x, term):
        term, sign = term[0].strip(" "), term[1]
        val = 0
        if sign == "+": val = 1
        elif sign == "-": val = -1 
        if ("**" in term) or ("x" in term):
                if "**" in term:
                        i = term.index("**") + 2
                        val *= (x ** int(term[i:].strip(" ")))
                else:
                        val *= x
                if term.index("x") > 0:
                        i = term.index("x")
                        val *= float(term[0:i].strip(" *"))
        else:
                val *= int(term)
        return val

if __name__ == "__main__":
        x, k = map(int, input().split(" "))
        expression = input()
        p_x = 0

        terms = lexer(expression)
        for term in terms:
                p_x += process(x, term)
        print(p_x == k)