# -*- coding: utf-8 -*-
"""compgenproject_icw2109.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16mpa5GqPOvnutJ4rYXj4v3kJUjak0qno
"""

from google.colab import drive
drive.mount('/content/drive')

# May have to restart runtime
!pip install PhenoGraph
!pip install palantir
!pip uninstall -y numpy
!pip install numpy
!pip uninstall -y numba
!pip install numba

#install in order,restart runtime.

import palantir

!pip install scanpy

import scanpy as sc

#!pip install python-magic

#import magic
#import phenograph

#import matplotlib.pyplot as plt

#import pandas as pd

#file_path = '/content/drive/MyDrive/ComputationalGeonomics/marrow_sample_scseq_counts.h5ad'

!pip install scvelo

"""
print("Data shape:", adata.shape)

print("Cell barcodes (top 5):", adata.obs.head())

print("Gene names (top 5):", adata.var.head())

print("Unprocessed data matrix:\n", adata.X.toarray())

print("Cell metadata:", adata.obs)

print("Gene metadata:", adata.var)
"""

import scvelo as scv
import scanpy as sc
import phenograph
import os

#!tar -xzf /content/drive/MyDrive/ComputationalGeonomics/compgen.tar.gz

# Replace this with the path to your folder
#input_folder = "/content/drive/MyDrive/ComputationalGeonomics/filtered_feature_bc_matrix"

# Read the input files
#adata = sc.read_10x_mtx(
#    input_folder,
#    var_names='gene_symbols',
#    cache=True
#)

#data_path = "/content/drive/MyDrive/ComputationalGeonomics/filtered_feature_bc_matrix"

#adata = sc.read_10x_mtx(data_path)

# Check if the dataset contains spliced and unspliced counts
#if "spliced" in adata.layers.keys() and "unspliced" in adata.layers.keys():
#    print("Dataset contains spliced and unspliced counts.")
#else:
#    print("Dataset does not contain spliced and unspliced counts.")

#import tarfile

#tar_path = '/content/drive/MyDrive/ComputationalGeonomics/GSE109774_Marrow.tar.gz'
#output_path = '/content/drive/MyDrive/ComputationalGeonomics/extracted_data'

#with tarfile.open(tar_path, 'r:gz') as tar:
#    tar.extractall(path=output_path)

#!tar -xzf /content/drive/MyDrive/ComputationalGeonomics/GSE109774_Marrow.tar.gz -C /content/drive/MyDrive/ComputationalGeonomics

"""Main Project Start."""

######################################################################################################################
######################################################################################################################
# MAIN PROJECT START
######################################################################################################################
#######################################################################################################################

!pip install scvelo --upgrade --quiet

import scvelo as scv
scv.logging.print_version()

adata = scv.datasets.pancreas()
adata

adata.X

adata.layers['spliced']
adata.layers['unspliced']

import pandas as pd
import numpy as np
!pip install magic-impute
import magic
import phenograph
import scvelo as scv

#NOt Directetly relevent cell

adata.layers["spliced"] = adata.layers["spliced"].astype("float64")
adata.layers["unspliced"] = adata.layers["unspliced"].astype("float64")

# Preprocessing
#scv.pp.filter_and_normalize(adata)
#scv.pp.moments(adata)

scv.tl.velocity(adata)

scv.tl.velocity_graph(adata)

scv.tl.velocity_embedding(adata, basis='umap')

dense_matrix = adata.X.toarray()
ms = dense_matrix.sum(axis=1)
normalized_matrix = (dense_matrix / ms[:, np.newaxis]) * np.median(ms)
log_transformed_matrix = palantir.preprocess.log_transform(normalized_matrix)
df = pd.DataFrame(log_transformed_matrix, index=adata.obs_names, columns=adata.var_names)
dm_res = palantir.utils.run_diffusion_maps(df)

#NOt Directetly relevent cell

scv.tl.velocity_graph(adata)
scv.tl.velocity_embedding(adata, basis='umap')
dense_matrix = adata.X.toarray()
ms = dense_matrix.sum(axis=1)
normalized_matrix = (dense_matrix / ms[:, np.newaxis]) * np.median(ms)
log_transformed_matrix = palantir.preprocess.log_transform(normalized_matrix)
df = pd.DataFrame(log_transformed_matrix, index=adata.obs_names, columns=adata.var_names)
dm_res = palantir.utils.run_diffusion_maps(df)

