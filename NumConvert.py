#NumConvert.py
import sys
NumStr = input()
if NumStr[0] in ['0','1','2','3','4','5','6','7','8','9']:
    i = 0
    for i in range(len(NumStr)):
        if NumStr[i] in ['0']:
            sys.stdout.write("零")
        elif NumStr[i] in ['1']:
            sys.stdout.write("一")
        elif NumStr[i] in ['2']:
            sys.stdout.write("二")
        elif NumStr[i] in ['3']:
           sys.stdout.write("三")
        elif NumStr[i] in ['4']:
            sys.stdout.write("四")
        elif NumStr[i] in ['5']:
            sys.stdout.write("五")
        elif NumStr[i] in ['6']:
            sys.stdout.write("六")
        elif NumStr[i] in ['7']:
            sys.stdout.write("七")
        elif NumStr[i] in ['8']:
            sys.stdout.write("八")
        elif NumStr[i] in ['9']:
            sys.stdout.write("九")
        else:
            print("False")
elif NumStr[0] in ['零','一','二','三','四','五','六','七','八','九']:
    i = 0
    for i in range(len(NumStr)):
        if NumStr[i] in ["零"]:
            sys.stdout.write("0")
        elif NumStr[i] in []:
            sys.stdout.write("1")
        elif NumStr[i] in ['二']:
            sys.stdout.write("2")
        elif NumStr[i] in ['三']:
            sys.stdout.write("3")
        elif NumStr[i] in ['四']:
            sys.stdout.write("4")
        elif NumStr[i] in ['五']:
            sys.stdout.write("5")
        elif NumStr[i] in ['六']:
            sys.stdout.write("6")
        elif NumStr[i] in ['七']:
            sys.stdout.write("7")
        elif NumStr[i] in ['八']:
            sys.stdout.write("8")
        elif NumStr[i] in ['九']:
            sys.stdout.write("9")
        else:
            print("False")
else:
    print("False-fatle")