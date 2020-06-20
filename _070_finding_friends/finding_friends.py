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
    return sorted(distance)


def main():
    n = int(input())
    adj = [None] * n
    for i in range(n):
        adj[i] = list()
    for i in range(n - 1):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    occupied = [False] * n
    q = int(input())
    for i in range(q):
        index = int(input()) - 1
        occupied[index] = True
    distances = bfs(0, n, adj)
    for i in range(n):
        if occupied[distances[i][1]]:
            print(distances[i][1] + 1)
            return


if __name__ == '__main__':
    main()
