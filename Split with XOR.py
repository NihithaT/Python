print("XOR all - pair cancel, 2 odd occurring numbers remain")
print("[1,4,3,3]")
result = 1 ^ 4 ^ 3 ^ 3
print("odd ones in list:", result, "binary representation of", result, "is", bin(result)[2:])
n=int(input("Enter a number:"))
if n&1:
    print(n, "is odd", "binary representation of", n, "is", bin(n)[2:])
else:
    print(n, "is even", "binary representation of", n, "is", bin(n)[2:])
    
