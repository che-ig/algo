Easy

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Example 1:**

![](./700_search_in_a_binary_search_tree_images/a91017386e3c1158fd2e4169959880d7_MD5.jpg)

**Input:** root = [4,2,7,1,3], val = 2
**Output:** [2,1,3]

**Example 2:**

![](./700_search_in_a_binary_search_tree_images/b2acaa3f792ce75b2faac0c9500bdbea_MD5.jpg)

**Input:** root = [4,2,7,1,3], val = 5
**Output:** []

**Constraints:**

- The number of nodes in the tree is in the range `[1, 5000]`.
- `1 <= Node.val <= 10^7`
- `root` is a binary search tree.
- `1 <= val <= 10^7`
