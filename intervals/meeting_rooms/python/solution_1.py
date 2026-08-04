class Solution:
    # @param A : list of list of integers
    # @return an integer

    # time: O(n * log n)
    # mem (дополнительной): O(n)
    def solve(self, A):
        points = []
        for elem in A:
            points.append([elem[0], +1])  # точка, +1 - что нужна еще одна комната
            points.append([elem[1], -1])  # точка, -1 - что комната осободилась

        points.sort()  # [10, -1] будет перед [10, +1] - сначала комнаты особождают а потом занимают
        max_room_numbers = 0
        curr_room_numbers = 0
        # для каждого момента времени находим используемое число комнат и выбираем максимальное значение
        for point in points:
            curr_room_numbers += point[1]
            max_room_numbers = max(max_room_numbers, curr_room_numbers)
        return max_room_numbers
