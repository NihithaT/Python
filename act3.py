n=int(input("Enter a number:"))
result=(n>>2)&1
if result:
    print(n, "binary:", bin(n)[2:], "bit at position 2 is set")
else:
    print(n, "binary:", bin(n)[2:], "bit at position 2 is not set")
    