# Clustering


To do (ppt)
---
- **Explain why choose 7 clusters:**
    We want to use Kmeans to cluster datas, and the way we determine value of k is by Elbow(within-cluster variance) and Silhouette(the average distance between clusters) method.

    **Elbow Method:**

    ![](https://i.imgur.com/W6hZW6f.png)
    **Silhouette Method:**

    ![](https://i.imgur.com/BQVmpvs.png)
    ![](https://i.imgur.com/k3rW7Pa.png)
    
    And we will discover that **k = 7** will be the optimal k since it is the location of  bend (knee) in the plot Elbow, and is also the relatively large value in plot Silhouette.

    **Distribution(TSNE):**

    ![](https://i.imgur.com/uQJxhPl.png)
    
    **Features' Mean of each cluster:**

    ![](https://i.imgur.com/cUUV2QU.png)



Internal measures for cluster validation
---
- Internal validation measures reflect often the compactness, the connectedness and the separation of the cluster partitions.
1. **Compactness or cluster cohesion**: Measures how close are the objects within the same cluster. A lower within-cluster variation is an indicator of a good compactness (i.e., a good clustering). The different indices for evaluating the compactness of clusters are base on distance measures such as the cluster-wise within average/median distances between observations.
2. **Separation**: Measures how well-separated a cluster is from other clusters. The indices used as separation measures include:distances between cluster centersthe pairwise minimum distances between objects in different clusters
3. **Connectivity**: corresponds to what extent items are placed in the same cluster as their nearest neighbors in the data space. The connectivity has a value between 0 and infinity and should be minimized.

**Silhouette coefficient**:
---

The silhouette analysis measures how well an observation is clustered and it **estimates the average distance between clusters**

1. For each observation i, calculate the average dissimilarity ai between i and all other points of the cluster to which i belongs.

2. For all other clusters C, to which i does not belong, calculate the average dissimilarity d(i,C) of i to all observations of C. The smallest of these d(i,C) is defined as bi=minCd(i,C). The value of bi can be seen as the dissimilarity between i and its “neighbor” cluster, i.e., the nearest one to which it does not belong.

3. Finally the silhouette width of the observation i is defined by the formula: Si=(bi−ai)/max(ai,bi).

Elbow method
---
The Elbow method looks at the total WSS as a function of the number of clusters: One should choose a number of clusters so that adding another cluster doesn’t improve much better the total WSS.
1. Compute clustering algorithm (e.g., k-means clustering) for different values of k. For instance, by varying k from 1 to 10 clusters.

2. For each k, calculate the total within-cluster sum of square (wss).

3. Plot the curve of wss according to the number of clusters k.

4. The location of a bend (knee) in the plot is generally considered as an indicator of the appropriate number of clusters.


