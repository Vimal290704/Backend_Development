try:
    x = int(input("Input an Integer: "))
    print(x)
except (
    ValueError
):  # the except activates on error and we can specify it's activation cause too like here it is ValueError
    print("Value not Integer")
else:  # it occurs only when when it's a pass
    print("nothing went wrong")
finally:  # it activates after all passing either it is a pass or failure
    print("try except finished")
