import pandas as pd
import plotly.graph_objs as go

def mi_descripcion(df):
    descripcion = df.describe(include="all").T
    descripcion["Tipos"] = df.dtypes
    descripcion["Nulos"] = df.isna().sum()
    descripcion["Únicos"] = df.nunique()
    return descripcion

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

def dumifica_columna_comas(df, columna, inplace=False):
    if not inplace:
        df = df.copy()
    categorias_unicas = set()
    for lista_categorias in df[columna].dropna():  # Drop NaN values to avoid errors
        for categoria in lista_categorias.split(','):
            categorias_unicas.add(categoria.strip())

    for categoria in categorias_unicas:
        df[categoria] = df[columna].str.contains(categoria, regex=False).astype(int)

    return df

pd.DataFrame.descripcion = mi_descripcion
pd.DataFrame.rotable_3d = rotable_3d
pd.DataFrame.dumifica_columna_comas = dumifica_columna_comas

def aplana_json(json_obj: dict, prefix: str = '') ->dict:
    """
    Convierte un diccionario con claves anidadas en un diccionario plano.
    Todas las claves son la sucesión (path) de claves hasta llegar a los valores en el original.
    Los valores del diccionario resultante no contienen diccionarios
    """
    # Creamos el diccionari que servirá de salida
    dict_plano = {}
    # Si lo que se ha introducido no es un diccionario, lo devolvemos como diccionario 
    # para evitar errores en las llamadas recursivas
    if not isinstance(json_obj, dict) and not isinstance(json_obj, list):
        return {prefix: json_obj}
    for clave, valor in json_obj.items():
        # Concatena las claves sólo si hay path ya concatenado, si no, es la clave misma
        nueva_clave = f"{prefix}.{clave}" if prefix else clave
        if isinstance(valor, dict):
            # Si el valor es un diccionario, se autollama recursivamente
            dict_plano.update(aplana_json(valor, nueva_clave))
        elif isinstance(valor, list):
            # Si el valor es una lista, añade el índice a la clave y se autollama recursivamente
            for i, item in enumerate(valor):
                dict_plano.update(aplana_json(item, f"{nueva_clave}.{i}"))
        else:
            # Si no es dict ni list, guarda clave y valor al dict plano
            dict_plano[nueva_clave] = valor
    return dict_plano

if __name__ == "__main__":
    diccionario = {"Clave_principal1" : "valor1", 
                "Clave_principal2" : "valor2", 
                "Clave_principal3" : {"Clave_anidada1": "Valor anidado en primer nivel"}, 
                "Clave_principal4" : [{"Clave_anidada1": "Valor anidado en lista"}, {"Clave_anidada2": "Valor anidado en lista"}], 
                "Clave_principal5" : ["Valor anidado en lista", "Valor anidado en lista"], 
                }
    
    print(aplana_json(diccionario))