#NOt Directetly relevent cell

magic_operator = magic.MAGIC()
magic_res = magic_operator.fit_transform(df)
_, _, clusters = phenograph.cluster(magic_res, k=30)  
adata.obs['palantir_clusters'] = pd.Series(clusters, index=adata.obs.index)

velocity_clusters = adata.obs['palantir_clusters'].unique()
average_velocities = {}

for cluster in velocity_clusters:
    cluster_cells = adata[adata.obs['palantir_clusters'] == cluster]
    cluster_velocity = np.mean(cluster_cells.obsm['velocity_umap'], axis=0)
    average_velocities[cluster] = cluster_velocity

load_ad = adata.X

ad = sc.AnnData(load_ad)

ad

import pickle

!pip install python-louvain

import community
import random

#!wget https://s3.amazonaws.com/dp-lab-data-public/palantir/human_cd34_bm_rep%5B1-3%5D.h5ad

#NOt Directetly relevent cell

adata = scv.datasets.pancreas()

sc.pp.log1p(adata)
normalized_df = adata.to_df()

dm_res = palantir.utils.run_diffusion_maps(normalized_df)

ms_data = palantir.utils.determine_multiscale_space(dm_res)

num_cells = adata.shape[0]
random_index = random.randint(0, num_cells - 1)
early_cell = adata.obs_names[random_index]

num_terminal_states = 3
terminal_states = random.sample(list(adata.obs_names), num_terminal_states)
pt = palantir.core.run_palantir(dm_res, early_cell=early_cell, terminal_states=terminal_states, num_waypoints=500)

bp_res = palantir.branch_point_analysis.run_branch_point_analysis(dm_res, pt)

# Plot the results
palantir.plot.plot_palantir_results(dm_res, pt, bp_res)

adata = scv.datasets.dentategyrus()

scv.pp.filter_and_normalize(adata)
scv.pp.moments(adata, n_neighbors=30, n_pcs=30)

scv.tl.velocity(adata)
scv.tl.velocity_graph(adata)
 
scv.tl.umap(adata)

scv.pl.velocity_embedding_stream(adata, basis='umap')

adata = scv.datasets.dentategyrus()

scv.pp.filter_and_normalize(adata)
scv.pp.moments(adata, n_neighbors=30, n_pcs=30)

scv.tl.velocity(adata)
scv.tl.velocity_graph(adata)
scv.tl.umap(adata)
scv.pl.velocity_embedding_stream(adata, basis='umap')

# Convert AnnData object to a Pandas DataFrame
expr_matrix = pd.DataFrame(adata.X.toarray(), index=adata.obs.index, columns=adata.var.index)

#NOt Directetly relevent cell
#adata.obs['branching_points'] = branching_points
#sc.pl.umap(adata, color='branching_points', size=50)
#scv.pl.velocity_embedding_stream(adata, basis='umap', color='branching_points', size=50)

####################################################################
#####################################################################
######################################################################
# Following Used to Generate Graphs in Report, Primary Data pipeline.
###############################################################

# Commented out IPython magic to ensure Python compatibility.
#matplotlib.rcParams['font.family'] = 'DejaVu Sans'
# %matplotlib inline

import random

adata = scv.datasets.pancreas()

sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
adata = adata[:, adata.var.highly_variable]
sc.pp.scale(adata, max_value=10)
sc.tl.pca(adata, svd_solver='arpack')

pca_df = pd.DataFrame(adata.obsm['X_pca'])
dm_res = palantir.utils.run_diffusion_maps(pca_df, n_components=5)

early_cell_index = random.randint(0, adata.n_obs - 1)

pr_res = palantir.core.run_palantir(dm_res['EigenVectors'], early_cell=early_cell_index, num_waypoints=500)

scv.pp.filter_and_normalize(adata, min_shared_counts=20, n_top_genes=2000)
scv.pp.moments(adata, n_pcs=30, n_neighbors=30)
scv.tl.velocity(adata)

