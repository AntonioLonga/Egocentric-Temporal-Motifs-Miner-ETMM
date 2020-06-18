import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


from tabulate import tabulate

def split_data_in_groups(path_data,path_metadata):

    data = load_data(path_data)
    file_metadata = path_metadata

    metadata = dict()
    with open(file_metadata) as f:
        for line in f:
            node,group = line.split()
            metadata[int(node)] = group

    groups = dict()
    person_type = []
    for i in np.unique(list(metadata.values())):
        person_type.append(i)

    person_type.append("Mixed")

    for i in person_type:
        groups[i] = []


    for t,i,j in data:
        if(metadata[i] == metadata[j]):
            groups[metadata[i]].append([t,i,j]) 
        else:
            person = "Mixed"
            groups[person].append([t,i,j])


    interactions_in_group = [len(x) for x in groups.values()]
    node_in_group = [len(np.unique(np.array(x)[:,1:])) for x in groups.values()]
    print(tabulate([["Name"]+list(groups.keys())+["TOT"],
                    ["interactions"]+interactions_in_group+[len(data)],
                    ["nodes"]+node_in_group+[len(individuals(data))]]))

    for key in groups.keys():
        groups[key] = np.array(groups[key])
    return(groups)


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



def build_weighted_graph(data,gap=19):
    nodes = individuals(data)
    graphs,pos = build_graphs(data,gap)

    G = nx.complete_graph(nodes)
    for e in G.edges():
        G[e[0]][e[1]]["weight"]=0

    for g in graphs:
        for e in g.edges():
            G[e[0]][e[1]]["weight"] = G[e[0]][e[1]]["weight"] + 1
    GG = G.copy()
    for e in G.edges():
        if (G[e[0]][e[1]]["weight"] == 0):
            GG.remove_edge(e[0],e[1])
            
    return(GG)


def not_consecutive_duplicates_data(data):
    i_old = 0
    j_old = 0
    new_data = []
    for t,i,j in data:
        if not(i == i_old and j==j_old):
            i_old = i
            j_old = j
            new_data.append([t,i,j])
    new_data = np.array(new_data)
    return(new_data)
    
def build_weighted_graph_2(data,gap=19):
    nodes = individuals(data)
    data = not_consecutive_duplicates_data(data)
    graphs,pos = build_graphs(data,gap)

    G = nx.complete_graph(nodes)
    for e in G.edges():
        G[e[0]][e[1]]["weight"]=0

    for g in graphs:
        for e in g.edges():
            G[e[0]][e[1]]["weight"] = G[e[0]][e[1]]["weight"] + 1
    GG = G.copy()
    for e in G.edges():
        if (G[e[0]][e[1]]["weight"] == 0):
            GG.remove_edge(e[0],e[1])
            
    return(GG)



def build_graphs(data,gap=19):
    graphs = []
    G=nx.Graph()
    nodes = individuals(data)
    G.add_nodes_from(nodes)
    pos = nx.spring_layout(G)
    splitted_data = split_input_data(data,gap)
    
    for t in splitted_data:
        g = G.copy()
        for _,i,j in t:
            g.add_edge(i,j)
        graphs.append(g)  

    return(graphs,pos)




def split_input_data(data, gap=19):
    times = data[:,0]
    pos = times[0]
    chunks = []
    for i in range(len(times)):
        if not(times[i]<=(pos + gap)):
            chunks.append(i)
            pos = times[i]

    return(np.split(data,chunks))

