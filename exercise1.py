def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
print(find_largest([3, 41, 56, 21, 76, 9]))