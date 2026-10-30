def has_cycle(graph):
    # Tracks nodes that have been completely explored in the past
    visited = set()
    # Tracks nodes in the current active recursion/exploration stack
    rec_stack = set()

    def dfs(node):
        # If the node is in the current path, we found a cycle!
        if node in rec_stack:
            return True
        # If the node was already completely verified in the past, skip it
        if node in visited:
            return False

        # Add the node to the current active path
        rec_stack.add(node)

        # Explore all neighbors recursively
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        # Backtrack: remove the node from the active path once we finish exploring its neighbors
        rec_stack.remove(node)
        # Mark the node as fully processed so we never waste time recalculating it
        visited.add(node)
        
        return False

    # The graph might have disconnected components, so we must check every node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False
