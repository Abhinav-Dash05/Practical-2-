# finding the sum of digits of the given number

n = input("Enter number: ")
result = 0
l = len(n)

for x in n:
    z = int(x[0])
    result = result+z

print(result)
