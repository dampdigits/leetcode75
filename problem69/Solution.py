class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while c > 0:
            if (c&1) == 0:
                flips += (a&1) + (b&1)
            elif ((a&1) | (b&1)) == 0:
                flips += 1
                
            c >>= 1
            a >>= 1
            b >>= 1
        
        while a > 0 or b > 0:
            flips += (a&1) + (b&1)
            a >>= 1
            b >>= 1
        
        return flips
