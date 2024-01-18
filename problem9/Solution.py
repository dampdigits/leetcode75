class Solution:
    def compress(self, chars: List[str]) -> int:
        nums = []
        prev = chars[0]
        repeat = 0
        tmpChars = [prev]

        for ch in chars:
            if ch == prev:
                repeat += 1
            else:
                tmpChars.append(ch)
                nums.append(repeat)
                repeat = 1
            prev = ch
            
        if repeat >= 1:
            nums.append(repeat)

        chars.clear()
        for i in range(len(tmpChars)):
            chars.append(tmpChars[i])
            if nums[i] > 9:
                chars.extend(list(str(nums[i])))
            elif nums[i] != 1:
                chars.append(str(nums[i]))
        
        return len(chars)
