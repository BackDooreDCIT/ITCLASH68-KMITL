def main():
    
    N, M = map(int, input().split())
    edges = [[] for _ in range(N + 1)]  
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges[u].append((w, v))
        edges[v].append((w, u))
    
    start = int(input())

    
    visited = [False] * (N + 1)
    min_cost = 0
    pq = [(0, start)]  
    count = 0
    
    while pq and count < N:
        
        pq.sort()
        w, u = pq.pop(0)

        if visited[u]:
            continue
        
        
        visited[u] = True
        min_cost += w
        count += 1

        for nw, v in edges[u]:
            if not visited[v]:
                pq.append((nw, v))
    
    
    print(min_cost if count == N else -1)

main()



