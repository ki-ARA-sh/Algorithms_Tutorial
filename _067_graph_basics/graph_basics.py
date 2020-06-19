from queue import Queue


# finding distance of every vortex from a given vortex r by BFS
def bfs(r, n, adj):
    inf_val = float('inf')
    distance = [inf_val] * n
    q = Queue()
    distance[r] = 0
    q.put(r)
    while q.qsize():
        v = q.get()
        for u in adj[v]:
            if distance[u] > distance[v] + 1:
                distance[u] = distance[v] + 1
                q.put(u)
    return distance


# finding the cycle in a given graph with minimum length using BFS tree
def bfs_back(r, n, adj, deleted):
    inf_val = float('inf')
    distance = [inf_val] * n
    q = Queue()
    distance[r] = 0
    q.put(r)
    while q.qsize():
        v = q.get()
        for u in adj[v]:
            if (v == r) and (u == deleted):
                continue
            if distance[u] > distance[v] + 1:
                distance[u] = distance[v] + 1
                q.put(u)
    return distance


def solve_back(n, adj):
    result = float('inf')
    for i in range(n):
        for u in adj:
            distances = bfs(i, n, adj, u)
            result = min(result, distances[u] + 1)
    return result



# finding connected components by DFS
def dfs(v, L, mark, adj):
    mark[v] = True
    for u in adj[v]:
        if not mark[u]:
            dfs(u, L, mark, adj)
    pass


def solve(n, adj):
    mark = [False] * n
    connected_components = []
    for i in range(n):
        if not mark[i]:
            component = []
            dfs(i, component, mark, adj)
            connected_components.append(component)
    return connected_components


# finding whether a given graph has cycle or not by DFS (DFS tree to be exact)
def dfs_cyle(v, dad, mark, adj):
    mark[v] = True
    result = False
    for u in adj[v]:
        if not mark[u]:
            result = result or dfs_cyle(u, v, mark, adj)
        elif u != dad:
            result = True
    return result


# finding whether a given graph is bipartite or not by DFS
def dfs_bipartite(v, dad, color, mark, adj):
    if dad != -1:
        color[v] = 1 - color[dad]
    else:
        color[v] = 1
    mark[v] = True
    for u in adj[v]:
        if not mark[u]:
            dfs_bipartite(u, v, color, mark, adj)
        elif color[v] == color[u]:
            return False
    return True


