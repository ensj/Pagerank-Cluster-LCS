import os # Used for the weighting algorithm and the pagerank algorithm
import re # regex

import networkx as nx
from weight import lcsweight, percentweight

import numpy as np # Used for visualization and ease of handling data

from visualizer import drawNetwork, drawMDS

def createNetwork(l, w, double_edge=False): 
    G = nx.complete_graph(len(l))
    if double_edge: 
        G = G.to_directed()

    for e in G.edges:
        G[e[0]][e[1]]['weight'] = w(l[e[0]], l[e[1]])
        if double_edge: 
            G[e[1]][e[0]]['weight'] = w(l[e[1]], l[e[0]]) 

    return G

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

G = createNetwork(words, lcsweight)
#print(names)
#print(nx.pagerank(G))

drawNetwork(names, G)
#drawMDS(G)