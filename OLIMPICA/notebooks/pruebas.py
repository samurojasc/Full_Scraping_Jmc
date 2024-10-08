import base64
import json

# La cadena Base64 original
cadena_base64_original = 'eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiIxIiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjoiVTFjalpYaHBkRzlqYjJ3N1pYaHBkRzlqYjJ3ME1Eaz0iLCJ1dG1fY2FtcGFpZ24iOm51bGwsInV0bV9zb3VyY2UiOm51bGwsInV0bWlfY2FtcGFpZ24iOm51bGwsImN1cnJlbmN5Q29kZSI6IkNPUCIsImN1cnJlbmN5U3ltYm9sIjoiJCIsImNvdW50cnlDb2RlIjoiQ09MIiwiY3VsdHVyZUluZm8iOiJlcy1DTyIsImFkbWluX2N1bHR1cmVJbmZvIjoiZXMtQ08iLCJjaGFubmVsUHJpdmFjeSI6InB1YmxpYyJ9'
# Decodificar la cadena Base64 para obtener el JSON original
cadena_json_original = base64.b64decode(cadena_base64_original).decode('utf-8')
print('cadena decodificada', cadena_json_original)
# Convertir la cadena JSON original a un objeto
datos_original = json.loads(cadena_json_original)
print('datos original: ', datos_original)
# Volver a codificar el objeto JSON en Base64
# Asegúrate de usar las mismas configuraciones de codificación de caracteres y formateo JSON
cadena_json_nueva = json.dumps(datos_original, separators=(',', ':')).encode('utf-8')
cadena_base64_nueva = base64.b64encode(cadena_json_nueva).decode('utf-8')

# Comparar las dos cadenas Base64
coinciden = cadena_base64_nueva == cadena_base64_original

# Mostrar los resultados
print(f'Cadena Base64 original: {cadena_base64_original}')
print(f'Nueva cadena Base64: {cadena_base64_nueva}')
print(f'¿Coinciden las cadenas? {"Sí" if coinciden else "No"}')


#cadena_json_original = base64.b64decode("eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6dHJ1ZSwic2t1c0ZpbHRlciI6IkFMTF9BVkFJTEFCTEUiLCJzaW11bGF0aW9uQmVoYXZpb3IiOiJkZWZhdWx0IiwiaW5zdGFsbG1lbnRDcml0ZXJpYSI6Ik1BWF9XSVRIT1VUX0lOVEVSRVNUIiwicHJvZHVjdE9yaWdpblZ0ZXgiOmZhbHNlLCJtYXAiOiJjIiwicXVlcnkiOiJ2aW5vcy15LWxpY29yZXMiLCJvcmRlckJ5IjoiT3JkZXJCeVNjb3JlREVTQyIsImZyb20iOjAsInRvIjoxOSwic2VsZWN0ZWRGYWNldHMiOlt7ImtleSI6ImMiLCJ2YWx1ZSI6InZpbm9zLXktbGljb3JlcyJ9XSwiZmFjZXRzQmVoYXZpb3IiOiJTdGF0aWMiLCJjYXRlZ29yeVRyZWVCZWhhdmlvciI6ImRlZmF1bHQiLCJ3aXRoRmFjZXRzIjpmYWxzZSwic2hvd1Nwb25zb3JlZCI6dHJ1ZX0=").decode('utf-8')
#cadena_2 = base64.b64decode("eyJoaWRlVW5hdmFpbGFibGVJdGVtcyI6dHJ1ZSwic2t1c0ZpbHRlciI6IkFMTF9BVkFJTEFCTEUiLCJzaW11bGF0aW9uQmVoYXZpb3IiOiJkZWZhdWx0IiwiaW5zdGFsbG1lbnRDcml0ZXJpYSI6Ik1BWF9XSVRIT1VUX0lOVEVSRVNUIiwicHJvZHVjdE9yaWdpblZ0ZXgiOmZhbHNlLCJtYXAiOiJwcm9kdWN0Q2x1c3RlcklkcyIsInF1ZXJ5Ijoidmlub3MteS1saWNvcmVzIiwib3JkZXJCeSI6Ik9yZGVyQnlTY29yZURFU0MiLCJmcm9tIjowLCJ0byI6MTksInNlbGVjdGVkRmFjZXRzIjpbeyJrZXkiOiJwcm9kdWN0Q2x1c3RlcklkcyIsInZhbHVlIjoidmlub3MteS1saWNvcmVzIn1dLCJmYWNldHNCZWhhdmlvciI6IlN0YXRpYyIsIndpdGhGYWNldHMiOmZhbHNlLCJzaG93U3BvbnNvcmVkIjp0cnVlfQ==").decode('utf-8')
#print('cadena decodificada',cadena_json_original)
#print('cadena 2 decodificada', cadena_2)