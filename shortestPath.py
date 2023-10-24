INF = float('inf')

def floydWarshall(graph, start, end):
    n = len(graph)
    distances = list(map(lambda i: list(map(lambda j: j, i)), graph))
    pred = [[None for _ in range(n)] for _ in range(n)]

    for k in range(n-1, -1, -1):
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    pred[i][j] = k

    printSolution([start] + shortestPath(pred, start, end), distances[start][end])

def shortestPath(pred, i, j):
    if pred[i][j] == None:
        return [j]
    else:
        return shortestPath(pred, i, pred[i][j]) + shortestPath(pred, pred[i][j], j)

def printSolution(path, shortestDistance):
    print("Jalur Optimum:", " -> ".join(chr(vertex + ord('A')) for vertex in path))
    print("Biaya Optimum:", shortestDistance)

if __name__ == "__main__":
    graph = [
        [0, 13, 6, 9, 22, INF, INF, INF, INF, INF],
        [INF, 0, INF, INF, 11, INF, 12, INF, INF, INF],
        [INF, INF, 0, INF, INF, 6, INF, INF, INF, INF],
        [INF, INF, INF, 0, INF, 6, INF, 24, 20, INF],
        [INF, INF, INF, INF, 0, INF, 2, INF, INF, INF],
        [INF, INF, INF, INF, INF, 0, 12, 21, 16, INF],
        [INF, INF, INF, INF, INF, INF, 0, INF, INF, 2],
        [INF, INF, INF, INF, INF, INF, INF, 0, INF, 5],
        [INF, INF, INF, INF, INF, INF, INF, INF, 0, 3],
        [INF, INF, INF, INF, INF, INF, INF, INF, INF, 0]
    ]

    floydWarshall(graph, 0, 9)
