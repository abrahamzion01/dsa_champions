def most_frequent(numbers):
    # Handle the empty list edge case
    if not numbers:
        return None
        
    # Dictionary to store the frequency of each number
    frequency_map = {}
    
    # List to store the order of first appearances
    first_appearance_order = []
    
    # Step 1: Build the frequency map and track the first appearance order
    for num in numbers:
        if num not in frequency_map:
            frequency_map[num] = 0
            first_appearance_order.append(num)
        frequency_map[num] += 1
        
    # Step 2: Find the number with the highest frequency
    max_count = 0
    result = None
    
    # Iterating in order of first appearance automatically breaks ties correctly
    for num in first_appearance_order:
        if frequency_map[num] > max_count:
            max_count = frequency_map[num]
            result = num
            
    return result
