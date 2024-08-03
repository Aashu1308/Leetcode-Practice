from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        def floydWarshall(original: List[str], changed: List[str], cost: List[int]):
            graph, node_id = to_graph(original, changed, cost)
            dist = [row[:] for row in graph]
            n = len(graph)
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            return dist, node_id

        def to_graph(original: List[str], changed: List[str], cost: List[int]):
            nodes = set()
            for o, c in zip(original, changed):
                nodes.add(o)
                nodes.add(c)
            nodes = list(nodes)
            node_id = {node: id for id, node in enumerate(nodes)}
            n = len(nodes)
            graph = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                graph[i][i] = 0
            for o, c, p in zip(original, changed, cost):
                graph[node_id[o]][node_id[c]] = p
            return graph, node_id

        dist, node_id = floydWarshall(original, changed, cost)
        cost = 0
        for i, j in zip(source, target):
            try:
                if dist[node_id[i]][node_id[j]] == float('inf'):
                    return -1
                cost += dist[node_id[i]][node_id[j]]
            except KeyError:
                return -1
        return cost


sol = Solution()
print(
    sol.minimumCost(
        "abcd",
        "abce",
        ["a"],
        ["e"],
        [1000],
    )
)
