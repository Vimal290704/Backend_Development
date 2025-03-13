def check(a, b):
    if a == b:
        print("a == b")
    elif a < b:
        print("a is less than b")
    else:
        print("a is greater than b")
    print(a , b)

for i in range(10):
    check(i , 10 - i)