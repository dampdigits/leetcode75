class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowelList = []
        ans = list(s)
        for ch in s:
            if ch in vowels:
                vowelList.append(ch)
        
        for i in range(len(ans)):
            if ans[i] in vowels:
                ans[i] = vowelList.pop()
        return "".join(ans)
