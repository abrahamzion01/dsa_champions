def path_exists(graph, start, target):
    # If the start and target are the exact same node, a path naturally exists
    if start == target:
        return True
        
    # Keep track of nodes we have already explored to prevent infinite loops (cycles)
    visited = set([start])
    
    # Use a stack (LIFO) to perform a Depth-First Search (DFS)
    stack = [start]
    
    while stack:
        current = stack.pop()
        
        # Check all direct neighbors of the current node
        for neighbor in graph.get(current, []):
            if neighbor == target:
                return True
                
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                
    return False
