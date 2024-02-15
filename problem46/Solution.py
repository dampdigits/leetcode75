class Solution:
    def calcEquation(self, equations, values, queries):
        # Create a weighted graph (dict of dicts)
        graph = {}
        for equation, value in zip(equations, values):
            if equation[0] not in graph:
                graph[equation[0]] = {}
            if equation[1] not in graph:
                graph[equation[1]] = {}
            graph[equation[0]][equation[1]] = value
            # inverse value for a1 / a0
            graph[equation[1]][equation[0]] = 1 / value
        
        visited, valStack = [], [] # list for visited nodes, stack for values

        def dfs(node, target):
            if node == target: return valStack.pop()
            visited.append(node)
            for key, val in graph[node].items():
                if key in visited: continue
                valStack.append(val)
                value = dfs(key, target)
                if value: return value * valStack.pop()
            valStack.pop()
            return 0

        ans = []

        for query in queries:
            visited.clear()
            valStack.append(1)
            if query[0] not in graph or query[1] not in graph:
                ans.append(-1)
            else:
                val = dfs(query[0], query[1])
                ans.append(-1 if val == 0 else val)
        
        return ans
