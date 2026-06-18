Medium

You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where `answer[i]` is the value of the next greater node of the `ith` node (**1-indexed**). If the `ith` node does not have a next greater node, set `answer[i] = 0`.

**Example 1:**

![](./1019_next_greater_node_in_linked_list_images/4772e1e45789352c46d7f8572d571c7e_MD5.jpg)

**Input:** head = [2,1,5]
**Output:** [5,5,0]

**Example 2:**

![](./1019_next_greater_node_in_linked_list_images/5b19adbb230aeab4bc56ace53296b885_MD5.jpg)

**Input:** head = [2,7,4,3,5]
**Output:** [7,0,5,5,0]

**Constraints:**

- The number of nodes in the list is `n`.
- `1 <= n <= 10^4`
- `1 <= Node.val <= 10^9`
