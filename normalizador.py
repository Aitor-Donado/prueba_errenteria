from sklearn.preprocessing import StandardScaler
import pandas as pd

def normalizador(df, normalizar = True, excepciones = []):
    if not normalizar:
        return df
    ss = StandardScaler()
    data_sin_columnas = ss.fit_transform(df)
    datos_normalizados = pd.DataFrame(data_sin_columnas, columns = df.columns)
    for columna in excepciones:
        datos_normalizados[columna] = df[columna]

    return datos_normalizados