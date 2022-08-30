from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) - i - 1):
                if nums[i] == nums[j + i]:
                    count = count + 1
        return count

d = Solution()
print(d.numIdenticalPairs([1,2,3]))