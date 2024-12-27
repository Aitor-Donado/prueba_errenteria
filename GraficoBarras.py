import matplotlib.pyplot as plt
import seaborn as sns

for column in datafr.columns:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    
    sns.histplot(data=datafr, x=column, kde=True, ax=axes[0], color='skyblue', edgecolor='black', bins=30)
    axes[0].set_title(f'Histograma con línea de densidad de {column}')
    axes[0].set_xlabel(column)
    axes[0].set_ylabel('Frecuencia')
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    
    sorted_values = datafr[column].value_counts().sort_index()
    axes[1].bar(sorted_values.index, sorted_values.values, color='lightgreen', edgecolor='black')
    axes[1].set_title(f'Gráfico de barras de {column}')
    axes[1].set_xlabel(column)
    axes[1].set_ylabel('Frecuencia')
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()