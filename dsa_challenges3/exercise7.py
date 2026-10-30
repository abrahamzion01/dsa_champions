def first_unique(text):
    # Stage 1: Count the frequency of every character
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Stage 2: Search the original text sequentially
    for char in text:
        if char_counts[char] == 1:
            return char  # Found the first character that appears exactly once
            
    return None  # Return None if every character has duplicates
