class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        # if all workers will be part of the sessions
        if (candidates * 2) >= n:
            costs.sort()
            return sum(costs[:k])
        
        total_cost = 0
        heap = []
        heapq.heapify(heap)
        # Create heap of candidates from beginning and end of list
        for i in range(candidates):
            heappush(heap, (costs.pop(0), 0))
            heappush(heap, (costs.pop(-1), n-1))
        # Remember cost of worker and from which end of list
        cost, index = heappop(heap)
        total_cost += cost
        sessions = 1
        
        for i in range(k-1):
            if not costs: break
            ''' If the last selected worker was from the front of list
                then add worker to heap from the front of the list '''
            if index == 0:
                heappush(heap, (costs.pop(0), 0))
            else: # Otherwise add worker to heap from the end of list
                heappush(heap, (costs.pop(-1), n-1))
            cost, index = heappop(heap)
            total_cost += cost
            sessions += 1
        ''' If no more sessions could be conducted because
            costs was empty and all workers are in heap '''
        while sessions < k:
            cost, index = heappop(heap)
            total_cost += cost
            sessions += 1
        
        return total_cost
