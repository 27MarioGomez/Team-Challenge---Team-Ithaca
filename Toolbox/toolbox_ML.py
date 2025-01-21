def describe_df(): 
    print(rellenar)

import pandas as pd

# Definir la función describe_df
def describe_df(df):
    # Inicializamos el diccionario para almacenar los resultados
    description = {
        'Tipo de Dato': [],
        'Porcentaje de Valores Nulos': [],
        'Valores Únicos': [],
        'Porcentaje de Cardinalidad': []
    }
    
    # Iteramos sobre las columnas del dataframe
    for column in df.columns:
        # Tipo de dato
        description['Tipo de Dato'].append(df[column].dtype)
        
        # Porcentaje de valores nulos
        missing_percentage = df[column].isnull().mean() * 100
        description['Porcentaje de Valores Nulos'].append(missing_percentage)
        
        # Valores únicos
        unique_values = df[column].nunique()
        description['Valores Únicos'].append(unique_values)
        
        # Porcentaje de cardinalidad
        cardinality_percentage = (unique_values / len(df)) * 100
        description['Porcentaje de Cardinalidad'].append(cardinality_percentage)
    
    # Convertimos el diccionario en un DataFrame
    description_df = pd.DataFrame(description, index=df.columns)
    
    return description_df

# Cargar el dataset desde la ruta especificada
file_path = r'C:\Users\angel\OneDrive\Documentos\DATA_SCIENCE\Bootcamp\Team-Challenge---Team-Ithaca\Toolbox\data\heart_cleveland_upload.csv'
df = pd.read_csv(file_path)

# Aplicar la función describe_df sobre el dataframe cargado
result = describe_df(df)

# Mostrar el resultado
print(result)


def tipifica_variables():

def get_features_num_regression(df, target_col, umbral_corr, pvalue ):

    #Comprobaciones de la función:
    
    if not isinstance(df, pd.DataFrame):
        print("Error: El argumento 'df' debe ser un DataFrame.")
        return None

    if target_col not in df.columns:
        print(f"Error: La columna '{target_col}' no está en el DataFrame.")
        return None

    if not np.issubdtype(df[target_col].dtype, np.number):
        print(f"Error: La columna '{target_col}' no es numérica.")
        return None

    if not (0 <= umbral_corr <= 1):
        print("Error: El valor de 'umbral_corr' debe estar entre 0 y 1.")
        return None

    if pvalue is not None and (not isinstance(pvalue, float) or not (0 <= pvalue <= 1)):
        print("Error: El valor de 'pvalue' debe ser un float entre 0 y 1.")
        return None

    # selección de colunas numéricas:
    columnas_num = df.select_dtypes(include=[np.number]).columns.tolist()

    # quitamos la variable target de las columnas_num si está:
    columnas_num = [columna for columna in columnas_num if columna != target_col]

    #lista de columnas seleccionadas:
    columnas_seleccionadas = []

    #Calculo de la correlacion
    for columna in columnas_num:
        
        # Calcular la correlación y el p-value
        corr, p_val = pearsonr(df[target_col], df[columna])

        # Verificar si la correlación supera el umbral y si p-value es None o (>= 1 - pvalue proporcionado), si esto se cumple se añade la columna a la lista.
        if abs(corr) > umbral_corr:
            if pvalue is None or p_val >= (1 - pvalue):  
                columnas_seleccionadas.append(columna)

    # Si no hay columnas selecionadas:
    if not columnas_seleccionadas:
            print("Ninguna columna cumple con los criterios especificados.")
            return None
        
    return columnas_seleccionadas

def plot_features_num_regression():

def get_features_cat_regression():

def plot_features_cat_regression():