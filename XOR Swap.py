print("XOR Swap - exchange 2 values without using a 3rd variable")
a = 5
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
print("After swapping, a =", a, "b =", b)
n1=int(input("Enter a number:"))
n2=int(input("Enter another number:"))
print("Before swapping, n1 =", n1, "n2 =", n2)
n1 = n1 ^ n2
n2 = n1 ^ n2
n1 = n1 ^ n2
print("After swapping, n1 =", n1, "n2 =", n2)
