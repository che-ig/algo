Floyd’s Cycle detection algorithm or Hair Tortoise algorithm is used to detect if there is a cycle in a linked list. This algorithm is quite confusing if not analyzed mathematically.

If you are aware of the algorithm and want to check only the **WHY,** jump to the [proof section](https://medium.com/p/59f61984dc3e#67a7).

## What is a Linked List Cycle?

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*f_-HHcKU9RFPim2OLGwyKA.jpeg)

LinkedList cycle

A linked list is said to have a cycle if the end of the linked list points to another node of the list.

### Code

## What is Floyd’s Cycle detection algorithm?

Floyd’s Cycle detection algorithm is used to detect whether the linked list has a cycle in it and what is the starting point(green node in the above diagram) of the cycle.

### Algorithm to find whether there is a cycle or not :

1. Declare 2 nodes say `**slowPointer**` and `**fastPointer**` pointing to the linked list head.
2. Move `**slowPointer**` by one node and `**fastPointer**` by 2 nodes till either of one reaches nil.
3. If at any point in the above traversal, `**slowPointer**` and `**fastPointer**` are found to be pointing to the same node, which implies the list has a cycle

### Algorithm to find the starting node of the cycle:

After figuring out whether there is a cycle or not perform the following steps

1. Reset the `**slowPointer**` to point to the head of the linked list and keep the `**fastPointer**` at the intersected position.
2. Move both the `**fastPointer**` and `**slowPointer**` pointers by one node.
3. The point at which they will intersect is the starting of the cycle.

## Why does Floyd’s Cycle Algorithm works?

But can we prove whether the algorithm will even work?

![](https://miro.medium.com/v2/resize:fit:998/1*Kn3tKdKp1bPetLR9VqGMJQ.gif)

Well then let’s prove it.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*NCUKC3ZELzZze5VjM4_ZgA.jpeg)

Let us assume that the Linked list has a cycle that starts at the green node. As per the algorithm, we have 2 traversal pointers `**slowPointer**` and `**fastPointer**` that move 1 node and 2 nodes respectively before they meet each other at the pink node. From there the `**slowPointer**` node is reset to point to the head and both of `**fastPointer**` and `**slowPointer**` are then moved by one node. The next point they meet will be the start of the cycle i.e the green node.

Let,**  
x** = Distance between the start of the Linked List and the start of the cycle.**y** = Distance between the start of the cycle to the point where **slowPointer** and **fastPointer** first meet each other.**l** = Total distance of the cycle.Distance travelled by **slowPointer** on meeting **fastPointer** is

When they first meet each other i.e at the pink node,

## Get G. Abhisek’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

`**slowPointer**` has covered a distance of `**x + s*l + y**` , where `**s**` is a non-negative integer.

`**fastPointer**` has covered a distance of `**x + f*l + y**` , where `**f**` is a non-negative integer.

Since `**fastPointer**` travels twice the speed of `**slowPointer**` , it would travel twice the distance in the same time as that of `**slowPointer**`. This we have calculated from simple [time, speed, and distance relation.](https://www.geeksforgeeks.org/calculate-speed-distance-time/)

So,  
**x + f*l + y = 2(x + s*l + y)**Solving this, we get  
**x + y = f*l - 2s*l  
**We can say, **f*l - 2s*l = (some integer) * l = k*l**So, **x + y = kl**, where **k** is an integer  
=> **x = kl - y**

Now, if we move `**slowPointer**` the start of the linked list will cover `**x**`distance to meet `**fastPointer**`, when `**fastPointer**` will cover `**kl-y**`distance (because `**fastPointer**` already has covered `**y**`distance).

Since, `**kl — y = x**` **,** both `**fastPointer**` and `**slowPointer**` will cover `**x**` i.e same distance after the pink node at some point to meet at the start point of the cycle. When we say at some point, i.e `**fastPointer**` can complete some `**kl**` distance out of which it has already covered `**y**` distance.

The concepts of Floyd’s Cycle detection algorithm can also be applied to many other linked list problems. So it is pretty necessary to understand the working of these.