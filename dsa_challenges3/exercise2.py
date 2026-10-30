def longest_consecutive(numbers):
    # Convert list to a set for O(1) lookups
    num_set = set(numbers)
    longest_streak = 0
    
    for num in num_set:
        # Check if this number is the start of a sequence
        # (It's a start if the number right before it isn't in the set)
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # Keep counting the consecutive chain
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            # Update the longest streak found so far
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak
