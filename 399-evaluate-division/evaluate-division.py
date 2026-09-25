class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        graph = {}

        # Build the graph
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(current, target, visited):

            # Target found
            if current == target:
                return 1.0

            visited.add(current)

            for neighbor, weight in graph[current]:
                if neighbor in visited:
                    continue

                result = dfs(neighbor, target, visited)

                if result != -1.0:
                    return weight * result

            return -1.0

        answers = []

        for start, end in queries:

            # Undefined variables
            if start not in graph or end not in graph:
                answers.append(-1.0)
                continue

            if start == end:
                answers.append(1.0)
                continue

            result = dfs(start, end, set())
            answers.append(result)

        return answers