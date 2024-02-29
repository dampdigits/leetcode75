class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, provinces = len(isConnected), 0
        visited = [False] * n

        def visit(city):
            visited[city] = True
            for i in range(n):
                if (isConnected[city][i]) and (not visited[i]): visit(i)
        
        for city in range(n):
            if not visited[city]:
                provinces += 1
                visit(city)
        
        return provinces
