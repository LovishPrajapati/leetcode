from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = candies[0]
        for candy in candies:
            maxCandies = max(maxCandies, candy)

        result = [True if candy+extraCandies >= maxCandies else False for candy in candies]
        return result

d = Solution()
print(d.kidsWithCandies([2,3,5,1,3],3))