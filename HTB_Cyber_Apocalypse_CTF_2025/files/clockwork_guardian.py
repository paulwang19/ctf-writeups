
def calculate_shortest_path(maze, x, y):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1 or maze[x][y] == 'P':
        return float('inf')
    if maze[x][y] == 'E':
        return 1
    
    maze[x][y] = 'P'
    up_shortest_path = calculate_shortest_path(maze, x - 1, y)
    down_shortest_path = calculate_shortest_path(maze, x + 1, y)
    left_shortest_path = calculate_shortest_path(maze, x, y - 1)
    right_shortest_path = calculate_shortest_path(maze, x, y + 1)
    maze[x][y] = 0
    
    return 1 + min(up_shortest_path, down_shortest_path, left_shortest_path, right_shortest_path)

def main():
    maze = eval(input())
    shortest_path_length = calculate_shortest_path(maze, 0, 0)
    print(shortest_path_length - 1)

main()