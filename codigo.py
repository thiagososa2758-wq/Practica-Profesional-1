import pandas as pd

# Cargar el dataframe desde el archivo de Excel real disponible en el entorno
df = pd.read_excel("eph_tecnologia_microdatos.csv.xlsx")

# Calcular métricas para el ingreso total familiar (ITF)
promedio = df["ITF"].mean()
print("El promedio del ingreso familiar es de:", promedio)

mediana = df["ITF"].median()
print("La mediana del ingreso familiar es de:", mediana)

maximo = df["ITF"].max()
print("El máximo del ingreso familiar es de:", maximo)

minimo = df["ITF"].min()
print("El mínimo del ingreso familiar es de:", minimo)

desviacion = df["ITF"].std()
print("El desvío estándar del ingreso familiar es de:", desviacion)

# Resumen completo con todas las estadísticas
resumen = df["ITF"].describe()
print("\nResumen completo:")
print(resumen)
