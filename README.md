# Egocentric Temporal Motifs Miner (ETMM)
Here you can find the code associated with the paper "An Efficient Procedure for Mining Egocentric
Temporal Motifs". [paper](https://arxiv.org/pdf/2110.01391.pdf)

You can find a tutorial [here](https://antoniolonga.github.io/posts/ETMM.html)

## Installation
Download the repository and import files as follow:

```python
import construction as cs
from ETN import *
from ETMM import *
```
then, given a temporal graph represented in an edge list (like those in Dataset/) and a temporal gap, you can build an ordered sequence of static snapshots with:

```python
# Parameters 
gap = 299   # temporal gap
file_name = "InVS13" # name of the file
data = cs.load_data("Datasets/"+file_name+".dat")
graphs = cs.build_graphs(data,gap=gap,with_labels=False)
```
Since the array of static graphs is computed you can count ETN (given k) simply by:
```python
S = count_ETN(graphs,k,meta=meta_data)
S = {k: v for k, v in sorted(S.items(), key=lambda item: item[1], reverse=1)}

store_etns(S,file_name,gap,k,label=label) # store the ETN counts
```

## References
[1] Longa, A. et al (2021). An Efficient Procedure for Mining Egocentric
Temporal Motifs.

## License
[MIT](https://choosealicense.com/licenses/mit/)
