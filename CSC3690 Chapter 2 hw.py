from collections import deque

def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for child in (2 * node, 2 * node + 1):
            if child not in visited:
                visited.add(child)
                queue.append(path + [child])
    return None

result = bfs(1, 11)
print(f"Path from 1 to 11: {result}")