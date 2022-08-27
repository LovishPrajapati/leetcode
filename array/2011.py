# There is a programming language with only four operations and one variable X:
#
# ++X and X++ increments the value of the variable X by 1.
# --X and X-- decrements the value of the variable X by 1.
# Initially, the value of X is 0.
#
# Given an array of strings operations containing a list of operations, return the final value of X after performing all
# the operations.
from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0
        for op in operations:
            if op == '++X' or op == 'X++':
                num = num + 1
            elif op == '--X' or op == 'X--':
                num = num - 1
        return num


d = Solution()
t = d.finalValueAfterOperations(operations=["--X", "X++", "X++"])
print(t)
