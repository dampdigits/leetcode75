class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed[:0] = [0]
        flowerbed.append(0)
        
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return n <= 0

    def main(self):
        obj = Solution()
        flowerbed = [1,0,0,0,1]
        n = 2
        print(obj.canPlaceFlowers(flowerbed, n))

if __name__ == "__main__":
    sol = Solution()
    sol.main()

