class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]
        
        def visitRoom(room):
            for key in rooms[room]:
                if key not in visited:
                    visited.append(key)
                    visitRoom(key)
        
        visitRoom(0)
        return len(visited) == len(rooms)
