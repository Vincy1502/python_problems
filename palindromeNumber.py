x = 121
num=x
reverse=0
while x>0:
    digit=x%10
    reverse=reverse*10+digit
    x=x//10
if reverse==num:
    print(True)
else:
    print(False)
               