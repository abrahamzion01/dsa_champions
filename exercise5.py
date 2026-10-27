def count_occurrences(numbers, target):
    count = 0
    for num in numbers:
        if num == target:
            count += 1
    return count
print(count_occurrences( numbers = [2, 5, 2, 8, 2], target = 2))