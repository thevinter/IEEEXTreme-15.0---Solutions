import re

T = int(input())
for n in range(T):
    x = input()
    if re.search(r"[^0-9()*\-+]", x) != None:
        print("invalid")
    elif re.search(r"\(\)", x) != None:
        print("invalid")
    elif re.search(r"[+\-*][+\-*]", x) != None:
        print("invalid")
    elif re.search(r"\)\(", x) != None:
        print("invalid")
    elif re.search(r"\([+\-]", x) != None:
        print("invalid")
    elif len(x) == 0:
        print("invalid")
    elif x[0] == "-" or x[0] == "+":
        print("invalid")
    else: 
        try:
            res = eval(x)
            print(res % 1000000007)
        except: 
            print("invalid")
