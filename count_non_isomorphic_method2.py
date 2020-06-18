import networkx as nx
import numpy as np
import pickle as pk


def store_count(count,path):
    file = open(path+".dat", 'wb')
    pk.dump(count, file)
    file.close()

def load_count(path):
    ff = open(path, 'rb')
    f = pk.load(ff)
    ff.close()
    return(f)


# input an array of graphs:
# [ GO12_1,GO12_2,GO12_3,G123_1, ....]
# output
# dict:
# {
#   nx.graph: count,
#   nx.graph: count, ....
# }
def count_non_isomorphic_graphs(flat_res):
    group = dict()
    group[flat_res[0]] = 0
    for graph in flat_res:
        add = True
        for iso in group:
            if (nx.is_isomorphic(iso,graph)):
                add = False
                # puoi usare break solo se NON li vuoi contare
                #break
                group[iso] = group[iso] + 1
        if(add):
            group[graph] = 1
    return(group)

#### tmp
#### returns
# {
#   nx.graph: [nx.graph,nx.graph,nx.graph,nx.graph,...],
#   nx.graph: [nx.graph,nx.graph,nx.graph,nx.graph,...], ....
# }
def getall_non_isomorphic_graphs(flat_res):
    group = dict()
    group[flat_res[0]] = []
    for graph in flat_res:
        add = True
        for iso in group:
            if (nx.is_isomorphic(iso,graph)):
                add = False
                # puoi usare break solo se NON li vuoi contare
                #break
                group[iso].append(graph)

        if(add):
            group[graph] = [graph]
    return(group)

# input an array of graphs:
# [ GO12_1,GO12_2,GO12_3,G123_1, ....]
# output
# array of non isomorphic graphs
def get_non_isomorphic_graphs(flat_res):
        # dividili in gruppi    
    group = []
    group.append(flat_res[0])
    for graph in flat_res:
        add = True
        for iso in group:
            if (nx.is_isomorphic(iso,graph)):
                add = False
                break
        if(add):
            group.append(graph)
        
    return (group)


def get_flat_array(res):
    flat_res = []
    for i in res:
        for tmp in i:
            g = tmp
            flat_res.append(g)
    return(flat_res)



