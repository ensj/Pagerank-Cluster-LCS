from suffix_tree import Tree

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