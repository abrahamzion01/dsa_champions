from collections import deque

def reverse_first(queue, k):
    # Handle edge cases: if k is invalid or queue is empty, do nothing
    if k <= 0 or len(queue) == 0 or k > len(queue):
        return queue
        
    stack = []
    
    # Step 1: Dequeue the first k elements and push them onto a stack
    for _ in range(k):
        stack.append(queue.popleft())
        
    # Step 2: Pop from the stack and enqueue back to the queue (this reverses them)
    while stack:
        queue.append(stack.pop())
        
    # Step 3: Rotate the remaining elements to the back of the queue
    remaining_elements = len(queue) - k
    for _ in range(remaining_elements):
        queue.append(queue.popleft())
        
    return queue
