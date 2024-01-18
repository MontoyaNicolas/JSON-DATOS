import pandas as pd
import json

# Cargar el archivo de Excel
excel_file_path = 'D:/DATOS PROYECTADOS/datosgeometia.xlsx'

# Leer el archivo Excel
df = pd.read_excel(excel_file_path)

# Convertir los strings de la columna 'geometria' a listas de Python usando json.loads
df['geometry'] = df['geometria'].apply(lambda x: json.loads(x))

# Crear las features GeoJSON
features = []
for _, row in df.iterrows():
    feature = {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "Polygon",
            "coordinates": row['geometry']
        },
        
    }
    features.append(feature)

# Crear el objeto GeoJSON completo
geojson = {
    "type": "FeatureCollection",
    "features": features
}

# Convertir el objeto GeoJSON a una cadena de texto JSON
geojson_str = json.dumps(geojson, indent=2, ensure_ascii=False)

# Guardar el JSON en un archivo GeoJSON
json_file_path = 'D:/DATOS PROYECTADOS/datos_geometricos_completos.geojson'
with open(json_file_path, 'w', encoding='utf-8') as file:
    file.write(geojson_str)

print('Archivo GeoJSON guardado en:', json_file_path)
