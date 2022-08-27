from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxcount = 0
        for sentence in sentences:
            maxcount = max(maxcount, len(sentence.split(" ")))
        return maxcount

d = Solution()
print(d.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))
