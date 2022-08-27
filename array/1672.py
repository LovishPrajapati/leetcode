from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for customers in accounts:
            currMax = 0
            for bank in customers:
                currMax = currMax + bank

            richest = max(richest, currMax)

        return richest


d = Solution()
print(d.maximumWealth([[1,2,3],[3,2,1]]))
