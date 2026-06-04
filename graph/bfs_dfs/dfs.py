#dfs recursion when graph is adjacency matrix
def dfs_matrix(matrix, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    print(node, end=' ')  # Process the node
    
    n = len(matrix)
    # Check all possible neighbors by scanning the row
    for neighbor in range(n):
        # matrix[node][neighbor] == 1 means there's an edge
        if matrix[node][neighbor] == 1 and neighbor not in visited:
            dfs_matrix(matrix, neighbor, visited)
    
    return visited

# Example graph as adjacency matrix
#     0  1  2  3  4  5
matrix = [
    [0, 1, 1, 0, 0, 0],  # 0 → 1, 2
    [1, 0, 0, 1, 1, 0],  # 1 → 0, 3, 4
    [1, 0, 0, 0, 0, 1],  # 2 → 0, 5
    [0, 1, 0, 0, 0, 0],  # 3 → 1
    [0, 1, 0, 0, 0, 1],  # 4 → 1, 5
    [0, 0, 1, 0, 1, 0],  # 5 → 2, 4
]

dfs_matrix(matrix, 0)
# Output: 0 1 3 4 5 2