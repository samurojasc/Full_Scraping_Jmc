import pandas as pd

# Leer el archivo Excel
archivo_excel = 'carulla2.xlsx'

# Leer todas las hojas del archivo Excel
hojas_excel = pd.read_excel(archivo_excel, sheet_name=None)

# Crear un DataFrame vacío para almacenar los datos de todas las hojas
datos_totales = pd.DataFrame()

# Iterar sobre cada hoja
for nombre_hoja, datos_hoja in hojas_excel.items():
    # Eliminar duplicados en cada hoja
    datos_sin_duplicados = datos_hoja.drop_duplicates()
    # Agregar los datos de la hoja sin duplicados al DataFrame total
    datos_totales = pd.concat([datos_totales, datos_sin_duplicados])

# Resetear los índices después de concatenar todos los datos
datos_totales.reset_index(drop=True, inplace=True)

# Eliminar duplicados en el conjunto total de datos
datos_totales_sin_duplicados = datos_totales.drop_duplicates()

# Guardar los datos sin duplicados en una nueva hoja de Excel
nombre_nueva_hoja = 'Datos_sin_duplicados'
datos_totales_sin_duplicados.to_excel('carulla_sin_duplicados.xlsx', sheet_name=nombre_nueva_hoja, index=False)

print("Datos sin duplicados guardados en la hoja:", nombre_nueva_hoja)

