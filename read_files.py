# content = open("./test.txt", "r")
# print(content.readable())
# content_str = content.readlines()
# for line in content_str:
#     print(line)
# content.close()


# writing files
content = open("./new.py", "a")
content.write("print('This a new line')")
