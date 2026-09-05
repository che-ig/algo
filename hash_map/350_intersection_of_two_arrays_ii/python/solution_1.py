class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Сортируем оба массива для использования двух указателей
        nums1.sort()
        nums2.sort()

        result = []
        i, j = 0, 0  # два указателя

        # Проходим по обоим массивам одновременно
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                # Элемент в nums1 меньше — сдвигаем указатель i
                i += 1
            elif nums1[i] > nums2[j]:
                # Элемент в nums2 меньше — сдвигаем указатель j
                j += 1
            else:
                # Нашли общий элемент — добавляем в результат
                result.append(nums1[i])
                i += 1
                j += 1

        return result
