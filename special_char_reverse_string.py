s=input('enter a string:')
length=len(s)-1
s1=''
for i in range(length,-1,-1):
    print(s1.join(s[i]))
