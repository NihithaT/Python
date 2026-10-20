print("power of 4: n % 3 == 1 and power of 8: n % 7 == 1")
print("16 binary =", bin(16)[2:], "16 % 3 = ", 16 % 3, "16 % 7 = ", 16 % 7)
print("8 binary =", bin(8)[2:], "8 % 3 = ", 8 % 3, "8 % 7 = ", 8 % 7)
n=int(input("Enter a number:"))
if n>0 and n%3==1 and (n&(n-1)==0):
    print(n, "is a power of 4", "binary representation of", n, "is", bin(n)[2:])
else: 
    print(n, "is not a power of 4", "binary representation of", n, "is", bin(n)[2:])
if n>0 and n%7==1 and (n&(n-1)==0):
    print(n, "is a power of 8", "binary representation of", n, "is", bin(n)[2:])
else: 
    print(n, "is not a power of 8", "binary representation of", n, "is", bin(n)[2:])


      