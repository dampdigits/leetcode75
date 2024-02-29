class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys, n = [0], len(rooms)
        visited = [False] * n
        visited[0] = True
        
        for key in keys:
            for k in rooms[key]:
                if not visited[k]:
                    keys.append(k)
                    visited[k] = True
        
        return len(keys) == n
