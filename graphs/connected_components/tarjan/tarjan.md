## 1. Introduction[](https://www.baeldung.com/cs/scc-tarjans-algorithm#introduction)

In this topic, we’ll discuss Tarjan’s algorithm for finding strongly connected components (SCCs) in directed graphs. Furthermore, we can check out [Kosaraju’s algorithm](https://www.baeldung.com/cs/kosaraju-algorithm-scc) for the definition of SCCs to start.

## 2. An Example Graph[](https://www.baeldung.com/cs/scc-tarjans-algorithm#an-example-graph)

Let’s pick an example graph, ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg), for our discussion:

![](./tarjan_images/02668af6575644ef95e1d7e82b45216f_MD5.webp)

![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg) is a directed graph with four SCCs. We’ve depicted the SCCs with different colors for visual comprehension:

![](./tarjan_images/e5cb6b85331c50fd09da02bb86e17029_MD5.webp)

Further, we’ll use this graph to demonstrate the ideas of Tarjan’s algorithm.

## 3. The Spanning Forest of DFS[](https://www.baeldung.com/cs/scc-tarjans-algorithm#the-spanning-forest-of-dfs)

**Before digging into the algorithm itself, we need to introduce the notion of the DFS spanning forest**. Hence, when DFS traverses a directed graph, it defines a set of non-intersecting trees. We’ll call this set the spanning forest of DFS.

**Additionally, we’ll also classify the edges of the graph depending on how DFS discovers them**. If DFS processes vertex ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg) it discovers:

- An unvisited neighbour, ![](./tarjan_images/ada68d710aa57708f8d822c6887ce660_MD5.svg), then edge (![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg), ![](./tarjan_images/ada68d710aa57708f8d822c6887ce660_MD5.svg)) is a tree edge.
- A visited but not yet fully processed neighbor, ![](./tarjan_images/3c5857e4d5aef6c99dc81e8e85ff6a07_MD5.svg), then edge (![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg), ![](./tarjan_images/3c5857e4d5aef6c99dc81e8e85ff6a07_MD5.svg)) is a back edge.
- A fully processed neighbour, ![](./tarjan_images/8c889f933bccb4d2a0c065a6e63f8928_MD5.svg), then edge (![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg), ![](./tarjan_images/8c889f933bccb4d2a0c065a6e63f8928_MD5.svg)) is a cross edge.

Let’s classify the edges of the sample graph. First, we run DFS for vertex ![](./tarjan_images/3ca8877da55b00ac3c8673fe4f26fb6a_MD5.svg). DFS visits vertices ![](./tarjan_images/3ca8877da55b00ac3c8673fe4f26fb6a_MD5.svg), ![](./tarjan_images/abf9c44dff2dc42816767fcaccf4fcbc_MD5.svg), ![](./tarjan_images/913bf9b60256fe7b549d285cc5ac5e9d_MD5.svg), ![](./tarjan_images/b63bbd89009e4cb53682be7af9c13e0e_MD5.svg), ![](./tarjan_images/61377fa17e75430862921da24fb801c6_MD5.svg), ![](./tarjan_images/4ec3090d3f95536f8280eebeef49c375_MD5.svg) and exits. Then, let’s run DFS for ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg). Now, DFS visits the remaining vertices: ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg), ![](./tarjan_images/caba3e744402dce21f65f536bc0cd72e_MD5.svg), ![](./tarjan_images/dbc81dc70ede9cd8a7cbde978ab3e0dc_MD5.svg), and ![](./tarjan_images/c49fdf19e3dfe2ada7c697edf02adc1b_MD5.svg). Moreover, The tree edges are depicted with solid lines, the back edges with dashed lines, and the cross edges with dotted lines:

![](./tarjan_images/85318ef3bfc89c040bcb8821fe4daf7c_MD5.webp)

The spanning forest of the graph consists of two trees:

- The first tree consists of the set of vertices ![](./tarjan_images/df99e2000b338c1d3f652ce346d686c0_MD5.svg) and the set of edges ![](./tarjan_images/b5b5efe8e71e8d89aa964ad5507fd556_MD5.svg).
- The second tree consists of the set of vertices ![](./tarjan_images/7f504152a82dc057502e47768b6ddea9_MD5.svg) and the set of edges ![](./tarjan_images/e331a93061a538d48aeb9dfb281893b3_MD5.svg).

Note that depending on which vertex we start DFS for, the classification of edges may change. For example, some back edges may become tree edges and vice versa, and some cross edges may become tree edges. Thus, the tree set in the spanning forest may also change. Fortunately, that doesn’t affect Tarjan’s algorithm in any way.

