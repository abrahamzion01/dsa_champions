def move_zeros(numbers):
    nonzeros = [n for n in numbers if n != 0]
    zeros = [0] * numbers.count(0)
    return nonzeros + zeros
print(move_zeros([1,0, 2, 3]))