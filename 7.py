i=2
print("these are even numbers")
while i<=100:
    print(i)
    i+=2

i=1
print("these are odd numbers")
while i<=100:
    print(i)
    i+=2

minimum = int(input(" enter the first number: "))
maximum = int(input(" enter the second number: "))

for Number in range (minimum, maximum + 1):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '')

