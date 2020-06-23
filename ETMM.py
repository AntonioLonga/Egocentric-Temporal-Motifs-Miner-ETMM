import numpy as np
from ETN import *

def get_ETM(counts,alpha,beta,gamma):
    over = over_representation(counts,alpha)
    mdev = minimum_deviation(counts,beta)
    mfrq = minimum_frequency(counts,gamma)
    valid = mfrq * over * mdev

    ETM = []
    ETNS = list(counts.keys())
    for k in range(len(ETNS)):
        if(valid[k]==1):
            ETM.append([ETNS[k],counts[ETNS[k]][0]])
    return(ETM)

def minimum_deviation(counts,beta):
    N_G = np.array(list(counts.values()))[:,0]
    N_G0 = np.array(list(counts.values()))[:,1:]

    N_G0_mean = np.mean(N_G0,-1)
    valid = []
    for i in range(len(N_G)):

        if(N_G[i] - N_G0_mean[i] > beta * N_G0_mean[i]):
            valid.append(1)
        else:
            valid.append(0)
            
    return(np.array(valid))
    
    
def over_representation(counts,alpha=0.01):
    N_G = np.array(list(counts.values()))[:,0]
    N_G0 = np.array(list(counts.values()))[:,1:]
    alpha = 0.01
    valid = []
    for j in range(len(N_G)):
        P = 0
        for i in N_G0[j]:
            if (i > N_G[j]):
                P = P + 1
        P = P/len(N_G0[j])
        if(P<alpha):
            valid.append(1)
        else:
            valid.append(0)
    return(np.array(valid))

def minimum_frequency(counts,gamma=5):
    
    N_G = np.array(list(counts.values()))[:,0]
    valid = []
    for i in N_G:
        if(i >= gamma):
            valid.append(1)
        else:
            valid.append(0)
    return(np.array(valid))


def counts_ETN_null_models(null_models,S,k,verbose):
    counts = dict()
    for i in list(S.keys()):
        counts[i] = [S[i]]
    c = 1
    for null_model in null_models:
        S_i = count_ETN_null_model(S,null_model,k)
        for j in list(S_i.keys()):
            counts[j].append(S_i[j])
        if (verbose):
            print("done",c)
        c = c + 1
    return (counts)

def count_ETN_null_model(S_in,graphs,k):
    S = S_in.copy()
    for i in S:
        S[i] = 0
    for i in range(len(graphs)-k + 1):
        for v in graphs[i].nodes():
            etn = build_ETN(graphs[i:i+k+1],v)
            etns = get_ETNS(etn)
            if etns in S.keys():
                S[etns] = S[etns] + 1
    return(S)


def shuffle_graphs(graphs_in,n,seed): # Shuffle array of graphs
    graphs = graphs_in.copy()
    null_models = []
    for i in range(n):
        np.random.seed(seed+i)
        np.random.shuffle(graphs)
        null_models.append(graphs.copy())
        
    return(null_models)