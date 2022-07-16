import re

def replace(match):
        if match.group(0) == " && " : return " and "
        else : return " or "

if __name__ == "__main__" :
        buffer = ""

        for _ in range(int(input())) :
                buffer += input() + "\n"

        str_and = r" && "
        str_or = r" \|\| "
        buffer = re.sub(r"(%s|%s)" % (str_and, str_or), replace, buffer)
        print()
        print(buffer)