## 4. Tarjan’s Algorithm[](https://www.baeldung.com/cs/scc-tarjans-algorithm#tarjans-algorithm)

### 4.1. Observations[](https://www.baeldung.com/cs/scc-tarjans-algorithm#1-observations)

**Tarjan’s algorithm uses the observation that SCCs can be built out of the trees in the spanning forest**. **Furthermore, a single tree in the spanning forest may contain several SCCs, but no SCC can belong to more than one tree**. If an SCC belonged to more than one tree, then those trees would have been reachable from each other during DFS traversal, thus forming a single tree.

If each SCC exactly matched a tree in the spanning forest, the problem of finding SCCs would have been solved by running a simple DFS and identifying trees in the spanning forest. However, this approach only works for finding connected components in undirected graphs. In the case of directed graphs, a tree in the spanning forest may contain multiple SCCs.

Let’s pay attention to another observation that is used by the algorithm. In particular, any SCC can be treated as a directed cycle because any two vertices in an SCC are reachable from each other. Hence, **if we start DFS for any of the SCC vertices, there will be a moment when DFS sees a back edge to that vertex**. A back edge identifies a cycle. Thus, when we see a back edge during DFS, we conclude that either we’ve found an SCC or a small cycle inside of a bigger cycle.

### 4.2. Algorithm Description[](https://www.baeldung.com/cs/scc-tarjans-algorithm#2-algorithm-description)

**Tarjan’s algorithm defines arrays ![\boldsymbol{num[]}](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-d23d39ecb7524c58f27a2422fea19e13_l3.svg "Rendered by QuickLaTeX.com") and ![\boldsymbol{lowest[]}](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-58d9cceb2ee246ca3cd249ed2e254c70_l3.svg "Rendered by QuickLaTeX.com"), which help in classifying edges**. Furthermore, they help identify the starting vertex of an SCC. Additionally, the algorithm also uses a stack to keep the current DFS tree’s vertices and correctly fetches the vertices of SCCs afterward.

The steps of the algorithm are described below:

1. Select an unvisited vertex, ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg). Furthermore, if there’re no unvisited vertices, the algorithm terminates
2. Run DFS for ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)
3. Go to step 1

Inside DFS:

1. ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg) is marked as visited
2. ![num[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-253e03b478f4321a6920892fa00bbca1_l3.svg "Rendered by QuickLaTeX.com") is initialized to be the current value of the counter
3. ![lowest[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-4af99e104140a5ca2484b571a5ab5bbd_l3.svg "Rendered by QuickLaTeX.com") is initially equal to ![num[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-253e03b478f4321a6920892fa00bbca1_l3.svg "Rendered by QuickLaTeX.com")
4. Next, we go over the ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg) neighbors. If we see an unvisited neighbor, ![](./tarjan_images/ada68d710aa57708f8d822c6887ce660_MD5.svg), we invoke DFS for it and, upon returning, update ![lowest[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-4af99e104140a5ca2484b571a5ab5bbd_l3.svg "Rendered by QuickLaTeX.com") with ![lowest[u]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-fb669cee89bc80ce0852d02347d4ab61_l3.svg "Rendered by QuickLaTeX.com") if ![lowest[v] > lowest[u]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-521c941ad4e767dde7a5c4de10c821b4_l3.svg "Rendered by QuickLaTeX.com")
5. If we see a visited but not processed neighbor, ![](./tarjan_images/3c5857e4d5aef6c99dc81e8e85ff6a07_MD5.svg), we have a back edge. In this case, we update ![lowest[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-4af99e104140a5ca2484b571a5ab5bbd_l3.svg "Rendered by QuickLaTeX.com") with ![num[w]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-ae4cc4ea32244b3380121c4c296d7acf_l3.svg "Rendered by QuickLaTeX.com") if ![lowest[v] > num[w]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-ee092669e2f231423ee6cfa90dd268b3_l3.svg "Rendered by QuickLaTeX.com")
6. After we process ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)‘s neighbours, we mark ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg) as processed
7. After ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg) is processed, we check if ![num[v] = lowest[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-b1648f60fa24264da0f2a9ff8045acf4_l3.svg "Rendered by QuickLaTeX.com"). Thus, if that’s the case, ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg) is the starting vertex of its component. Furthermore, we unwind the stack until we retrieve ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg). The unwound vertices belong to the  ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)‘s SCC

### 4.3. Running the Algorithm for the Example Graph[](https://www.baeldung.com/cs/scc-tarjans-algorithm#3-running-the-algorithm-for-the-example-graph)

In our example, the white vertices are unvisited. The light grey nodes have been visited but have not yet been processed. Further, the dark grey vertices are fully processed. Moreover, the processed edges are colored red. Finally, we depict the vertex stack in the lower right corner.

