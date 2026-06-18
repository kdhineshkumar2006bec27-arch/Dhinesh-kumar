num = int(input("enter a number: "))
n = [int(x) for x in input("enter all numbers: ").split()]
total = 1
for x in n:
    total = total * x
answer = []
for x in n:
    answer.append(total // x)
print(*answer)
