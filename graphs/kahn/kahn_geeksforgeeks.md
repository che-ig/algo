# Topological Sorting using BFS - Kahn's Algorithm

[source](https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/)

Given a Directed Acyclic Graph having V vertices and E edges, find any Topological Sorted ordering of the graph.

Topological Order is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.

**Example:**

**Input:** `adj[][] = [[1], [2], [], [2, 4], []]`
**Output:** `[0, 3, 1, 4, 2]`
**Explanation:** For every pair of vertex(u -> v) in the ordering, u comes before v.

![](./kahn_geeksforgeeks_images/1ff49b6c871dc6497ca471dece4921f3_MD5.webp)

**Input:** `adj[][]= [[1], [2], [3], [], [5], [1, 2]]`
**Output:** `[0, 4, 5, 1, 2, 3]`
**Explanation:** For every pair of vertex(u -> v) in the ordering, u comes before v.

![](./kahn_geeksforgeeks_images/74551164bb189d42b01f5a164e19c9ea_MD5.webp)

Try It Yourself

The Kahn’s Algorithm uses BFS and has the following steps.

- Compute in-degree of every vertex — representing how many incoming edges each vertex has.
- Add all vertices with an in-degree of 0 a queue, as they can appear first in the topological ordering.
- Repeatedly remove a vertex from the queue, add it to result, and reduce in-degree of all its adjacent. If any of those vertices now have an in-degree of 0, add them also to the queue.
- This process continues until the queue is empty

**Illustration of the algorithm:**

![](./kahn_geeksforgeeks_images/fccb05f4b3d310286e3d80d47f25c4b5_MD5.webp)

![](./kahn_geeksforgeeks_images/55a0a3061b3a54d1663970b705ac0cc0_MD5.webp)

![](./kahn_geeksforgeeks_images/e81b43e3a5a0ab3816f0b6cfcf4b3a4c_MD5.webp)

![](./kahn_geeksforgeeks_images/1798c1f86994b72cd885f02239c9cab6_MD5.webp)

![](./kahn_geeksforgeeks_images/6be8fef428a753fcf12757252d45d787_MD5.webp)

![](./kahn_geeksforgeeks_images/42992b5b2c9c276e3ba6a5b3aec2ed7d_MD5.webp)

![](./kahn_geeksforgeeks_images/117a8a3f2d56dcc300fdfb080dbfe661_MD5.webp)

![](./kahn_geeksforgeeks_images/f8dbddbe16f348f06cc56084cd9d4998_MD5.webp)

![](./kahn_geeksforgeeks_images/de2585c16dbf7177c50cd8ce44675a73_MD5.webp)

![](./kahn_geeksforgeeks_images/d0ace7ff3650e1eff3d8ee995c19c917_MD5.webp)

![](./kahn_geeksforgeeks_images/f1c8007824f56bb1b7acd989f7ec62d8_MD5.webp)

![](./kahn_geeksforgeeks_images/c366060d2cc5dc001005856e650f9351_MD5.webp)

![](./kahn_geeksforgeeks_images/13104dd3a0a55b0b24d84eaa6147a867_MD5.webp)

![](./kahn_geeksforgeeks_images/26bc3bf7c6c702fd549e16f2ece86206_MD5.webp)

Below is the implementation of the above algorithm.

### Python

```python
#Driver Code Starts
from collections import deque
#Driver Code Ends

def topoSort(adj):
    n = len(adj)
    indegree = [0] * n
    res = []
    queue = deque()

    # Compute indegrees
    for i in range(n):
        for next_node in adj[i]:
            indegree[next_node] += 1

    # Add all nodes with indegree 0
    # into the queue
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # Kahn’s Algorithm
    while queue:
        top = queue.popleft()
        res.append(top)
        for next_node in adj[top]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
    return res

def addEdge(adj, u, v):
    adj[u].append(v)

#Driver Code Starts
# Example
n = 6
adj = [[] for _ in range(n)]
addEdge(adj, 0, 1)
addEdge(adj, 1, 2)
addEdge(adj, 2, 3)
addEdge(adj, 4, 5)
addEdge(adj, 5, 1)
addEdge(adj, 5, 2)
res = topoSort(adj)
print(*res)
#Driver Code Ends
```



**Output:**
`0 4 5 1 2 3`

**Time Complexity:** O(V+E). For Performing BFS.
**Auxiliary Space:** O(V).

