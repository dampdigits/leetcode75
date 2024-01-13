from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        hcf = gcd(len(str1), len(str2))
        ans = str1[:hcf] if len(str1) < len(str2) else str2[:hcf]
        if ans in str1 and ans in str2:
            return ans
        return ""
