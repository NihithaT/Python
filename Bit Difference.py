print("Bit difference - XOR shows which bits differ")
print("5 XOR 3 =", 5 ^ 3, "binary representation of", 5 ^ 3, "is", bin(5 ^ 3)[2:].count('1'), "bits differ")
print("21 XOR 42 =", 21 ^ 42, "binary representation of", 21 ^ 42, "is", bin(21 ^ 42)[2:].count('1'), "bits differ")
n1 = int(input("Enter a number:"))
n2 = int(input("Enter another number:"))
print(n1, "in binary representation is", bin(n1)[2:])
print(n2, "in binary representation is", bin(n2)[2:])
print(n1, "XOR", n2, "=", n1 ^ n2, "binary representation of", n1 ^ n2, "is", bin(n1 ^ n2)[2:].count('1'), "bits differ")

