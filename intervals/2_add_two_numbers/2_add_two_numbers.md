Medium

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Example 1:**

![](./2_add_two_numbers_images/6d807a9b7486c05db0d3ae91d4dec327_MD5.jpg)

**Input:** l1 = [2,4,3], l2 = [5,6,4]
**Output:** [7,0,8]
**Explanation:** 342 + 465 = 807.

**Example 2:**

**Input:** l1 = [0], l2 = [0]
**Output:** [0]

**Example 3:**

**Input:** l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
**Output:** [8,9,9,9,0,0,0,1]

**Constraints:**

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

___
Единственное отличие, что в АВИТО числа это не перевернутые и в массивах хранятся: (**Первая задача**)

- input: arr1 = [1, 2, 3], arr2 = [4, 5, 6]

- output: [0, 5, 7, 9] (один ведущий 0 в ответе допускается)

- Note: 123 + 456 = 579