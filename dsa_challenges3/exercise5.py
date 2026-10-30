def merge_intervals(intervals):
    if not intervals:
        return []
        
    # Sort the intervals by their starting points
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        # Get the end time of the last interval we added to our merged list
        last_added_end = merged[-1][1]
        
        # If the current interval's start is less than or equal to the last end, they overlap
        if current[0] <= last_added_end:
            # Extend the end of the last added interval if the current one finishes later
            merged[-1][1] = max(last_added_end, current[1])
        else:
            # If they don't overlap, it's a completely new interval sequence
            merged.append(current)
            
    return merged
