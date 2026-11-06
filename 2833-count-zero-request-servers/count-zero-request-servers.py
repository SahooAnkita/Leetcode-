from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda log: log[1])

        # Store queries with their original indexes
        sorted_queries = sorted(
            [(query, i) for i, query in enumerate(queries)]
        )

        result = [0] * len(queries)

        # Frequency of requests for each server inside current window
        server_count = {}

        left = 0
        right = 0

        for query, index in sorted_queries:
            start_time = query - x
            end_time = query

            # Add logs whose time <= query
            while right < len(logs) and logs[right][1] <= end_time:
                server_id = logs[right][0]
                server_count[server_id] = server_count.get(server_id, 0) + 1
                right += 1

            # Remove logs whose time < query - x
            while left < right and logs[left][1] < start_time:
                server_id = logs[left][0]

                server_count[server_id] -= 1

                if server_count[server_id] == 0:
                    del server_count[server_id]

                left += 1

            # Servers present in server_count received requests
            active_servers = len(server_count)

            # Remaining servers received no requests
            result[index] = n - active_servers

        return result