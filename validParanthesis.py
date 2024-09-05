s = "()"
stack=[]
d={"(":")","{":"}","[":"]"}
for i in s:
    if i in d.keys():
        stack.append(i)
    else:
        if stack==[]:
            print(0)
        else:
            if d[stack[-1]]==i:
                stack.pop()
            else:
                print(0)
if stack==[]:
    print(1)          
else:
    print(0)
            