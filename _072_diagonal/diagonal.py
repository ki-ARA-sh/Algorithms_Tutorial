from queue import Queue


def bfs(r, n, adj):
    inf_val = float('inf')
    distance = [(inf_val, -1)] * n
    q = Queue()
    distance[r] = (0, r)
    q.put(r)
    while q.qsize():
        v = q.get()
        for u in adj[v]:
            if distance[u][0] > distance[v][0] + 1:
                distance[u] = (distance[v][0] + 1, u)
                # distance[u][0] = distance[v][0] + 1
                # distance[u][1] = distance[v][1]
                q.put(u)
    return sorted(distance, reverse=True)


def get_diagonal(n, adj):
    distances = bfs(0, n, adj)
    p1 = distances[0]
    distances = bfs(distances[0][1], n, adj)
    return distances[0][0]


def main():
    n = int(input())
    adj = [None] * n
    for i in range(n):
        adj[i] = list()
    for i in range(n - 1):
        x, y = map(int, input().split())
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
    print(get_diagonal(n, adj))



if __name__ == '__main__':
    main()
