import re

def isValidUID(UID):
        """
        A valid UID must follow the rules below:

        - It must contain at least 2 uppercase English alphabet characters.
        - It must contain at least 3 digits (0 - 9).
        - It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
        - No character should repeat.
        - There must be exactly 10 characters in a valid UID.
        """

        match = re.match(r"^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$", UID)
        result = bool(match)
        return result

if __name__ == "__main__" :

        for _ in range(int(input())) :
                UID = input()
                if isValidUID(UID) :
                        print("Valid")
                else :
                        print("Invalid")