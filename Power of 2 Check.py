print("n & (n-1) clears the right most set bit")
print("12 & 11 = ", 12 & 11, "binary representation of", 12 & 11, "is", bin(12 & 11)[2:])
n=int(input("Enter a number:"))
if n>0 and n&(n-1)==0:
    print(n, "is a power of 2", "binary representation of", n, "is", bin(n)[2:])
else: 
    print(n, "is not a power of 2", "binary representation of", n, "is", bin(n)[2:])
    