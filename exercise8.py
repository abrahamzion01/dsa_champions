def has_duplicates(numbers):
    seen = set()
    for num in numbers:
        if num in seen:
            return True
        seen.add(num)
    return False
print(has_duplicates([1, 2, 3, 4]))