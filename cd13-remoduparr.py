def remove_duplicates(arr):
    unique_elements = []
    for item in arr:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
input_array = [1, 2, 2, 4, 4, 5, 6, 7, 7]
result = remove_duplicates(input_array)
print(*result)  
