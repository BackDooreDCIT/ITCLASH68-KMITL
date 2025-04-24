def main():
    
    M, N = map(int, input().split())

    
    grid = []
    for _ in range(M):
        grid.append(list(map(int, input().split())))

    
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    
    def dfs(x, y):
        stack = [(x, y)]
        size = 0
        
        while stack:
            cx, cy = stack.pop()
            if grid[cx][cy] == 1:
                grid[cx][cy] = 0  
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < M and 0 <= ny < N and grid[nx][ny] == 1:
                        stack.append((nx, ny))
        return size

    max_size = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:  
                max_size = max(max_size, dfs(i, j))

    print(max_size)


main()




