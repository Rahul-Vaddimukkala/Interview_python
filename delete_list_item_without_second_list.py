l=[1,1,2,3,4,4,5,5,5]

i=0
lent=len(l)

while i<lent:
    j=i+1
    while j<lent:
        if l[i]==l[j]:
            del l[j]
            lent=len(l)
        else:
            j=j+1
    i=i+1
    
print(l)

