from typing import List


class Solution:
    #num occurances in list -> hash
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            d[n] = 0
        for n in nums:
            d[n] += 1
            if d[n] > 1:
                return True

        return False




nums = [1, 2, 3, 3]
print(Solution().hasDuplicate(nums))