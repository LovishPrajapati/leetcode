from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums) - 1,2):
            freq, val = nums[i], nums[i + 1]
            for j in range(freq):
                result.append(val)
        return result


d = Solution()
print(d.decompressRLElist([1, 2, 3, 4]))
