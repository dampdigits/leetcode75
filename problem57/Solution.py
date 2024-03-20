class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        ans, combination = [], ""
        map = { '2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        
        def combine(num, combination, ans):
            if not num:
                ans.append(combination)
                return

            letters = map[num[0]]
            for l in letters:
                combine(num[1:], combination + l, ans)

        combine(digits, "", ans)
        return ans
