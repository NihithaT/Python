n=int(input("Enter a number:"))
p=n
pos=0
while p>0:
    print("binary:", bin(p)[2:], "last bit:", p&1)
    if p&1==1:
        break
    pos+=1
    p=p>>1
print("First set bit is at position:", pos)
