import chardet
import pandas as pd
# Ruta del archivo
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/circuits.csv'
#  file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/constructor_results.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/constructor_standings.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/constructors.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/drivers_standings.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/drivers.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/lap_times.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/pit_stops.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/qualifying.csv'
file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/races11.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/results.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/seasons.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/sprint_results.csv'
#file_path = 'C:/Users/CONECTIA BA/Desktop/F1/RAW DATA/status.csv's

# Detectar la codificación
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    print(f"Codificación detectada para {file_path}: {result['encoding']}")
    

# Cargar el archivo CSV con la codificación detectada
df = pd.read_csv(file_path)

# Mostrar los nombres de las columnas
print("Nombres de las columnas:", df.columns)

# Mostrar los valores únicos en la columna 'raceId'
if 'raceId' in df.columns:
    print("Valores únicos en la columna 'raceId':")
    print(df['raceId'].unique())
else:
    print("La columna 'raceId' no existe en el DataFrame.")

# Mostrar las filas donde la columna 'raceId' tenga valores que no son enteros
if 'raceId' in df.columns:
    print("\nFilas con valores no enteros en 'raceId':")
    print(df[~df['raceId'].apply(lambda x: str(x).isdigit())])


"""
    /*Cargar el archivo CSV
df = pd.read_csv(file_path,encoding='UTF-8')
# Mostrar los valores únicos de la columna PK
print("Valores únicos en la columna PK")
#print(df['circuitId'].unique())
#  print(df['constructorResultsId'].unique())
#print(df['constructorStandingsId'].unique())
#print(df['constructorId'].unique())
#print(df['driverStandingsId'].unique())

#print(df['driverId'].unique())
#print(df['lap'].unique())
#print(df['raceId'].unique())

#print(df['stop'].unique())
#print(df['driverId'].unique())
#print(df['raceId'].unique())


#print(df['qualifyId'].unique())
print(df['raceId'].unique())
#print(df['resultId'].unique())
#print(df['year'].unique())
#print(df['resultId'].unique())
#print(df['StatusId'].unique())


# Mostrar las filas donde la columna circuitId tenga valores que no son enteros
print("\nFilas con valores no enteros en PK:")
#print(df[~df['circuitId'].apply(lambda x: str(x).isdigit())])
#  print(df[~df['constructorResultsId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['constructorStandingsId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['constructorId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['driverStandingsId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['driverId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['lap'].apply(lambda x: str(x).isdigit())])
print(df[~df['raceId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['stop'].apply(lambda x: str(x).isdigit())])
#print(df[~df['driverId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['raceId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['qualifyId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['raceId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['resultId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['year'].apply(lambda x: str(x).isdigit())])
#print(df[~df['resultId'].apply(lambda x: str(x).isdigit())])
#print(df[~df['statusId'].apply(lambda x: str(x).isdigit())])


print(df.columns)
*/
"""