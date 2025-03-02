import networkx as nx
from sklearn.manifold import MDS # Used for multidimensional scaling (visualizing clusters)

import matplotlib.pyplot as plt
from adjustText import adjust_text
import numpy as np

def drawNetwork(G, names):
    labeldict = {}
    for i, name in enumerate(names):
        labeldict[i] = name

    nx.draw_shell(G, labels=labeldict, with_labels=True)
    pos = nx.shell_layout(G)
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()

def drawMDS(G, names):
    X = np.asarray([ [ 1/n if n > 0 else 0 for n in row ] for row in nx.adjacency_matrix(G).toarray() ])

    embedding = MDS(n_components=2, dissimilarity="precomputed")
    X_transformed = embedding.fit_transform(X)

    plt.scatter(X_transformed[:,0], X_transformed[:,1])

    texts = [plt.text(X_transformed[i][0], X_transformed[i][1], names[i], ha='center', va='center') for i in range(len(names))]
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))

    plt.show()