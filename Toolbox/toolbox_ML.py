import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, f_oneway, kruskal, shapiro


# Definir la función describe_df
def describe_df(df):

    '''
    Genera un resumen detallado de un DataFrame, mostrando información clave para cada columna. 
    
    Argumentos: 
        - df (pd.DataFrame): El DataFrame a describir. 

    Retorna: 
        - pd.DataFrame: Un DataFrame con las siguientes métricas en las filas por cada columna: 
        - Tipo de Dato: Tipo de datos de la columna (int, float, object, etc.). 
        - Porcentaje de Valores Nulos: Proporción de valores faltantes en la columna. 
        - Valores Únicos: Número de valores únicos presentes en la columna. 
        - Porcentaje de Cardinalidad: Proporción de valores únicos en relación al total de filas.  

    '''

    # Inicializa el diccionario para almacenar los resultados
    description = {
        'Tipo de Dato': [],
        'Porcentaje de Valores Nulos': [],
        'Valores Únicos': [],
        'Porcentaje de Cardinalidad': []
    }
    
    # Itera sobre las columnas del dataframe
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
    
    # Convierte el diccionario en un DataFrame
    description_df = pd.DataFrame(description, index=df.columns).T
    
    return description_df



def tipifica_variables(df, umbral_categoria, umbral_continua):

    '''
    Analiza las columnas de un DataFrame de pandas y clasifica cada una según su tipo de datos, 
    basándose en reglas predefinidas relacionadas con la cardinalidad (cantidad de valores únicos) de las variables. 
    Genera como salida un nuevo DataFrame con el nombre de cada columna y su tipo sugerido.

    Argumentos:
        - df (pd.Dataframe): dataframe de pandas.
        - umbral_categoria (int): define el número máximo de valores únicos (cardinalidad) para clasificar una columna 
            como una variable categórica. Si la cardinalidad es menor a este valor pero mayor que 2, se clasifica como categórica.
        - umbral_continua (float): define el porcentaje mínimo de cardinalidad (número de valores únicos dividido entre la cantidad 
            total de filas) para clasificar una columna como numérica continua. 
            Las columnas que no cumplan con este criterio se clasifican como numéricas discretas.

    Retorna: 
    Un DataFrame que contiene:
        - nombre_variable: Nombre de cada columna del DataFrame original.
        - tipo_sugerido: Tipo sugerido para la variable (Binaria, Categórica, Numérica Continua, o Numérica Discreta).
    
    '''

    # Crear un DataFrame vacío para guardar los resultados
    tipo_sugerido = []

    # Iterar sobre las columnas del DataFrame
    for column in df.columns:
        # Obtener la cardinalidad de la columna
        cardinalidad = df[column].nunique()
        
        # Sugerir el tipo de variable según las reglas dadas
        if cardinalidad == 2:
            tipo = "Binaria"
        elif cardinalidad < umbral_categoria:
            tipo = "Categórica"
        else:
            # Calcular el porcentaje de cardinalidad con respecto al total de filas
            porcentaje_cardinalidad = cardinalidad / len(df)
            if porcentaje_cardinalidad >= umbral_continua:
                tipo = "Numerica Continua"
            else:
                tipo = "Numerica Discreta"
        
        # Añadir el resultado en la lista
        tipo_sugerido.append((column, tipo))
    
    # Convertir la lista de tuplas en un DataFrame
    resultado_df = pd.DataFrame(tipo_sugerido, columns=["nombre_variable", "tipo_sugerido"])
    
    return resultado_df



