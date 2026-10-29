def find_number(numbers, target):
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1
print(find_number( numbers = [10, 20, 30], target = 99))