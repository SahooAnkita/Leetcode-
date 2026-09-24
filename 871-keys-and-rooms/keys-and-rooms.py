class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        visited = set()

        def dfs(room):
            if room in visited:
                return

            visited.add(room)

            for key in rooms[room]:
                dfs(key)

        dfs(0)

        return len(visited) == len(rooms)