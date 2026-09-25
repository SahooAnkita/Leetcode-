class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        graph = [[] for _ in range(n)]

        for a, b in connections:
            # Original direction: a -> b
            graph[a].append((b, 1))

            # Reverse direction for traversal: b -> a
            # No change needed
            graph[b].append((a, 0))

        visited = set()

        def dfs(city):
            visited.add(city)
            changes = 0

            for next_city, cost in graph[city]:
                if next_city not in visited:
                    changes += cost
                    changes += dfs(next_city)

            return changes

        return dfs(0)