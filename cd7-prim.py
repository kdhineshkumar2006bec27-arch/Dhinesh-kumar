start = 10
end = 20
for current_number in range(start, end + 1):
     if current_number < 2:
         continue
     mistakes_found = 0
     for tester in range(2, current_number):
        remainder = current_number % tester
        if remainder == 0:
            mistakes_found = mistakes_found + 1
     if mistakes_found == 0:
         print(current_number)
