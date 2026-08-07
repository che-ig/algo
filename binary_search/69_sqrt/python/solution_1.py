class Solution:
    # time: O(log n)
    # mem:  O(1)
    def mySqrt(self, x: int) -> int:
        def good(i: int):
            return i * i <= x

        # Note: работаем именно с целыми числами
        # если работать с не целыми, то получим неточный ответ
        # из-за накаплавающейся неточности во float
        l, r = 0, x + 1
        while r - l > 1:
            m = (l + r) // 2
            if good(m):
                l = m
            else:
                r = m
        return l
