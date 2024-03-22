class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        combo = []
        
        def backtrack(size, sum):
            if size == k:
                if sum == n:
                    ans.append(combo.copy())
                    return True
                return False

            strt = 1 if not combo else combo[-1]+1
            
            for i in range(strt, 10):
                combo.append(i)
                sum += i
                found = backtrack(size+1, sum)
                sum -= i
                combo.pop(-1)
                if found: break
            return False

        backtrack(0, 0)
        return ans
