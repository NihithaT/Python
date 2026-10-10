n=int(input("Enter a number:"))
print("binary representation of", n, "is", bin(n)[2:])
print("set a bit: or turns it on")
print("5|2=", 5|2, "binary representation of", 5|2, "is", bin(5|2)[2:])

print("zero a bit: and turns it off")
print("5&2=", 5&2, "binary representation of", 5&2, "is", bin(5&2)[2:])
if n>0 and n&(n-1)==0:
    print(n, "is a power of 2")
else: 
    print(n, "is not a power of 2")