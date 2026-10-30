def valid_parentheses(text):
    stack = []
    # Map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in text:
        # If it's a closing bracket
        if char in mapping:
            # Pop the top element from stack if it's not empty, else use a dummy value
            top_element = stack.pop() if stack else '#'
            
            # The popped bracket must match the required opening bracket
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
            
    # If the stack is empty, all brackets were properly matched
    return len(stack) == 0
