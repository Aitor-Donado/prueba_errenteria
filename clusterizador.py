from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import seaborn as sns

def grafico_codo(X, min_clusters=1, max_clusters=10):
    clusters = []

    for i in range(min_clusters, max_clusters + 1):
        km = KMeans(n_clusters=i).fit(X)
        clusters.append(km.inertia_)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.lineplot(x=list(range(1, 11)), y=clusters, ax=ax)
    ax.set_title('Codo de inercia decreciente')
    ax.set_xlabel('Clusters')
    ax.set_ylabel('Inercia')

    plt.show()

