def describe_df(): 
    print(rellenar)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, f_oneway, kruskal, shapiro

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

def get_features_num_regression(df, target_col, umbral_corr, pvalue = None ):

    '''Genera una lista de variables numéricas de un dataframe, sin añadir el target, 
    estableciendo un umbral de correlación y un p-value que por defecto es None. En caso de que se de valor al p-value,
    la variable deberá ser mayor o iggual a 1 - pvalue. 

    Argumentos:
    df (pd.DataFrame): DataFrame con los datos de entrada.
    target_col: columna objetivo que no debe aparecer en nuestra lista de variables numéricas.
    umbral_corr: Umbral de la correlación para incluir una columna.
    pvalue: nivel de significación para el test de correlación. Por defecto es None.

    Retorna:
    columnas_seleccionadas: lista de columnas numéricas que cumplen con los criterios de correlación.
    
    '''

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

def plot_features_num_regression(df, target_col="", columns=[], umbral_corr=0, pvalue=None):
    """
    Genera gráficos pairplot para analizar la relación entre las variables numéricas y una columna objetivo en un dataframe.
    También filtra y selecciona columnas en función de la correlación y significación estadística.
    
    Argumentos:
    df (pd.DataFrame): DataFrame con los datos de entrada.
    target_col (str): Columna objetivo para calcular correlaciones y representar gráficamente. Debe ser numérica.
    columns (list): Lista de columnas a considerar. Si está vacía, se seleccionan automáticamente las columnas numéricas del DataFrame.
    umbral_corr (float): Umbral mínimo de valor absoluto de la correlación para incluir una columna.
    pvalue (float or None): Nivel de significación para el test de correlación. Si es None, no se realiza el test de significación.

    Retorna:
    list: Lista de columnas que cumplen con los criterios de correlación y significación estadística.
    """

    # Validaciones iniciales
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El argumento 'df' debe ser un DataFrame de pandas.")
    if target_col not in df.columns:
        raise ValueError(f"La columna objetivo '{target_col}' no existe en el DataFrame.")
    if not pd.api.types.is_numeric_dtype(df[target_col]):
        raise ValueError(f"La columna objetivo '{target_col}' debe ser numérica.")
    
    # Seleccionar columnas si la lista está vacía
    if not columns:
        columns = df.select_dtypes(include=['number']).columns.tolist()
        columns.remove(target_col)  # Excluir la columna objetivo
    else:
        columns = [col for col in columns if col in df.columns]
        if not columns:
            raise ValueError("Ninguna de las columnas proporcionadas está en el DataFrame.")
    
    # Filtrar columnas según correlación y p-value
    selected_columns = []
    for col in columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            corr, p = pearsonr(df[col], df[target_col])
            if abs(corr) >= umbral_corr and (pvalue is None or p < pvalue):
                selected_columns.append(col)

    # Generar gráficos por lotes de cinco columnas
    if selected_columns:
        for i in range(0, len(selected_columns), 5):
            subset_columns = selected_columns[i:i+5]
            # Agregar la columna objetivo para el pairplot
            plot_columns = [target_col] + subset_columns
            sns.pairplot(df[plot_columns], diag_kind="kde")
            plt.show()
    else:
        print("No se encontraron columnas que cumplan con los criterios establecidos.")
    
    return selected_columns



def get_features_cat_regression(df, target_col, pvalue=0.05):
    if not isinstance(df, pd.DataFrame):  #Aquí se comprueba si df es efectivamente un data frame y si no, muestra una columna de error
        print("Error: 'df' debe ser un DataFrame."); return None
    if target_col not in df.columns or not np.issubdtype(df[target_col].dtype, np.number):  #Verificamos que: target_col (la columna objetivo) exista en el DataFrame. Sea de tipo numérico. Si algo falla, mostramos un error y terminamos.
        print(f"Error: '{target_col}' debe ser una columna numérica en el DataFrame."); return None
    if not 0 < pvalue < 1:
        print("Error: 'pvalue' debe estar entre 0 y 1."); return None #Comprobamos que el valor de pvalue esté entre 0 y 1 (debe ser válido para una prueba estadística). Si no cumple, paramos.
    
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns   #Aquí buscamos las columnas categóricas del DataFrame, es decir, las que son de tipo object o category.
                                                                                       #Si no encontramos ninguna columna categórica, mostramos un error y salimos.'''
    if len(categorical_columns) == 0:
        print("Error: No hay columnas categóricas."); return None
    
    
    relevant_columns = []    #Creamos una lista vacía llamada relevant_columns para almacenar las columnas categóricas que tengan una relación estadísticamente significativa con la columna objetivo (target_col).
    for col in categorical_columns:
        groups = [group.dropna() for _, group in df.groupby(col)[target_col]] #Aquí se agrupan los datos de target_col por categorías de la columna actual, 
        if len(groups) < 2 or any(group.empty for group in groups): #Para cada categoría, filtramos las filas correspondientes en el DataFrame (df[df[col] == category]) y seleccionamos la columna objetivo (target_col).
            continue
        if all(shapiro(g)[1] > pvalue for g in groups if len(g) >= 3):  #Mediante el código que sigue se verifica si los grupos siguen una dstribución normal
            test_result = f_oneway(*groups)
        else:
            test_result = kruskal(*groups)
        if test_result[1] < pvalue:
            relevant_columns.append(col)

    return relevant_columns

def plot_features_cat_regression():