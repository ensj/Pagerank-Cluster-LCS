import os # Used for the weighting algorithm and the pagerank algorithm
import array 
import re # regex

from suffix_tree import Tree
import networkx as nx

import numpy as np # Used for visualization and ease of handling data
import matplotlib.pyplot as plt

from sklearn.manifold import MDS # Used for multidimensional scaling (visualizing clusters)

# Proposed by Phil
def percentweight(f1, f2):
    #finds %of f1 that is contained in f2
    #so directed edge in one direction f1->f2
    #returns (|words contained in f1&f2|/length of f1)
    #try running both commented and uncommetned on small files
    n = len(f1)
    score = 0
    
    l1 = [f1[x : x + 1] for x in range(0, len(f1))]
    tree = Tree({'A': f2})
    for el in l1:
        if tree.find(el):
            score+=1
    return score/n

# Proposed by Tran
def lcsweight(f1, f2):
    k = 1
    w = 0
    n = len(f1)
    tree = Tree({'A': f2})
    while(k <= n):
        l1 = [f1[x : x + k] for x in range(0, len(f1) - k + 1)]
        for el in l1:
            if(tree.find(el)):
                w += 1
                break # if a sequence of k words exists between both files, break the loop and update k
        k *= 2

    return w

def createNetwork(l):
    G = nx.complete_graph(len(l))
    #G = G.to_directed()

    for e in G.edges:
        G[e[0]][e[1]]['weight'] = lcsweight(l[e[0]], l[e[1]])
        #G[e[1]][e[0]]['weight'] = lcsweight(l[e[1]], l[e[0]]) #meaningless with log alg
        #print("1: ", G[e[0]][e[1]]['weight'], " 2: ", G[e[1]][e[0]]['weight'])

    return G

def drawNetwork(names, G):
    labeldict = {}
    for i, name in enumerate(names):
        labeldict[i] = name

    nx.draw_shell(G, labels=labeldict, with_labels=True)
    pos = nx.shell_layout(G)
    nx.draw_networkx_edge_labels(G, pos)
    plt.show()

def drawMDS(G) 
    X = np.asarray([ [ 1/n if n > 0 else 0 for n in row ] for row in nx.adjacency_matrix(G).toarray() ])

    embedding = MDS(n_components=2, dissimilarity="precomputed")
    X_transformed = embedding.fit_transform(X)

    plt.scatter(X_transformed[:,0], X_transformed[:,1])
    plt.show()


def wordify(filecontent):
    p = re.compile(r"\w+")
    return p.findall(filecontent)

names = []
words = []
for filename in os.listdir('input'):
    if(filename.endswith('.py')):
        names.append(filename)
        with open(os.path.join('input', filename)) as f:
            words.append(wordify(f.read()))

G = createNetwork(words)
#print(names)
#print(nx.pagerank(G))

#drawNetwork(names, G)
#drawMDS(G)