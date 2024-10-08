#!/usr/bin/python3

def canUnlockAll(boxes):
    visited = set()
    stack = [0]
    
    while stack:
        box = stack.pop()
        
        if box not in visited:
            visited.add(box)
            
            for key in boxes[box]:
                if key not in visited and key < len(boxes):
                    stack.append(key)
    
    return len(visited) == len(boxes)

