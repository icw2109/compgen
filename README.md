# Enhanced scRNA-seq Analysis Pipeline

This repository contains an enhanced pipeline for single-cell RNA sequencing (scRNA-seq) analysis. The workflow integrates multiple dimensionality reduction methods, robust clustering evaluations, pseudotime inference, and interactive visualizations into one streamlined pipeline.

---

### Features

- **Data Preprocessing:**  
  Loads and preprocesses scVelo's pancreas dataset with proper scaling and precision adjustments.

- **Dimensionality Reduction:**  
  Implements PCA, t-SNE, and deep learning–based latent space extraction using scVI. UMAP is computed on the scVI latent space for improved embeddings.

- **Clustering and Evaluation:**  
  Performs clustering using Phenograph and evaluates cluster quality via silhouette score and, if available, the Adjusted Rand Index (ARI).

- **Pseudotime Analysis:**  
  Uses scVelo's latent time to infer developmental trajectories for advanced pseudotime analysis.

- **Interactive Visualization:**  
  Provides interactive UMAP visualizations built with Plotly, enabling dynamic exploration of cell clusters and metadata.

---

### Requirements

- **Python 3.6+**

- **Required Python Packages:**

  - scanpy
  - scvelo
  - palantir
  - magic-impute
  - phenograph
  - seaborn
  - scvi-tools
  - plotly
  - scikit-learn

Install dependencies using pip:

```bash
pip install scanpy scvelo palantir magic-impute phenograph seaborn scvi-tools plotly scikit-learn
