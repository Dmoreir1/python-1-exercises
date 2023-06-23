def add_numbers(array):
    sum = 0
    for i in array:
        sum += float(i)
    return sum




array = [1.0, 1.1, "1"]
result = add_numbers(array)
print(result)