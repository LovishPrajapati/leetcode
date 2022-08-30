from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        if len(nums) != len(index):
            return

        for i in range(len(nums)):
            result.insert(index[i], nums[i])

        return result

d = Solution()
print(d.createTargetArray([0,1,2,3,4],[0,1,2,2,1]))
