print("XOR sign detection - m XOR n < 0 means different signs, m XOR n >= 0 means same signs")
n=int(input("Enter a number:"))
m=int(input("Enter another number:"))
print("m XOR n =", m ^ n, "binary representation of", m ^ n, "is", bin(m ^ n)[2:])
if m ^ n < 0:
    print(m, "and", n, "have different signs")
else:
    print(m, "and", n, "have same signs")
