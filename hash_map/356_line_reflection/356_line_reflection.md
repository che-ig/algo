
Medium

Given `n` points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

**Note** that there can be repeated points.

**Example 1:**
![](./356_line_reflection_images/1.png)
Input: points = [\[1,2],[-1,2]\]
Output: true
Explanation: We can choose the line x = 0.

**Example 2:**
![](./356_line_reflection_images/2.png)
Input: points = [\[2,1],[-1,2]\]
Output: false
Explanation: We can't choose a line.

**Constraints:**

- `n == points.length`
- `1 <= n <= 10⁴`
- `-10⁸ <= points[i][j] <= 10⁸`
    

**Follow up:** Could you do better than `O(n²)`?[](https://raw.githubusercontent.com/MGMCN/leetcode/c0174c5adcc19e8699943792dbbf959f4919c132/solution/0300-0399/0356.Line%20Reflection/README_EN.md#1)