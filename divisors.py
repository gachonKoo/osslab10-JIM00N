import sys

number = int(input(sys.argv[0]))

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
