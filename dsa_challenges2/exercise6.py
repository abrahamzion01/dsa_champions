def closest_number(numbers, target):
    # Return None if the list is empty
    if not numbers:
        return None
        
    # Assume the first number is the closest to start with
    closest = numbers[0]
    
    for num in numbers:
        # Calculate the absolute distances to the target
        current_distance = abs(num - target)
        closest_distance = abs(closest - target)
        
        # Condition 1: The current number is strictly closer to the target
        if current_distance < closest_distance:
            closest = num
            
        # Condition 2: It's a tie, so pick the smaller number
        elif current_distance == closest_distance:
            if num < closest:
                closest = num
                
    return closest
