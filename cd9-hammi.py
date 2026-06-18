num1 = int(input("enter a  first number: "))
num2 = int(input("enter a second number"))
xor=num1^num2
binary=bin(xor)
hamming_distance = binary.count('1')
print(hamming_distance)
