# Graph representation using a dictionary where keys are nodes and values are lists of adjacent nodes
graph = {
     '5' : [ '3' ,  '7' ],
     '3' : [ '2' ,  '4' ],
     '7' : [ '8' ],
     '2' : [ '3' ],
     '4' : [ '8' ],
     '8' : [ '4' ,  '7' ]
}
# Function to find a path between two nodes using DFS
def dfs_path(graph, start, goal, path=None):
    # Initialize the path as an empty list if not provided
    if path is None:
        path = []

    # Add the current node to the path
    path = path + [start]

    # If the current node is the goal, return the path
    if start == goal:
        return path

    # Return None if the current node is not in the graph
    if start not in graph:
        return None

    # Iterate over neighbors of the current node
    for node in graph[start]:
        # If the neighbor has not been visited
        if node not in path:
            # Recursively search the neighbor
            new_path = dfs_path(graph, node, goal, path)
            # Return the path if found
            if new_path:
                return new_path

    # Return None if no path is found
    return None

# Driver code
# Get start and end nodes from the user
start_node = input("Enter the start node: ")
end_node = input("Enter the end node: ")

# Print the initial message
print(f"Path from {start_node} to {end_node}:")

# Find the path using DFS
path = dfs_path(graph, start_node, end_node)

# Print the path if found
if path:
    print(" -> ".join(path))
else:
    # Print a message if no path is found
    print("No path found")
