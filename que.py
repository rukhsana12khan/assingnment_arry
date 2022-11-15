a=[1,2,3,3,4,55,55,9]
mo=''
for i in a:
    c=0
    for j in a:
        
        if j==i:
            c+=1
    if c>0:
        if str(i) not in mo:
            mo=mo+str(i)+' '
print(mo)                    