def second_largest(numbers):
    # Initialize both tracking variables to None
    largest = None
    sec_largest = None

    for num in numbers:
        # Step 1: Update largest and bump old largest to second largest
        if largest is None or num > largest:
            sec_largest = largest
            largest = num
        # Step 2: Update second largest only if the number is distinct and bigger
        elif num != largest and (sec_largest is None or num > sec_largest):
            sec_largest = num

    return sec_largest
