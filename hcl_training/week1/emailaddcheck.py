def fun(s):
        try:
                sign1 = s.index('@')
        except:
                return False
        try:
                sign2 = s.index('.')
        except:
                return False
        if (s.count('@') != 1) : return False
        if (s.count('.') != 1) : return False
        if (abs(sign1 - sign2) == 1) : return False
        if (sign2 <= sign1) : return False
        username = s.split('@')
        webext = username[1]
        username = username[0]
        websitename = webext.split('.')
        extension = websitename[1]
        websitename = websitename[0]
        if(len(username) == 0 or len(websitename) == 0 or len(extension) > 3): 
                return False
        #username @ websitename . extension
        for ch in username:
                if (not(ch.isalnum() or (ch == '_' or ch == '-'))):
                        return False
        for ch in websitename:
                if (not(ch.isalnum())):
                        return False
        for ch in extension:
                if (not(ch.isalpha())):
                        return False
        return True


def filter_mail(emails):
        return list(filter(fun, emails))

if __name__ == '__main__':
        n = int(input())
        emails = []
        for _ in range(n):
                emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)