scv.tl.velocity_graph(adata)
sc.tl.umap(adata)
scv.tl.velocity_embedding(adata, basis='umap')

scv.pl.velocity_embedding_stream(adata, basis='umap', color='clusters')

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

velocities = adata.layers['velocity']
velocity_norm = np.linalg.norm(velocities, axis=1)

adata.obs['rna_velocity'] = velocity_norm
adata.obs['palantir_clusters'] = pr_res.cluster

cluster_mean_rna_velocity = adata.obs.groupby('palantir_clusters')['rna_velocity'].mean()
print("Average RNA velocity per Palantir cluster:")
print(cluster_mean_rna_velocity)

pr_res.pseudotime = pr_res.pseudotime.reindex(umap_coords.index)

plot_palantir_umap(pr_res, umap_coords)

import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn as sns

def plot_palantir_umap(pr_res, umap_coords, s=5):
    fig = plt.figure(figsize=[12, 4])
    gs = plt.GridSpec(2, 4)
    
    # Pseudotime
    ax = plt.subplot(gs[0:2, 1:3])
    c = pr_res.pseudotime[umap_coords.index]
    scatter = ax.scatter(umap_coords.iloc[:, 0], umap_coords.iloc[:, 1], s=s, cmap=matplotlib.cm.plasma, c=c)
    normalize = matplotlib.colors.Normalize(vmin=np.min(c), vmax=np.max(c))
    cax = plt.colorbar(matplotlib.cm.ScalarMappable(norm=normalize, cmap=matplotlib.cm.plasma),
                       ax=ax, ticks=np.linspace(np.min(c), np.max(c), 5))
    cax.ax.set_yticklabels(np.linspace(np.min(c), np.max(c), 5), fontsize=15)
    cax.ax.set_ylabel('Pseudo-time', fontsize=15)
    ax.set_title('Pseudo-time', fontsize=15)
    ax.set_xticks([])
    ax.set_yticks([])
    sns.despine(ax=ax, bottom=True, left=True)

    plt.tight_layout()
    plt.show()
    
umap_coords = pd.DataFrame(adata.obsm['X_umap'], index=adata.obs.index)
plot_palantir_umap(pr_res, umap_coords)

adata = sc.datasets.paul15()

pr_res = palantir.core.run_palantir(dm_res['EigenVectors'], early_cell=0)

!pip install --upgrade matplotlib

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


fig, ax = plt.subplots(figsize=(10, 10))
sns.scatterplot(x=adata.obsm['X_umap'][:, 0], y=adata.obsm['X_umap'][:, 1],
                hue=adata.obs['palantir_clusters'], palette='viridis', alpha=0.5, ax=ax)
ax.set_xlabel('UMAP1')
ax.set_ylabel('UMAP2')
ax.legend(title='Clusters')
plt.show()

import warnings
scv.pl.velocity_embedding_stream(adata, basis='umap', color='palantir_clusters')
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

adata.obs['average_velocity_x'] = adata.obs['palantir_clusters'].map({k: v[0] for k, v in average_velocities.items()})
adata.obs['average_velocity_y'] = adata.obs['palantir_clusters'].map({k: v[1] for k, v in average_velocities.items()})

fig, ax = plt.subplots(figsize=(10, 10))
scatter = sns.scatterplot(x=adata.obsm['X_umap'][:, 0], y=adata.obsm['X_umap'][:, 1],
                          hue=adata.obs['palantir_clusters'], palette='viridis', alpha=0.5, ax=ax)

# Add quiver plot on top of the scatter plot to represent the average velocities
ax.quiver(adata.obsm['X_umap'][:, 0], adata.obsm['X_umap'][:, 1],
          adata.obs['average_velocity_x'], adata.obs['average_velocity_y'],
          color='k', scale_units='xy', scale=1, width=0.003, alpha=0.8)

ax.set_xlabel('UMAP1')
ax.set_ylabel('UMAP2')
ax.legend(title='Clusters')
plt.show()

plt.show()

!find . -name '*.ipynb' -o -name '*.py' | xargs wc -l

############################################################
#################################################################


############################