First, we start by running DFS for ![](./tarjan_images/3ca8877da55b00ac3c8673fe4f26fb6a_MD5.svg). The image below shows the state after DFS has visited ![](./tarjan_images/3ca8877da55b00ac3c8673fe4f26fb6a_MD5.svg), ![](./tarjan_images/abf9c44dff2dc42816767fcaccf4fcbc_MD5.svg), and ![](./tarjan_images/913bf9b60256fe7b549d285cc5ac5e9d_MD5.svg), but hasn’t yet processed back edge ![](./tarjan_images/0c16230b7bdfbf89f6477035899ec0ec_MD5.svg):

![](./tarjan_images/6205aa095e840759bde11e83f6b5c5f5_MD5.webp)

Furthermore, the image below shows the state when DFS has processed back edge ![](./tarjan_images/0c16230b7bdfbf89f6477035899ec0ec_MD5.svg), updated ![lowest[C]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-7f2597cece5f29adbd2f29a5dc8b4454_l3.svg "Rendered by QuickLaTeX.com"), backtracked, and updated ![lowest[B]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-51aca36e6959e79d0e1416fa404df742_l3.svg "Rendered by QuickLaTeX.com"). Next, DFS visited the remaining vertices reachable from ![](./tarjan_images/abf9c44dff2dc42816767fcaccf4fcbc_MD5.svg):

![](./tarjan_images/f57296584ff2e65e08861dd3fab1aeb0_MD5.png)

Then, DFS backtracks from ![](./tarjan_images/4ec3090d3f95536f8280eebeef49c375_MD5.svg), and in ![](./tarjan_images/61377fa17e75430862921da24fb801c6_MD5.svg) DFS finds the first SCC = ![](./tarjan_images/fa4d77f16f283d3c99e09ab684f24f19_MD5.svg):

![](./tarjan_images/5cc7a3e4f05ebb86b92dd45c15581bae_MD5.png)

Next, DFS backtracks to ![](./tarjan_images/b63bbd89009e4cb53682be7af9c13e0e_MD5.svg), and the second SCC = ![](./tarjan_images/083a8de35df6386bba1ff29a34fc693e_MD5.svg) is found:

![](./tarjan_images/481e5065a2f731f8f25a7bccd428bf25_MD5.png)

Now, DFS backtracks to ![](./tarjan_images/abf9c44dff2dc42816767fcaccf4fcbc_MD5.svg), then to ![](./tarjan_images/3ca8877da55b00ac3c8673fe4f26fb6a_MD5.svg), and in ![](./tarjan_images/3ca8877da55b00ac3c8673fe4f26fb6a_MD5.svg) DFS finds the third SCC = ![](./tarjan_images/e588adaaaea71ba7a69b0392b9dac3a3_MD5.svg):

![](./tarjan_images/c6b23f95b68141d03f5adafa9fe900bd_MD5.png)

The DFS invocation terminates at this point as no reachable vertices are left. Next, we run DFS for an unvisited vertex, ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg). DFS visits ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg), ![](./tarjan_images/caba3e744402dce21f65f536bc0cd72e_MD5.svg), ![](./tarjan_images/dbc81dc70ede9cd8a7cbde978ab3e0dc_MD5.svg), and ![](./tarjan_images/c49fdf19e3dfe2ada7c697edf02adc1b_MD5.svg), processes back edge (![](./tarjan_images/c49fdf19e3dfe2ada7c697edf02adc1b_MD5.svg), ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg)), and updates ![lowest[J]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-c5f3abb053afdb530b5e699992dc23b9_l3.svg "Rendered by QuickLaTeX.com"):

![](./tarjan_images/722d24ffb359df04a4686266a6afcac7_MD5.png)

Then, DFS backtracks to ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg) and updates all the vertices on the way:

![](./tarjan_images/c8518d79e0c29deec48d5cefaaf09f2e_MD5.png)

Finally, when processing ![](./tarjan_images/ae194d0d6e4981f9664d7bab752d4abe_MD5.svg), DFS finds the last SCC = ![](./tarjan_images/7f504152a82dc057502e47768b6ddea9_MD5.svg).

## 5. The Pseudocode of the Algorithm[](https://www.baeldung.com/cs/scc-tarjans-algorithm#the-pseudocode-of-the-algorithm)

In this section, we’ll implement Tarjan’s algorithm. We’re using a number of variables needed by the algorithm. Note that we could have added all those variables as parameters to the DFS procedure. But let’s keep the DFS implementation simple and have all the auxiliary variables as global data. Here’re all the additional variables used by the algorithm:

