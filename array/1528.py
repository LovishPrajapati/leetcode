from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = []
        for i in range(len(s)):
            res.append("")
        for i in range(len(indices)):
            res[indices[i]] = s[i]

        return ''.join(res)


d = Solution()
print(d.restoreString("codeleet",[4,5,6,7,0,2,1,3]))