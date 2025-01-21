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

def get_features_num_regression():

def plot_features_num_regression():

def get_features_cat_regression():

def plot_features_cat_regression():