def get_features_num_regression(df, target_col, umbral_corr, pvalue = None):

    '''
    Genera una lista de variables numéricas de un dataframe, sin añadir el target, 
    estableciendo un umbral de correlación y un p-value que por defecto es None. En caso de que se de valor al p-value,
    la variable deberá ser mayor o igual a 1 - pvalue. 

    Argumentos:
        - df (pd.DataFrame): DataFrame con los datos de entrada.
        - target_col (str): columna objetivo que no debe aparecer en nuestra lista de variables numéricas.
        - umbral_corr (float): Umbral de la correlación para incluir una columna.
        - pvalue (float or None): nivel de significación para el test de correlación. Por defecto es None.

    Retorna:
        - columnas_seleccionadas: lista de columnas numéricas que cumplen con los criterios de correlación.
    
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

    # Selección de colunas numéricas:
    columnas_num = df.select_dtypes(include=[np.number]).columns.tolist()

    # Quita la variable target de las columnas_num si está:
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
        - df (pd.DataFrame): DataFrame con los datos de entrada.
        - target_col (str): Columna objetivo para calcular correlaciones y representar gráficamente. Debe ser numérica.
        - columns (list): Lista de columnas a considerar. Si está vacía, se seleccionan automáticamente las columnas numéricas del DataFrame.
        - umbral_corr (float): Umbral mínimo de valor absoluto de la correlación para incluir una columna.
        - pvalue (float or None): Nivel de significación para el test de correlación. Si es None, no se realiza el test de significación.

    Retorna:
        - list: Lista de columnas que cumplen con los criterios de correlación y significación estadística.

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
    selected_columns = get_features_num_regression(df, target_col=target_col, umbral_corr= umbral_corr, pvalue = None)

    # Generar gráficos por lotes de cinco columnas
    if selected_columns:
        for i in range(0, len(selected_columns), 4):
            subset_columns = selected_columns[i:i+4]
            # Agregar la columna objetivo para el pairplot
            plot_columns = [target_col] + subset_columns
            sns.pairplot(df[plot_columns], diag_kind="kde")
            plt.show()
    else:
        print("No se encontraron columnas que cumplan con los criterios establecidos.")
    
    return selected_columns



def get_features_cat_regression(df, target_col, pvalue=0.05):

    """
    Identifica las columnas categóricas que tienen una relación estadísticamente significativa con 
    una columna objetivo numérica en un DataFrame, usando pruebas estadísticas.

    Argumentos:
        - df (pd.DataFrame): DataFrame que contiene los datos a analizar.
        - target_col (str): Nombre de la columna objetivo que debe ser numérica.
        - pvalue (float, opcional): Nivel de significación para las pruebas estadísticas. Debe estar entre 0 y 1. 
            Por defecto es 0.05.

    Retorna:
        - list: Lista de columnas categóricas que tienen una relación estadísticamente significativa con la columna 
        objetivo.

    """
    # Comprueba si df es efectivamente un data frame y si no, muestra una columna de error
    if not isinstance(df, pd.DataFrame):  
        print("Error: 'df' debe ser un DataFrame."); return None

    # Verifica que target_col (la columna objetivo) exista en el DataFrame y sea de tipo numérico. Si algo falla, muestra un error y termina.
    if target_col not in df.columns or not np.issubdtype(df[target_col].dtype, np.number):  
        print(f"Error: '{target_col}' debe ser una columna numérica en el DataFrame."); return None

    # Comprueba que el valor de pvalue esté entre 0 y 1 (debe ser válido para una prueba estadística). Si no cumple, para.
    if not 0 < pvalue < 1:
        print("Error: 'pvalue' debe estar entre 0 y 1."); return None 
    
    # Busca las columnas categóricas del DataFrame, es decir, las que son de tipo object o category.
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns   


    # Si no encuentra ninguna columna categórica, muestra un error y sale.                                                                                   
    if len(categorical_columns) == 0:
        print("Error: No hay columnas categóricas."); return None
    
    
    # Crea una lista vacía llamada relevant_columns para almacenar las columnas categóricas que tengan una relación estadísticamente significativa con la columna objetivo (target_col).
    relevant_columns = []    
    for col in categorical_columns:

        # Agrupa los datos de target_col por categorías de la columna actual.
        groups = [group.dropna() for _, group in df.groupby(col)[target_col]]  

        # Para cada categoría, filtra las filas correspondientes en el DataFrame (df[df[col] == category]) y selecciona la columna objetivo (target_col).
        if len(groups) < 2 or any(group.empty for group in groups): 
            continue

        # Verifica si los grupos siguen una dstribución normal
        if all(shapiro(g)[1] > pvalue for g in groups if len(g) >= 3):  
            test_result = f_oneway(*groups)
        else:
            test_result = kruskal(*groups)
        if test_result[1] < pvalue:
            relevant_columns.append(col)

    return relevant_columns


def plot_features_cat_regression(df, target_col="", columns=None, pvalue=0.05, with_individual_plot=False):

    """
    Pinta histogramas agrupados para variables significativas y devuelve las variables que cumplen el criterio estadístico.
    
    Argumentos:
        - df (pd.dataframe): df que contiene los datos.
        - target_col (str): Nombre de la columna objetivo. Debe ser numérica continua.
        - columns (list): Lista de variables categóricas a analizar. Si es None, se seleccionarán todas las categóricas del df.
        - pvalue (float): Nivel de significación estadística para considerar una relación como significativa.
        - with_individual_plot (bool): Si True, generará gráficos individuales además de los agrupados.

    Return:
        - selected_features (list): Lista de columnas que tienen una relación significativa con la columna objetivo.

    """
    

    # Check de entradas

    # Se comprueba que el df sea un pd df
    if not isinstance(df, pd.DataFrame):
        print("Error: El argumento 'df' debe ser un pandas df.")
        return None

    # Si no hay una columna target o si esta no está en el df
    if not target_col or target_col not in df.columns:
        print("Error: 'target_col' no está presente en el df.")
        return None
    
    # Esta misma columna target debe ser de tipo numérica continua
    if not np.issubdtype(df[target_col].dtype, np.number):
        print("Error: 'target_col' debe ser una columna numérica y continua.")
        return None
    
    # Comprueba que el p-valor es correcto si está entre 0 y 1 y es numérico
    if not isinstance(pvalue, (float, int)) or not (0 < pvalue < 1):
        print("Error: 'pvalue' debe ser un número entre 0 y 1.")
        return None

    # Comprueba si la lista está vacía
    if not columns:
        columns = df.select_dtypes(include=['category', 'object']).columns.tolist()
        if not columns:
            print("Error: No se encontraron columnas categóricas en el DataFrame.")
    else:
        # Validar que las columnas proporcionadas están en el DataFrame y son categóricas
        columns = [col for col in columns if col in df.columns and df[col].dtype in ['category', 'object']]
        if not columns:
            print("Error: Ninguna de las columnas proporcionadas es categórica o no está en el DataFrame.")
    

    # Selección de features
    selected_features = get_features_cat_regression(df=df, target_col=target_col,pvalue=pvalue)
    

    # Plot de las features significativas

    if selected_features:

        # Verifica si 'with_individual_plot' es True y genera los gráficos correspondientes
        if with_individual_plot:

            for column in selected_features:
                unique_cats = df[column].unique()
                for cat in unique_cats:
                    plt.figure(figsize=(10, 6))
                    sns.histplot(df[df[column] == cat][target_col], kde=True, bins=20, color="skyblue", alpha=0.7)
                    plt.title(f"Distribución de '{target_col}' para '{column}' = '{cat}'")
                    plt.xlabel(target_col)
                    plt.ylabel("Frecuencia")
                    plt.legend()
                    plt.show()

        # Si 'with_individual_plot' es False, genera gráficos agrupados
        # Si es binario el target es diferente a si es continuo
        if df[target_col].nunique() != 2:
            for column in columns:
                unique_cats = df[column].unique()
                
                plt.figure(figsize=(10, 6))
                for cat in unique_cats:
                    sns.histplot(df[df[column] == cat][target_col], kde=True, label=str(cat), bins=20)
                
                plt.title(f'Histograms of {target_col} for {column}')
                plt.xlabel(target_col)
                plt.ylabel('Frequency')
                plt.legend()
                plt.show()
        else:
            for column in columns:
                unique_cats = df[column].unique()
                plt.figure(figsize=(10, 6))
                sns.countplot(x=df[column], hue=df[target_col], data=df)
                plt.title(f'Proporción de {target_col} para {column}')
                plt.xlabel(column)
                plt.ylabel('Count')
                plt.show()
            

    else:
    # Si no había ninguna seleccionada
        print("No se encontraron variables categóricas significativas para el nivel de significancia dado.")
        return None

    return selected_features