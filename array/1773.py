from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    count = count + 1
            if ruleKey == "color":
                if item[1] == ruleValue:
                    count = count + 1
            if ruleKey == "name":
                if item[2] == ruleValue:
                    count = count + 1

        return count

d = Solution()
print(d.countMatches(items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
