[Источник](https://www.geeksforgeeks.org/dsa/tree-traversals-inorder-preorder-and-postorder/)

---

# Tree Traversal Techniques

**Last Updated: 6 Dec, 2025**

Tree traversal refers to the process of visiting or accessing each node of a tree exactly once in a specific order. Unlike linear data structures such as arrays, linked lists, or queues (which have only one logical way of traversal), trees offer multiple ways to traverse their nodes. Tree traversals are broadly classified into two categories:

- **Depth-First Traversal (DFT)** – Explores as far as possible along a branch before exploring the next branch.
  - Types: Inorder, Preorder, Postorder
- **Breadth-First Traversal (BFT)** – Explores nodes level by level from top to bottom.
  - Type: Level Order Traversal.

> The level order traversal of the above tree is **1, 2, 3, 4, 5, 6, and 7**.

**General Tree Traversal Overview**

![](./tree_traversal_techniques_images/fa381413c10d43f69f3985bef5b79947_MD5.webp)

**Tree Construction from Inorder and Preorder Traversals**

![](./tree_traversal_techniques_images/4f8a98151cd77ba1aeb4a3dfcd4745e7_MD5.webp)

---

## Inorder Traversal

Inorder traversal visits the node in the order: **Left → Root → Right**

### Algorithm for Inorder Traversal

```
Inorder(tree)
1. Traverse the left subtree, i.e., call Inorder(left->subtree)
2. Visit the root.
3. Traverse the right subtree, i.e., call Inorder(right->subtree)
```

**Inorder Traversal – Slide 1 (Step 1)**

![](./tree_traversal_techniques_images/290cc2362bce0fb35efd7e91e2038f25_MD5.webp)

**Inorder Traversal – Slide 2 (Step 8)**

![](./tree_traversal_techniques_images/a39845138831f7764b9d493d93fc7152_MD5.webp)

**Inorder Traversal – Slide 3 (Step 3)**

![](./tree_traversal_techniques_images/a2ae415f55b9daa7ad0cd7d64364d898_MD5.webp)

**Inorder Traversal – Slide 4 (Step 10)**

![](./tree_traversal_techniques_images/9fe5dadb063b8618b824a2d0f7a88f6e_MD5.webp)

**Inorder Traversal – Slide 5 (Step 5)**

![](./tree_traversal_techniques_images/c9235dde289f69c91580fe14efad6a19_MD5.webp)

**Inorder Traversal – Slide 6 (Step 6)**

![](./tree_traversal_techniques_images/c815224f150620fbc5269f70629dcd45_MD5.webp)

### Uses of Inorder Traversal

- In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
- To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal is reversed can be used.
- Inorder traversal can be used to evaluate arithmetic expressions stored in expression trees.

> **Also Check:** [Inorder Traversal of Binary Tree](https://www.geeksforgeeks.org/dsa/inorder-traversal-of-binary-tree/) for more.

---

## Preorder Traversal

Preorder traversal visits the node in the order: **Root → Left → Right**

### Algorithm for Preorder Traversal

```
Preorder(tree)
1. Visit the root.
2. Traverse the left subtree, i.e., call Preorder(left->subtree)
3. Traverse the right subtree, i.e., call Preorder(right->subtree)
```

**Preorder Traversal – Slide 1 (Step 1)**

![](./tree_traversal_techniques_images/08a3ff45474250a12600575a6ca3d533_MD5.webp)

**Preorder Traversal – Slide 2 (Step 2)**

![](./tree_traversal_techniques_images/9f3b3a38ad353b511bec90e759561d18_MD5.webp)

**Preorder Traversal – Slide 3 (Step 3)**

![](./tree_traversal_techniques_images/32948ece56724d977676000afdea7f44_MD5.webp)

**Preorder Traversal – Slide 4 (Step 4)**

![](./tree_traversal_techniques_images/66f81f48f8566d527230f2a333e8303a_MD5.webp)

**Preorder Traversal – Slide 5 (Step 5)**

![](./tree_traversal_techniques_images/b947b0702668629ba1c80236c00ad126_MD5.webp)

**Preorder Traversal – Slide 6 (Step 6)**

![](./tree_traversal_techniques_images/84519c574a65ff0000dd6a80d59cd0ae_MD5.webp)

### Uses of Preorder Traversal

- Preorder traversal is used to create a copy of the tree.
- Preorder traversal is also used to get prefix expressions on an expression tree.

> **Also Check:** [Preorder Traversal of Binary Tree](https://www.geeksforgeeks.org/dsa/preorder-traversal-of-binary-tree/) for more.

---

## Postorder Traversal

Postorder traversal visits the node in the order: **Left → Right → Root**

### Algorithm for Postorder Traversal

```
Postorder(tree)
1. Traverse the left subtree, i.e., call Postorder(left->subtree)
2. Traverse the right subtree, i.e., call Postorder(right->subtree)
3. Visit the root.
```

**Postorder Traversal – Slide 1 (Step 1)**

![](./tree_traversal_techniques_images/b26f8650d103525ad976f32fccd2f5ca_MD5.webp)

**Postorder Traversal – Slide 2 (Step 2)**

![](./tree_traversal_techniques_images/98670dde5ddfaae43777b46c3108c609_MD5.webp)

**Postorder Traversal – Slide 3 (Step 3)**

![](./tree_traversal_techniques_images/8224b6ec54e14ee20401c03854c89ad0_MD5.webp)

**Postorder Traversal – Slide 4 (Step 4)**

![](./tree_traversal_techniques_images/ff92d43d8d139725896f6153dac220ac_MD5.webp)

**Postorder Traversal – Slide 5 (Step 5)**

![](./tree_traversal_techniques_images/1065559b920c865c8a1b6c326473227a_MD5.webp)

**Postorder Traversal – Slide 6 (Step 6)**

![](./tree_traversal_techniques_images/52dd436308994b47e920bac1f60388d7_MD5.webp)

### Uses of Postorder Traversal

- Postorder traversal is used to delete the tree.
- Postorder traversal is also useful to get the postfix expression of an expression tree.
- Postorder traversal can help in garbage collection algorithms, particularly in systems where manual memory management is used.

> **Also Check:** [Postorder Traversal of Binary Tree](https://www.geeksforgeeks.org/dsa/postorder-traversal-of-binary-tree/) for more.

---

## Level Order Traversal

Level Order Traversal visits all nodes present in the same level completely before visiting the next level.

### Algorithm for Level Order Traversal

```
LevelOrder(tree)
1. Create an empty queue Q
2. Enqueue the root node of the tree to Q
3. Loop while Q is not empty:
   a. Dequeue a node from Q and visit it
   b. Enqueue the left child of the dequeued node if it exists
   c. Enqueue the right child of the dequeued node if it exists
```

**Level Order Traversal – Slide 1 (Step 1)**

![](./tree_traversal_techniques_images/7d8980d95301500ff62934d4370c5eba_MD5.webp)

**Level Order Traversal – Slide 2 (Step 2)**

![](./tree_traversal_techniques_images/ccbaae65aa73909cc4d97b518c4fcbf2_MD5.webp)

**Level Order Traversal – Slide 3 (Step 3)**

![](./tree_traversal_techniques_images/725bd57d8dd67daeee92a5438266008a_MD5.webp)

**Level Order Traversal – Slide 4 (Step 4)**

![](./tree_traversal_techniques_images/7549361c12ba6dfe9cbaac5e64b7331f_MD5.webp)

**Level Order Traversal – Slide 5 (Step 5)**

![](./tree_traversal_techniques_images/36053a6c24d8b5595ced2e9850cefd10_MD5.webp)

**Level Order Traversal – Slide 6 (Step 6)**

![](./tree_traversal_techniques_images/2bb98fd47ccbce127f21003440244d42_MD5.webp)

**Level Order Traversal – Slide 7 (Step 7)**

![](./tree_traversal_techniques_images/cb8103a2a167475dd4bba4c9cc80ca6e_MD5.webp)

**Level Order Traversal – Slide 8 (Step 8)**

![](./tree_traversal_techniques_images/3b6f124cae50cc30dd20f5a2f693d1c6_MD5.webp)

### Uses of Level Order Traversal

- Level-wise node processing, like finding maximum/minimum at each level.
- Tree serialization/deserialization for efficient storage and reconstruction.
- Solving problems like calculating the "maximum width of a tree" by processing nodes level by level.

---

## Other Tree Traversals

- **Boundary Traversal**
- **Diagonal Traversal**

### 1. Boundary Traversal

Boundary Traversal of a Tree includes:

- left boundary (nodes on left excluding leaf nodes)
- leaves (consist of only the leaf nodes)
- right boundary (nodes on right excluding leaf nodes)

**Boundary Traversal**

![](./tree_traversal_techniques_images/af2a208cd1a1ca9bdaf4bc2698c8d9a4_MD5.png)

> **Also Check:** [Boundary Traversal of binary tree](https://www.geeksforgeeks.org/dsa/boundary-traversal-of-binary-tree/) for more.

### 2. Diagonal Traversal

In the Diagonal Traversal of a Tree, all the nodes in a single diagonal will be printed one by one.

**Diagonal Traversal**

![](./tree_traversal_techniques_images/ad14b006643b918317dfd4ed4758f5fb_MD5.webp)

> **Also Check:** [Diagonal Traversal of Binary Tree](https://www.geeksforgeeks.org/dsa/diagonal-traversal-of-binary-tree/) for more.

---

## Related Articles

- [Tree Traversal](https://www.geeksforgeeks.org/dsa/tree-traversals-inorder-preorder-and-postorder/)
- [Inorder Traversal of Binary Tree](https://www.geeksforgeeks.org/dsa/inorder-traversal-of-binary-tree/)
- [Preorder Traversal in Python](https://www.geeksforgeeks.org/dsa/preorder-traversal-of-binary-tree/)
- [Postorder Traversal in Python](https://www.geeksforgeeks.org/dsa/postorder-traversal-of-binary-tree/)

---
