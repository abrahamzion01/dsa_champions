from collections import deque

def shortest_path(graph, start, target):
    # If the start is already the target, the path is just the start node
    if start == target:
        return [start]
        
    # Queue stores tuples of (current_node, path_taken_to_reach_it)
    queue = deque([(start, [start])])
    
    # Track visited nodes to prevent infinite loops
    visited = {start}
    
    while queue:
        current_node, path = queue.popleft()
        
        # Explore all neighbors of the current node
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                # If we find the target, return the completed path immediately
                if neighbor == target:
                    return path + [neighbor]
                    
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    return None  # Return None if no path exists between start and target
