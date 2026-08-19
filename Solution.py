from typing import List


class Solution:
    # count occurances in list -> hash
    def hasDuplicate(self, nums: List[int]) ->bool:
        d = {}
        for n in nums:
            d[n] = 0
        for n in nums:
            d[n] += 1
            if d[n] > 1: return True
        return False

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        d = {}

        for c in d:
            d[c] = d.get(c,0) + 1

        for n in t:
            if n not in d.keys(): return False
            d[n] -= 1
        if all((x==0) for x in d.values()): return True
        return False
        

Solution().isAnagram(s = "racecar", t = "carrace")