from collections import Counter
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)
        for x in sorted(count):
            freq = count[x]
            if freq > 0:
                # try to form freq groups starting at x
                for v in range(x, x + k):
                    count[v] -= freq
                    if count[v] < 0:
                        return False
        return True
