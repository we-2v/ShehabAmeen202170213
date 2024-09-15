# ShehabAmeen202170213

```markdown
# Depth-First Search (DFS) Path Finder

This Python script finds a path between two nodes in a graph using the Depth-First Search (DFS) algorithm. The graph is represented as an adjacency list using a dictionary.

## Graph Structure

The graph is defined in the script as follows:

```python
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': ['3'],
    '4': ['8'],
    '8': ['4', '7']
}
```

## How It Works

1. **Function `dfs_path`**:
    - Takes the graph, a start node, and a goal node as inputs.
    - Uses recursion to explore each node and its neighbors.
    - Tracks the path from the start node to the goal node.
    - Returns the path if the goal is reached, otherwise returns `None`.

2. **User Input**:
    - The script prompts the user to enter the start and end nodes.
    - It then prints the path if one is found, or a message indicating that no path exists.

## Usage

To run the script, simply execute it in a Python environment. You will be prompted to input the start and end nodes, and the script will display the path if one exists.

### Example

```
Enter the start node: 2
Enter the end node: 8
Path from 2 to 8:
2 -> 3 -> 4 -> 8
```

### No Path Found

If there's no valid path between the specified nodes:

```
Enter the start node: 7
Enter the end node: 2
Path from 7 to 2:
No path found
```

## Requirements

- Python 3.x

## Notes

- The graph is hardcoded within the script. You can modify the graph dictionary to test different scenarios.
- The script assumes that all nodes are represented as strings.

Feel free to modify the graph and experiment with different start and end nodes!
```
