from collections import deque


def dfs(graph, start, visited=None):#глубина
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['2', '5']),
         '2': set(['1', '3', '4', '5']),
         '3': set(['2', '4']),
         '4': set(['2', '3', '5']),
         '5': set(['1', '2', '4'])}

dfs(graph, '1')


def bfs(graph, start):#ширина
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    '1': ['2', '5'],
    '2': ['1', '3', '4', '5'],
    '3': ['2', '4'],
    '4': ['2', '3', '5'],
    '5': ['1', '2', '4']
}
bfs(graph, '1')
