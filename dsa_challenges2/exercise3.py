def balanced_brackets(text):
    # Use a list as a stack to keep track of open brackets (LIFO)
    stack = []
    
    # Map closing brackets to their corresponding opening brackets
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in text:
        # If it's an opening bracket, push it onto the stack
        if char in "([{":
            stack.append(char)
        # If it's a closing bracket, check for a valid match
        elif char in ")]}":
            # Stack cannot be empty, and the top must match the closing bracket
            if not stack or stack[-1] != matching_bracket[char]:
                return False
            stack.pop() # Successfully matched, remove from stack
            
    # The string is balanced only if no unmatched opening brackets remain
    return len(stack) == 0
