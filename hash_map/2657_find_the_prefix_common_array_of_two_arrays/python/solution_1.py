class Solution:
    # time: O(n)
    # mem: O(n)
    def findThePrefixCommonArray(self, a: list[int], b: list[int]) -> list[int]:

        result = []
        setA = set()
        setB = set()
        currentIntersectionCnt = 0

        for i in range(len(a)):
            if b[i] in setA:
                currentIntersectionCnt += 1

            if a[i] in setB:
                currentIntersectionCnt += 1

            if a[i] == b[i]:
                currentIntersectionCnt += 1

            setA.add(a[i])
            setB.add(b[i])

            result.append(currentIntersectionCnt)
        return result
