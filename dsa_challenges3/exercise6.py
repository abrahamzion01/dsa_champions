def missing_number(numbers):
    n = len(numbers)
    
    # Calculate what the total sum should be from 0 to n
    expected_sum = (n * (n + 1)) // 2
    
    # Calculate the actual sum of the numbers present in the list
    actual_sum = sum(numbers)
    
    # The difference reveals the missing value
    return expected_sum - actual_sum
