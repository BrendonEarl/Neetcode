from multiprocessing.connection import answer_challenge
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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use dic for hash, use set for O(1) lookup for "is in set"
        d = {}
        s = set()

        for i, n in enumerate(nums):
            d[n] = d.get(n, i)
            if ((x := target - n) in s):
                return sorted([d[x], i])
            s.add(n)


        

Solution().twoSum(nums = [3,4,5,6], target = 7)