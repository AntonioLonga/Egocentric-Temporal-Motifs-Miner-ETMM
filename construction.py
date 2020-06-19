import networkx as nx
import numpy as np


from tabulate import tabulate


def load_data(path):
    data = []
    with open(path) as f:
        for line in f:
            tmp = line.split()[0:3]
            arr_tmp = [int(tmp[0]),int(tmp[1]),int(tmp[2])]
        
            data.append(arr_tmp)
    data = np.array(data)
    return(data)


def individuals(data):
    return(np.unique(data[:,1:]))





def build_graphs(data,gap=19):
    graphs = []
    G=nx.Graph()
    nodes = individuals(data)
    G.add_nodes_from(nodes)
    splitted_data = split_input_data(data,gap)
    
    for t in splitted_data:
        g = G.copy()
        for _,i,j in t:
            g.add_edge(i,j)
        graphs.append(g)  

    return(graphs)




def split_input_data(data, gap=19):
    times = data[:,0]
    pos = times[0]
    chunks = []
    for i in range(len(times)):
        if not(times[i]<=(pos + gap)):
            chunks.append(i)
            pos = times[i]

    return(np.split(data,chunks))

