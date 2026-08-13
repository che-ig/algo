class Solution:
    # time: O(n + m)
    # mem: O(min(n, m))
    def intersect(self, A, B):
        p1 = 0
        p2 = 0
        res = []
        # т к мы можем иметь дубликаты то на каждой итерации сравниваем на
        # равестно и если равны двигаем оба указателя и прибавляем ответ
        # иначе двигаем указатель который указывает на меньшее значение
        while p1 < len(A) and p2 < len(B):
            if A[p1] > B[p2]:
                p2 += 1
            elif A[p1] < B[p2]:
                p1 += 1
            else:
                res.append(A[p1])
                p1 += 1
                p2 += 1
        return res
