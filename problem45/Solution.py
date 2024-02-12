def minReorder(n, connections) -> int:
    edges = { (a,b) for a,b in connections}
    print(f"edges:\n{edges}")
    neighbours = {city:[] for city in range(n)}
    print(f"neighbours:\n{neighbours}")
    visit = set()
    changes = 0
    

    for a,b in connections:
        neighbours[a].append(b)
        neighbours[b].append(a)
    print(f"neighbours:\n{neighbours}")

    def dfs(city):
        nonlocal edges, neighbours, visit, changes

        for neighbour in neighbours[city]:
            if neighbour in visit:
                continue
            if (neighbour, city) not in edges:
                changes += 1
            visit.add(neighbour)
            dfs(neighbour)

    visit.add(0)
    dfs(0)

    return changes

def main():
    connections = [[4,2],[2,3],[1,0],[1,2]]
    print("reorders = ",minReorder(5, connections))
if __name__ == "__main__":
    main()
