import plotly.graph_objs as go
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def grafico_correlacion(data: pd.DataFrame):
    sns.set_theme(style="white")

    data = data.select_dtypes("number")
    data = data.dropna()
    # Compute the correlation matrix
    corr = data.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, annot=True, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})


# Función para pintar las reglas en 3D
def rotable_3d(x, col1, col2, col3, cat_col):
    datos = x.copy()
    # Reseteo el índice de los datos originales
    datos.reset_index(inplace=True)

    # Crear el scatter plot en 3D con Plotly
    fig = go.Figure(data=[go.Scatter3d(
        x=datos[col1],
        y=datos[col2],
        z=datos[col3],
        mode='markers',
        marker=dict(
            size=10,
            color=datos[cat_col],  # Color según el valor de la categoría
            colorscale='Viridis',  # Escala de color
            opacity=0.8
        ),
        text='<br>' + \
             col1 + ": " + datos[col1].astype(str) + '<br>' + \
             col2 + ": " + datos[col2].astype(str) + '<br>' + \
             col3 + ": " + datos[col3].astype(str),
        hoverinfo='text'  # Mostrar texto en el menú emergente
    )])

    # Configuración del diseño del gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title=col1,
            yaxis_title=col2,
            zaxis_title=col3,
        ),
        title='Scatter Plot 3D del dataset de Iris',
        width=800,
        height=1200,
    )

    # Mostrar el gráfico
    fig.show()