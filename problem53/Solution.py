# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        beg, end = 1, n
        while True:
            mid = (beg + end) // 2
            feedback = guess(mid)
            if feedback == 0: return mid
            if feedback == 1: beg = mid+1
            else: end = mid-1
