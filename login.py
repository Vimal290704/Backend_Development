name = input("Enter your name: ")
password = input("Enter your password: ")
print("Account Created Successfully")
login_credentials = [[name, password]]
isUser = False

while not isUser:
    l1 = input("Enter your name: ")
    l2 = input("Enter your password: ")
    if l1 == login_credentials[0][0] and l2 == login_credentials[0][1]:
        isUser = True
        print("User logged in Successfully")
    else:
        print("Invalid Credentials")
        isUser = False
