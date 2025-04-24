def find_min_communication_energy():
    
    N = int(input().strip())

    
    graph = {}

    
    for _ in range(N):
        k, m = map(int, input().split())  
        members = list(map(int, input().split()))  

        
        for i in members:
            if i not in graph:
                graph[i] = {}  
            for j in members:
                if i != j:
                    if j not in graph[i]:
                        graph[i][j] = m
                    else:
                        graph[i][j] = min(graph[i][j], m)  

    
    A, B = map(int, input().split())

    
    visited = set()
    energy = {node: float('inf') for node in graph}  

    if A not in graph or B not in graph:
        print(-1)  
        return
    
    energy[A] = 0  

    while True:
        
        min_energy = float('inf')
        current = None
        for node in graph:
            if node not in visited and energy[node] < min_energy:
                min_energy = energy[node]
                current = node

        if current is None or current == B:
            break  

        visited.add(current)  

        
        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                energy[neighbor] = min(energy[neighbor], energy[current] + cost)

    print(energy[B] if energy[B] != float('inf') else -1)


find_min_communication_energy()




