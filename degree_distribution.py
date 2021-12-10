import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt 

def preferential_tree(n):
    G = nx.Graph()
    G.add_node(0)
    node_count = 1
    degrees = [1]
    for i in range(n):
        x = random.choices([i for i in range(0, node_count)], degrees, k=1)[0]
        G.add_node(node_count)
        G.add_edge(x, node_count)
        degrees[x] += 1
        node_count += 1
        degrees.append(1)
    return G


k=100
n_nodes_list = [10, 50, 100, 500, 1000, 1500]
for n_nodes in n_nodes_list:
    results = []
    for i in range(k):
        g = preferential_tree(n_nodes)

        degrees_distribution = [i[1] for i in g.degree]
        degrees_distribution.sort(reverse=True)
        results.append(degrees_distribution)

    avg_results = []
    for idx in range(len(results[0])):
        col = [r[idx] for r in results]
        avg_results.append(np.mean(col))
        
    plt.figure()
    plt.plot(avg_results)
    plt.savefig("degree_distribution"+str(n_nodes)+".png")

    #nx.draw(g)
    #plt.savefig("graph.png")