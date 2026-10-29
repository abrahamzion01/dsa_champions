def first_position(numbers, target):
    low = 0
    high = len(numbers) - 1
    result = -1  # Default value if target is not found
    
    while low <= high:
        mid = (low + high) // 2
        
        if numbers[mid] == target:
            result = mid       # Record the index as a potential answer
            high = mid - 1     # Keep searching to the left for an even earlier occurrence
        elif numbers[mid] < target:
            low = mid + 1      # Target is in the right half
        else:
            high = mid - 1     # Target is in the left half
            
    return result
