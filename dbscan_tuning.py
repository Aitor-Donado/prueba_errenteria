import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from itertools import product

# Función para evaluar DBSCAN con diferentes hiperparámetros
def tune_dbscan(X, eps_values, min_samples_values):
    best_score = -1  # El índice de silueta varía entre -1 y 1
    best_eps = None
    best_min_samples = None
    best_labels = None

    # Búsqueda en cuadrícula
    for eps, min_samples in product(eps_values, min_samples_values):
        db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
        labels = db.labels_

        # Ignorar casos donde todos los puntos son ruido o solo hay un cluster
        if len(np.unique(labels)) > 1 and np.sum(labels != -1) > 1:
            score = silhouette_score(X, labels)
            if score > best_score:
                best_score = score
                best_eps = eps
                best_min_samples = min_samples
                best_labels = labels

    return best_eps, best_min_samples, best_score, best_labels

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un dataset de ejemplo
    np.random.seed(42)
    X = pd.DataFrame({
        'Income': np.random.normal(50, 15, 200),
        'Score': np.random.normal(60, 10, 200)
    })

    # Definir rangos de hiperparámetros para probar
    eps_values = np.arange(1, 20, 1)  # Valores de eps
    min_samples_values = range(2, 10)  # Valores de min_samples

    # Ajustar hiperparámetros
    best_eps, best_min_samples, best_score, best_labels = tune_dbscan(X, eps_values, min_samples_values)

    # Resultados
    print(f"Mejor valor de eps: {best_eps}")
    print(f"Mejor valor de min_samples: {best_min_samples}")
    print(f"Mejor índice de silueta: {best_score}")

    # Visualizar los clusters óptimos
    import matplotlib.pyplot as plt
    import seaborn as sns

    X['Labels'] = best_labels
    plt.figure(figsize=(11, 9))
    sns.scatterplot(x=X['Income'], y=X['Score'], hue=X['Labels'],
                    palette=sns.color_palette('hls', np.unique(best_labels).shape[0]))
    plt.title(f'DBSCAN con eps={best_eps}, min_samples={best_min_samples}')
    plt.show()