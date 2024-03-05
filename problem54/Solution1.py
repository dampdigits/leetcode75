class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res, m = [], len(potions)
        potions.sort()
        for spell in spells:
            req = math.ceil(success/spell)
            res.append(m - bisect.bisect_left(potions, req))
        return res
