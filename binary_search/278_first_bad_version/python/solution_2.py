class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        ans = -1
        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if isBadVersion(mi):
                ans = mi
                hi = mi - 1
            else:
                lo = mi + 1
        return ans
