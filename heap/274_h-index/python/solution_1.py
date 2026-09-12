class Solution:
    def hIndex(self, citations):
        n = len(citations)

        # buckets[i] — количество статей с ровно i цитированиями
        # Для статей с citations[i] >= n кладём в buckets[n]
        buckets = [0] * (n + 1)

        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        # Идём справа налево, накапливая количество статей с >= i цитированиями
        # papers_with_at_least_i — количество статей с >= i цитированиями
        papers_with_at_least_i = 0

        for i in range(n, -1, -1):
            papers_with_at_least_i += buckets[i]

            # Если статей с >= i цитированиями хотя бы i штук — нашли h-index
            if papers_with_at_least_i >= i:
                return i

        return 0
