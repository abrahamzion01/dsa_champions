def reverse_list(items):
    result = []
    for item in items:
        result.insert(0, item)
    return result
print(reverse_list( [1, 2, 3, 4]))