haystack = "sadbutsad"
needle = "sad"
mover=[0]*len(needle)
pre=0
for i in range(1,len(needle)):
    while pre>0 and needle[i]!=needle[pre]:
        pre=mover[pre-1]
        if needle[i]==needle[pre]:
            pre+=1
            mover[i]=pre       
    n=0
    for h in range(len(haystack)):
        while (n>0 and needle[n] != haystack[h]):
            n=mover[n-1]
            if needle[n]==haystack[h]:
                n+=1
            if n==len(needle):
                print(h-n+1)
else:
    print(-1)