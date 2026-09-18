#!/usr/bin/env python
"""Chapter 11: KMeans clustering and PCA dimensionality reduction."""

from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


def main() -> None:
    iris = load_iris()
    x = iris.data

    kmeans = KMeans(n_clusters=3, random_state=33, n_init=10)
    labels = kmeans.fit_predict(x)

    pca = PCA(n_components=2)
    reduced = pca.fit_transform(x)

    print("Silhouette score:", round(silhouette_score(x, labels), 4))
    print("PCA output shape:", reduced.shape)
    print("Explained variance ratio:", pca.explained_variance_ratio_)


if __name__ == "__main__":
    main()
