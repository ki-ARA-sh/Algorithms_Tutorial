import sys
sys.setrecursionlimit(10**6)


def vertices_connect(vertices, v1, v2):
    return (vertices[v1][0] == vertices[v2][0]) or (vertices[v1][1] == vertices[v2][1])


def dfs(v, L, mark, vertices):
    mark[v] = True
    for u in range(len(vertices)):
        if vertices_connect(vertices, u, v) and (not mark[u]):
            dfs(u, L, mark, vertices)
    pass


def main():
    n = int(input())
    vertices = [None] * n
    for i in range(n):
        x, y = map(int, input().split())
        vertices[i] = (x, y)
    result = -1
    mark = [False] * n
    for i in range(n):
        if not mark[i]:
            component = []
            dfs(i, component, mark, vertices)
            result += 1
    print(result)


if __name__ == '__main__':
    main()