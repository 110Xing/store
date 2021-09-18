list = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
i=[]
for a in list:
    if a in i:
        continue
    else:
        i.append(a)

for b in i:
    j=0
    for c in list:
        if b==c:
            j=j+1
    print(b,j)












