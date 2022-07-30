#import libraries

# port selector with int checker

HOST = None
check = False

while check != True:
    PORT = input("Enter the port in the range from 1024 to 65535: ")
    if PORT.isnumeric():
        PORT = int(PORT)
        if PORT >= 1024 and PORT <= 65535:
            check = True
        elif PORT > 65535:
            print("The selected port is too high")
            check = False
        else:
            print("The selected port is too low")
            check = False
    else:
        print("The specified value is not a port")
        check = False