import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
import copy



def preferential_connected_graph(n):
    G = nx.Graph()
    G.add_nodes_from([i for i in range(0, n)])
    total_edges = 0
    degrees = [1 for i in range(0, n)]
    while not nx.is_connected(G):
        x, y = random.choices([i for i in range(0, n)], degrees, k=2)
        if x != y:
            G.add_edge(x, y)
            degrees[x] += 1
            degrees[y] += 1
    return G


def random_connected_graph(n):
    G = nx.Graph()
    G.add_nodes_from([i for i in range(0,n)])
    while not nx.is_connected(G):
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        if x != y:
            G.add_edge(x, y)
    return G

n_nodes = list(range(10,251,10))
averages = []
graph_edges = []
for n in n_nodes:
    
    n_edges = []
    for k in range(30):
        n_edges.append(preferential_connected_graph(n).number_of_edges())
    print("\n", n, "nodes")
    print("average number of edges", np.mean(n_edges))
    graph_edges.append(copy.copy(n_edges))
    averages.append(np.mean(n_edges))


plt.xlabel("number of nodes")
plt.ylabel("number of edges until connectivity")
plt.plot(n_nodes, averages)

plt.savefig("graph.pdf")