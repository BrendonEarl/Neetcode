from collections import defaultdict
from math import floor
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #defaultdict() no error on accessing keys that don't exist
        #use frequency array converted to tuple (tuple because it's immutable and can be used a a dict key) to hash
        d = defaultdict(list)

        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            d[tuple(freq)].append(s)
        return list(d.values())

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #works when answers are unique. Edge cases aren't solved
        d = defaultdict(int)

        for n in nums:
            d[n] += 1

        top = sorted(d.values())[::-1][:k]
        answ = []
        for v in d.keys():
            if d[v] in top:
                answ.append(v)
        return answ

    def encode(self, strs: List[str]) -> str:
        send = ''

        for s in strs:
            send += str(len(s))
            send += '.'
        send += '|'
        for w in strs:
            send += w
        return send

    def decode(self, s: str) -> List[str]:
        send = []
        sizes, stream = s.split('|', 1)
        sizes = [int(x) for x in sizes.split('.')[:-1]]

        point = 0
        for size in sizes:
            word = ''
            for i in range(size):
                word += stream[point]
                point += 1
            send.append(word)
        return send

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #use suffix and prefix. if there were no inverse to multiplication, this is the only way
        x = len(nums)
        l,r = [],[]
        prd = 1
        for n in nums:
            prd *= n
            l.append(prd)
        prd = 1
        for n in nums[::-1]:
            r.append(prd)
            prd *= n
        r = r[::-1]
        ans=[r[0]]
        for i in range(1,x):
            ans.append(l[i-1]*r[i])
        return ans
        # prd = 1
        # cz = 0
        # for n in nums:
        #     if n==0:
        #         cz += 1
        #     else:
        #         prd *= n
        #
        # if cz > 1:
        #     return [0 for _ in nums]
        # if cz == 1:
        #     return [(prd if x==0 else 0) for x in nums]
        # return [prd//y for y in nums]

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [defaultdict(int) for _ in board]
        cols = [defaultdict(int) for _ in board]
        boxes = [defaultdict(int) for _ in board]

        calc = lambda r,c : ((int(floor(r/3)) * 3) + (int(floor(c/3))))

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val != '.':
                    rows[r][val] += 1
                    cols[c][val] += 1
                    boxes[calc(r,c)][val] += 1
        return all([all(all(k<2 for k in j.values()) for j in l) for l in [rows,cols,boxes]])


Solution().isValidSudoku(board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])

Solution().isValidSudoku([["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])