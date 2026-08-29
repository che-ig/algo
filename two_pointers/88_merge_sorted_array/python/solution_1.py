class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Не возвращаем результат, а изменяем nums1 in-place.
        """
        # Указатели:
        # i - последний полезный элемент в nums1 (позиция m-1)
        # j - последний элемент в nums2 (позиция n-1)
        # k - последняя позиция в nums1 (позиция m+n-1)
        i = m - 1
        j = n - 1
        k = m + n - 1

        # Пока оба массива имеют элементы для сравнения
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                # nums1[i] больше — ставим его в конец
                nums1[k] = nums1[i]
                i -= 1
            else:
                # nums2[j] больше или равен — ставим его в конец
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Если в nums2 остались элементы, копируем их в начало.
        # (Если остались в nums1 — они уже на месте, ничего делать не нужно)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


# --- Проверка на примерах ---
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    sol.merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)  # [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    sol.merge(nums1, 1, [], 0)
    print(nums1)  # [1]

    nums1 = [0]
    sol.merge(nums1, 0, [1], 1)
    print(nums1)  # [1]
