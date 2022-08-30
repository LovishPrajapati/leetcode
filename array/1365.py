from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] < num:
                    count = count + 1

            result.append(count)

        return result

d = Solution()
print(d.smallerNumbersThanCurrent([8,1,2,2,3]))
