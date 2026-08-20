Medium

You are given an integer array `ribbons`, where `ribbons[i]` represents the length of the `iᵗʰ` ribbon, and an integer `k`. You may cut any of the ribbons into any number of segments of positive integer lengths, or keep them intact.

Your task is to determine the maximum length of ribbon, `x`, that allows you to cut at least `k` ribbons, each of length `x`. You can discard any leftover ribbon.

If it is impossible to cut `k` ribbons of the same length, return `0`.

---

**Example 1:**

```
Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.
```

**Example 2:**

```
Input: ribbons = [7,5,9], k = 4
Output: 4
Explanation:
- Cut the first ribbon to two ribbons, one of length 4 and one of length 3.
- Cut the second ribbon to two ribbons, one of length 4 and one of length 1.
- Cut the third ribbon to two ribbons, one of length 4 and one of length 5.
Now you have 4 ribbons of length 4.
```

**Example 3:**

```
Input: ribbons = [5,7,9], k = 22
Output: 0
Explanation: You cannot obtain k ribbons of the same positive integer length.
```

---

**Constraints:**

- `1 <= ribbons.length <= 10^5`
- `1 <= ribbons[i] <= 10^5`
- `1 <= k <= 10^9`