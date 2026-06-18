def find_factors(num):
    if num == 0:
        return "No Factors"
    if num < 0:
        num = -num
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
print(find_factors(0))    
print(find_factors(-12))  
