def move_zeros(numbers):
    # This pointer tracks where the next non-zero number should go
    write_index = 0
    
    # Step 1: Scan the list and shift all non-zero numbers to the front
    for num in numbers:
        if num != 0:
            numbers[write_index] = num
            write_index += 1
            
    # Step 2: Fill the remaining slots at the end of the list with zeros
    for i in range(write_index, len(numbers)):
        numbers[i] = 0
