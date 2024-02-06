class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for i in arr:
            if i in occurrences:
                occurrences[i] += 1
            else:
                occurrences[i] = 1
        return len(occurrences.values()) == len(set(occurrences.values()))