class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Проверка на пустой массив (хотя по условиям задачи длина >= 1)
        if not nums:
            return 0

        # i - указатель на последний уникальный элемент
        # Начинаем с 0, так как nums[0] всегда уникален
        i = 0

        # j - быстрый указатель, пробегает по массиву
        # Начинаем с 1, так как nums[0] уже учтен
        for j in range(1, len(nums)):
            # Если нашли элемент, отличный от последнего уникального
            if nums[j] != nums[i]:
                # Сдвигаем i вправо (освобождаем место для нового уникального)
                i += 1
                # Записываем новый уникальный элемент
                nums[i] = nums[j]

        # Возвращаем количество уникальных элементов (i + 1, так как индексация с 0)
        return i + 1


# --- Проверка ---
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print(f"k = {k1}, nums = {nums1[:k1]}")

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print(f"k = {k2}, nums = {nums2[:k2]}")
