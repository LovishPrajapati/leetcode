from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[i + n])
        return temp



d = Solution()
d.shuffle([2,5,1,3,4,7],3)