print("XOR all numbers - the odd one stays")
print("list:[2,2, 4,4, 3, 7,7]")
print("odd one:", 2^2^4^4^3^7^7, "binary representation of", 2^2^4^4^3^7^7, "is", bin(2^2^4^4^3^7^7)[2:])
n=int(input("Enter a number:"))
l1=[5,5, 7,7, n, 9,9]
result=0
for i in l1:
    result=result^i
print("odd one in list:", result)
