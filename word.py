import os
import array 
import re

from suffix_tree import Tree
import networkx as nx
import matplotlib.pyplot as plt

def lcsweight(f1, f2):
	k = 1
	w = 0
	n = max([len(f1), len(f2)])
	tree = Tree({'A': f1, 'B': f2})
	while(k <= n):
		l1 = [f1[x : x + k] for x in range(0, len(f1) - k + 1)]

		for el in l1:
			count = [0, 0]
			for i, p in tree.find_all(el):
				if i == 'A':
					count[0] += 1  
				else: 
					count[1] += 1
			if count[0] and count[1]:
				w += max(count) * k/n
		k *= 2

	return round(w, 2)

def createNetwork(l):
	G = nx.complete_graph(len(l))

	for e in G.edges:
		G[e[0]][e[1]]['weight'] = lcsweight(l[e[0]], l[e[1]])

	return G

def drawNetwork(names, G):
	labeldict = {}
	for i, name in enumerate(names):
		labeldict[i] = name

	nx.draw_shell(G, labels=labeldict, with_labels=True)
	pos = nx.shell_layout(G)
	nx.draw_networkx_edge_labels(G, pos)
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
print(names)
print(nx.pagerank(G))
drawNetwork(names, G)