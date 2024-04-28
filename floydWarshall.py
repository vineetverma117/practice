#It is used to find the shortest paths between all pairs of nodes in a weighted graph
V = 4
INF = 100000

def floydWarshall(graph):
   

    dist = graph
    print(dist)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)



def printSolution(dist):
    print("every node shorted path")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d " % (dist[i][j]), end=' ')
            if j == V-1:
                print()


# Driver's code
if __name__ == "__main__":
    
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]
    # Function call
    floydWarshall(graph)
