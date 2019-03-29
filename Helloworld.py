#HelloWorld
mystr = input()
if eval(mystr)== 0:
    print("Hello World")
elif eval(mystr) > 0:
    print("Hello",end="")
    print("World",end="")
elif eval(mystr) < 0:
    print("Hello\nWorld")
else:
    print("error")