- ![](./tarjan_images/82249b0debc5888cc6df07502a791086_MD5.svg) – a counter used to assign sequential numbers to the vertices
- ![\boldsymbol{num[]}](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-d23d39ecb7524c58f27a2422fea19e13_l3.svg "Rendered by QuickLaTeX.com") – an array of integers holding the vertice numbers, ![num[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-253e03b478f4321a6920892fa00bbca1_l3.svg "Rendered by QuickLaTeX.com") is the number assigned to ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)
- ![\boldsymbol{lowest[]}](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-58d9cceb2ee246ca3cd249ed2e254c70_l3.svg "Rendered by QuickLaTeX.com") – an array of integers holding the minimum reachable vertex numbers, ![lowest[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-4af99e104140a5ca2484b571a5ab5bbd_l3.svg "Rendered by QuickLaTeX.com") is the minimum number of a vertex reachable from ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)
- ![\boldsymbol{visited[]}](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-b9def21f043f6cf796cbb0b2312dad87_l3.svg "Rendered by QuickLaTeX.com") – an array of booleans indicating which vertices have been visited by DFS so far. If ![visited[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-a0ec2089fd853334602f7201fa3c7715_l3.svg "Rendered by QuickLaTeX.com") is TRUE, then DFS has already seen ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg), but it hasn’t necessarily finished processing ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)
- ![\boldsymbol{processed[]}](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-38a3df76c5682c688c12d351f0da64c2_l3.svg "Rendered by QuickLaTeX.com") – an array of booleans indicating which vertices have been already processed by DFS. If ![processed[v]](https://www.baeldung.com/wp-content/ql-cache/quicklatex.com-b6e1216398f72d5e21b633ff0e6efdfb_l3.svg "Rendered by QuickLaTeX.com") is TRUE, then DFS has already finished with ![](./tarjan_images/68270fb6e5130e773a93924f422f5cbb_MD5.svg)
- ![](./tarjan_images/1e5e1ae3d9876a6fda96dfd265443984_MD5.svg) – a stack of vertices used to keep the working set of vertices. ![](./tarjan_images/e6346836a84328c0bc7b87a279931d30_MD5.svg) holds all the vertices reachable from the starting vertex. When the algorithm finds an SCC, it will unwind the stack until it gets all the vertices of that SCC

```java
// GLOBAL VARIABLES
//    num <- global array of size V initialized to -1
//    lowest <- global array of size V initialized to -1
//    visited <- global array of size V initialized to false
//    processed <- global array of size V initialized to false
//    s <- global empty stack
//    i <- 0

algorithm DFS(G, v):
    // INPUT
    //    G = the graph
    //    v = the current vertex
    // OUTPUT
    //    Vertices reachable from v are processed, their SCCs are reported

    num[v] <- i
    lowest[v] <- num[v]
    i <- i + 1
    visited[v] <- true
    s.push(v)

    for u in G.neighbours[v]:
        if visited[u] = false:
            DFS(G, u)
            lowest[v] <- min(lowest[v], lowest[u])
        else if processed[u] = false:
            lowest[v] <- min(lowest[v], num[u])

    processed[v] <- true

    if lowest[v] = num[v]:
        scc <- an empty set
        sccVertex <- s.pop()

        while sccVertex != v:
            scc.add(sccVertex)
            sccVertex <- s.pop()

        scc.add(sccVertex)

        Process the found scc in the desired way

    return
```

**Tarjan’s algorithm now takes the form of a series of DFS invocations**:

```java
algorithm TarjanAlgorithm(G):
    // INPUT
    //    G = the graph
    // OUTPUT
    //    SCCs of G are found

    visted <- an empty global visited map
    for v in G.V:
        if visited[v] = false:
            // global variables are accessible from within DFS
            DFS(G, v)
```

## 6. The Complexity Analysis[](https://www.baeldung.com/cs/scc-tarjans-algorithm#the-complexity-analysis)

Tarjan’s algorithm is a modification of the DFS traversal. **Hence, the complexity of the algorithm is linear: ![](./tarjan_images/c2414fc165715a320caa5c905f43cc2b_MD5.svg), where ![](./tarjan_images/7ad05e6e048bbc0fbb8231bba8b0e340_MD5.svg) is the number of vertices and ![](./tarjan_images/dc9aab24fc81af6fa579d195ee55ddf7_MD5.svg) is the number of edges**. Finally, please note that to achieve the mentioned complexity, we must use the adjacency list representation of the graph.

## 7. Conclusion[](https://www.baeldung.com/cs/scc-tarjans-algorithm#conclusion)

In this topic, we’ve discussed **Tarjan’s algorithm for finding strongly connected components in directed graphs. It’s an optimal linear time algorithm.**

Furthermore, it’s easy to implement as it simply modifies the standard DFS traversal.
