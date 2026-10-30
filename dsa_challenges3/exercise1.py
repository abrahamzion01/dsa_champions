def two_sum(numbers, target):
    seen = {}  # Stores previously seen numbers as keys and their indices as values
    
    for index, num in enumerate(numbers):
        complement = target - num  # What number do we need to reach the target?
        
        # Check if the needed number has already been seen
        if complement in seen:
            return [seen[complement], index]
            
        # If not, store the current number and its index in the dictionary
        seen[num] = index
        
    return None  # Return None if no matching pair exists
