myorg = input()
mystr = myorg.strip()
for c in mystr:
    location_c = mystr.index(c)
    if c in ['+']:
        myresult = eval(mystr[0:location_c])+eval(mystr[location_c+1:])
    elif c in ['-']:
        if location_c !=0:
            myresult = eval(mystr[0:location_c])-eval(mystr[location_c+1:])
    elif c in ['*']:
        myresult = eval(mystr[0:location_c])*eval(mystr[location_c+1:])
    elif c in ['/']:
        myresult = eval(mystr[0:location_c])/eval(mystr[location_c+1:])
print("{:.2f}".format(myresult))