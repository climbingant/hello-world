template = "零一二三四五六七八九"

s = input()
for c in s:
    if c in  ['0','1','2','3','4','5','6','7','8','9']:
        print(template[eval(c)], end="")
    elif c in ['零','一','二','三','四','五','六','七','八','九']:
        print(template.index(c),end="")
    else:
        print("error!")
