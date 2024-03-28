class Solution:
    def successfulPairs(self, spells, potions, success) :
        n, m = len(spells), len(potions)
        potions.sort(reverse=True) # descending order
        # indices of spells sorted in ascending order
        indices = sorted(range(len(spells)), key=lambda i:spells[i])
        pairs, start, i = [0]*n, 0, 0

        for index in range(n):
            i = indices[index]
            for j in range(start, m):
                if (spells[i] * potions[j]) < success:
                    pairs[i] = j
                    break
            else: # If no pair failed then all the remaining spells will successfully pair with every potion
                while index < n:
                    pairs[indices[index]] = m
                    index += 1
                break
            start = j
        return pairs

# Algo:
# sort potions in descending order
# create a list for indices of spells sorted in ascending order
# start making products using the smallest of spells and largest of potions
# mark the first potion that produces product < success
# for the next spell start from the marked potion
# if the last potion is reached then all the remaining spells will successfully pair with every potion
