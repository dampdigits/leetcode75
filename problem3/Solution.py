class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        arr=[]
        big = max(candies)
        for candy in candies:
            if candy + extraCandies >= big:
                arr.append(True)
            else:
                arr.append(False)
        return arr

    def main(self):
        obj = Solution()
        candies = [2,3,5,1,3]
        extraCandies = 3
        print(obj.kidsWithCandies(candies, extraCandies))

if __name__ == "__main__":
    sol = Solution()
    sol.main()
