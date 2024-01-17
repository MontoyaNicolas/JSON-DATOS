import pandas as pd
import json

# Cargar el archivo de Excel
excel_file_path = 'D:/DATOS PROYECTADOS/datosjson.xlsx'  # Asegúrate de que la ruta y el nombre del archivo sean correctos

# Leer el archivo Excel
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')  # Cambia 'Sheet1' si tu hoja tiene otro nombre

# Convertir la columna de geometría a objetos JSON válidos
df['geometry'] = df['geometria'].apply(lambda x: {"type": "Polygon", "coordinates": [json.loads(x.replace("'", "\""))]})

# Crear un nuevo DataFrame para el JSON con las columnas necesarias
json_df = df[['hex_id', 'latitud', 'longitud', 'geometry']]

# Convertir el DataFrame a JSON
json_result = json_df.to_json(orient='records')

# Guardar el JSON en un archivo
json_file_path = 'D:/DATOS PROYECTADOS/archivo.json'  # Cambia el nombre del archivo si es necesario
with open(json_file_path, 'w', encoding='utf-8') as file:
    file.write(json_result)

print(f'Archivo JSON guardado en: {json_file_path}')

