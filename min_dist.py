from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        def floydWarshall(edges: List[List[int]]) -> List[List[int]]:
            graph = to_graph(edges)
            dist = [row[:] for row in graph]
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            return dist

        def to_graph(edges: List[List[int]]):
            nodes = set()
            for u, v, _ in edges:
                nodes.add(u)
                nodes.add(v)
            graph = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                graph[i][i] = 0
            for u, v, w in edges:
                graph[u][v] = w
                graph[v][u] = w
            return graph

        dist = floydWarshall(edges)
        city = dict()
        for i in range(n):
            city[i] = []
            for j in range(n):
                if dist[i][j] <= distanceThreshold and i != j:
                    city[i].append(j)
        min_cities = float('inf')
        op = 0
        for i in range(n):
            if len(city[i]) <= min_cities:
                min_cities = len(city[i])
                if i > op:
                    op = i
        return op


sol = Solution()
print(
    sol.findTheCity(
        5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2
    )
)
