from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = []
        arr.append(first)
        for i in range(len(encoded)):
            arr.insert(i + 1, encoded[i] ^ arr[i])

        return arr


d = Solution()
print(d.decode([1, 2, 3], 1))
