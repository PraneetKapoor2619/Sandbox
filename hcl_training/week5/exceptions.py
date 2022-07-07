for _ in range(int(input())) :
        try :
                a, b = map(int, input().split())
                print(int(a / b))
        except ValueError as val:
                print("Error Code:", val)
        except ZeroDivisionError :
                print("Error Code: integer division or modulo by zero")