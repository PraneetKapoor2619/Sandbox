import re
import email.utils

def isValidEmailID(email):

        match = bool(re.match(r"^([a-zA-Z]{1})([a-zA-Z0-9\-_.]{1,})@([a-zA-Z]{1,})\.([a-zA-Z]{1,3})$", email))
        return match

if __name__ == "__main__" :

        for _ in range(int(input())) :
                string = input()
                emailid = email.utils.parseaddr(string)[1]
                if isValidEmailID(emailid) : print(string)