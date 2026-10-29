def insertion_sort(numbers):
    shifts = 0
    
    # Start from the second element (index 1) up to the end of the list
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        
        # Move elements of numbers[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            shifts += 1  # Record each individual data shift
            j -= 1
            
        # Place the key into its correct sorted slot
        numbers[j + 1] = key
        
    return numbers, shifts
