N = int(input("enter a number: "))
n = input("enter all numbers: ")
text_list = n.split()
text = []
for item in text_list:
    number = int(item)
    text.append(number)
k = int(input("enter a no inside the list of arry: "))
text.sort()
ans = text[-k]
print(ans)
