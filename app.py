import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns

# Ejercicio 00
# this CSV file contains semicolons instead of comas as separator
ds = pd.read_csv('assets/real_estate.csv', sep=';')



# Ejercicio 01



# valor_max = ds["price"].max()
# ds = ds[ds["price"] == valor_max]

# direccion = ds["address"].values[0]


# print(valor_max)
# print(direccion)

# Ejercicio 02

# valor_min = ds["price"].min()
# ds = ds[ds["price"] == valor_min]

# direccion = ds["address"].values[0]


# print(valor_min)
# print(direccion)

# Ejercicio 03

# sup_min = ds["surface"].min()
# ds = ds[ds["surface"] == sup_min]

# direccion = ds["address"].values[0]


# print(sup_min)
# print(direccion)

# sup_max = ds["surface"].max()
# ds = ds[ds["surface"] == sup_max]

# direccion = ds["address"].values[0]


# print(sup_max)
# print(direccion)

# Ejercicio 04

# num_poblaciones = ds["level5"].unique().shape[0]

# nombres_poblaciones = ds["level5"].unique().tolist()


# print(f"Número de poblaciones: {num_poblaciones}")
# print(", ".join(nombres_poblaciones))

# Ejercicio 05

# val_nulos= ds.isnull().sum()


# print(val_nulos)


# Iterar por las filas
# for i in range(ds.shape[0]):
#   # Verificar si hay valores NA en la fila
#   if ds.iloc[i,:].isnull().any():
#     # Imprimir True y la fila
#     print(True, i)

# # # Iterar por las columnas
# for i in range(ds.shape[1]):
#   # Verificar si hay valores NA en la columna
#   if ds.iloc[:,i].isnull().any():
#     # Imprimir True y la columna
#     print(True, ds.columns[i])

# Ejercicio 06

# dim_dataset= ds.shape
# print(dim_dataset)

# Ejercicio 07

# Seleccionar la columna 
# precios = ds["price"]

# # Calcular la media de los precios
# precio_medio=precios.mean()

# print(precio_medio)

# # Filtrar la población por ubicación
# precios_region = precios[ds["level5"] == "Arroyomolinos (Madrid)"]

# # Calcular la media de precios para la región
# precio_medio_region = precios_region.mean()

# # Seleccionar el precio medio
# precio_medio_seleccionado = precio_medio_region

# # Imprimir el precio medio seleccionado
# print(precio_medio_seleccionado)

# Ejercicio 08

# # Seleccionar la columna de precios y la columna de ubicación
# precios = ds["price"]
# ubicacion = ds["level5"]

# # # Filtrar el dataset por ubicación
# precios_region = precios[ds["level5"] == "Arroyomolinos (Madrid)"]

# # # # Calcular la frecuencia de precios
# frecuencia_precios = precios_region.hist(bins=100)

# # # # Mostrar el histograma
# # plt.show()

# # print(precios_region)



# plt.title("Histograma - Precios Arroyo Molinos")

# plt.show()
# plt.xlabel("precio")
# plt.savefig("histograma.png")
# El precio medio en la region Arroyo Molinos es de 30.000, y los valores extremos oscilan entre 0 y 60000

# Ejercicio 09

# # Seleccionar la columna 
# precios = ds["price"]

# # Calcular la media de los precios
# precio_medio=precios.mean()

# print(precio_medio)

# # Filtrar la población por ubicación
# precios_region = precios[ds["level5"] == "Valdemorillo"]
# precios_region_2 = precios[ds["level5"] == "Galapagar"]

# # Calcular la media de precios para la región
# precio_medio_region = precios_region.mean()
# precio_medio_region_2 = precios_region_2.mean()

# # Seleccionar el precio medio
# precio_medio_seleccionado = precio_medio_region
# precio_medio_seleccionado_2 = precio_medio_region_2

# # Imprimir el precio medio seleccionado
# print(precio_medio_seleccionado)
# print(precio_medio_seleccionado_2)

# Son precios muy similares pero no son exactamente iguales

# Ejercicio 10

# # Añadir una nueva columna a partir de una función
# ds["pps"] = ds["price"] / ds["surface"]

# # Guardar el dataset con la nueva columna
# ds.to_csv('assets/real_estate_nueva_col.csv', sep=';')

# # Seleccionar la columna 
# precio_por_metro_cuadradp = ds["pps"]

# # Filtrar la población por ubicación
# precios_region = precio_por_metro_cuadradp[ds["level5"] == "Valdemorillo"]
# precios_region_2 =precio_por_metro_cuadradp[ds["level5"] == "Galapagar"]

# # Calcular la media de precios para la región
# precio_medio_region = precios_region.mean()
# precio_medio_region_2 = precios_region_2.mean()

# # Seleccionar el precio medio
# precio_medio_seleccionado = precio_medio_region
# precio_medio_seleccionado_2 = precio_medio_region_2

# # Imprimir el precio medio seleccionado
# print(precio_medio_seleccionado)
# print(precio_medio_seleccionado_2)

# # Los precios de Galapagar son mas altos que los de Valdemorillo

# Ejercicio 11

# # Seleccionar las columnas
# x = ds["price"]
# y = ds["surface"]

# # Crear el diagrama de dispersión
# plt.figure(figsize=(10,5), facecolor="red")
# plt.scatter(x, y)

# # Agregar un título
# plt.title("Diagrama de dispersión")

# # Agregar etiquetas a los ejes
# plt.xlabel("price")
# plt.ylabel("surface")

# # Mostrar el diagrama
# plt.show()
# plt.savefig("histograma.png")

# Ejercicio 12

# num_bienes_raices = ds["realEstate_name"].unique().shape[0]

# print(f"Número de agencia de bienes raices: {num_bienes_raices}")

# Ejercicio 13

# # Contar la cantidad de veces que se repiten los datos en la columna "Columna"
# frecuencias = ds["level5"].value_counts()

# # Mostrar las frecuencias
# print(frecuencias)

# # Madrid es la region que mas cantidad de casas tiene

# Ejercicio 14

# # Poblaciones a incluir
# poblaciones = ["Fuenlabrada", "Leganés", "Getafe","Alcorcón"]

# # # Leer el dataframe original
# # df_original = pd.read_csv("data.csv")

# # Filtrar el dataframe por las poblaciones
# ds_filtrado = ds[ds["level5"].isin(poblaciones)]

# # Mostrar el dataframe filtrado
# print(ds_filtrado)

# Ejercicio 15

# # Seleccionar la variable para el eje X
# x = ds_filtrado["level5"]

# # Seleccionar la variable para el eje Y
# y = ds_filtrado["price"]

# # Crear el diagrama de barras
# plt.bar(x, y)

# # Agregar un título
# plt.title("Diagrama de barras")

# # Agregar etiquetas a los ejes
# plt.xlabel("Poblacion")
# plt.ylabel("Precio")

# # Mostrar el diagrama
# plt.show()
# plt.savefig("diagrama_barras.png")

# Ejercicio 16

# # Seleccionar las columnas de interés
# columnas = ["price", "surface", "rooms", "bathrooms"]

# # Calcular la media y la varianza de las columnas
# for columna in columnas:
#     media = ds[columna].mean()
#     varianza = ds[columna].var()
#     print(f"Columna: {columna}")
#     print(f"Media: {media}")
#     print(f"Varianza: {varianza}")

# Ejercicio 17

# # Filtrar el dataset para obtener el subconjunto deseado
# subconjunto = ds.loc[ds["level5"] == "Fuenlabrada"]

# # Agrupar el subconjunto por la variable "Tipo"
# grupos = subconjunto.groupby("Fuenlabrada")

# # Calcular el precio máximo de cada grupo
# precios_maximos = grupos["price"].max()

# # Filtrar por la fila con el precio máximo
# casas_mas_caras = grupos.loc[grupos["price"] == precios_maximos]

# # Mostrar los resultados
# for casa in casas_mas_caras:
#     print(f"Tipo: {casa['Tipo']}")
#     print(f"Precio: {casa['Precio']}")

# # # # Poblaciones a incluir
# poblaciones = ["Fuenlabrada", "Leganés", "Getafe","Alcorcón"]


# # # # # Filtrar el dataframe por las poblaciones
# # # ds_filtrado = ds[ds["level5"].isin(poblaciones)]

# # # # Agrupar el dataset por la variable "Poblacion"
# poblaciones = ds[ds["level5"].isin(poblaciones)]

# # # Calcular el precio máximo de cada grupo
# precios_maximos = poblaciones["price"].max()

# print(precios_maximos)

# # # Filtrar por la fila con el precio máximo
# casas_mas_caras = poblaciones.loc[poblaciones["price"] == precios_maximos]

# print(casas_mas_caras)

# # # Mostrar los resultados
# for casa in casas_mas_caras:
#     # print(f"poblaciones: {casa['level5']}")
#     print(f"Precio: {casa['price']}")

# Ejercicio 18

# # # Filtrar el dataset para obtener el subconjunto deseado
# # subconjunto = ds.loc[ds["level5"] == "Fuenlabrada", "Leganés", "Getafe","Alcorcón"]
# # print(subconjunto)
# # Filtrar el subconjunto para obtener la población deseada
# # poblacion = subconjunto.loc[subconjunto["Poblacion"] == "Panama City"]

# poblaciones = ["Fuenlabrada", "Leganés", "Getafe","Alcorcón"]
# ds_filtrado = ds[ds["level5"].isin(poblaciones)]
# # print(ds_filtrado)

# # # Función para normalizar por rango
# # def normalizar_rango(price):
# #     minimo = price.min()
# #     maximo = price.max()
# #     return (price - minimo) / (maximo - minimo)

# # # Calcular el valor normalizado
# # precio_normalizado = normalizar_rango(ds["price"])

# # # Crear una nueva columna
# # df["Precio_Normalizado"] = precio_normalizado

# # # Mostrar el DataFrame
# # print(df)

# # # Calcular el valor mínimo y máximo de la variable "Precio"
# precio_min = ds_filtrado["price"].min()
# precio_max = ds_filtrado["price"].max()
# # print(precio_max)
# # print(precio_min)

# # # Normalizar la variable "Precio"
# precio_normalizado = (ds_filtrado["price"] - precio_min) / (precio_max - precio_min)
# ds_filtrado["Precio_Normalizado"] = precio_normalizado
# # print(ds_filtrado)
# # print(precio_normalizado)

# # # Plotear el histograma de la variable normalizada

# # plt.hist(precio_normalizado)
# # plt.xlabel("Valor")
# # plt.ylabel("Frecuencia")
# # plt.title("Histograma de la columna Precio")
# # plt.show()
# # plt.savefig("histograma.png")

# sns.jointplot(data=ds_filtrado, x="level5", y="precio_normalizado")
# plt.show()
# plt.savefig("histograma.png")
# ds_filtrado["Precio_Normalizado"].hist()
# plt.show()

# Ejercicio 19

# Añadir una nueva columna a partir de una función
# ds["pps"] = ds["price"] / ds["surface"]

# # Guardar el dataset con la nueva columna
# ds.to_csv('assets/real_estate_nueva_col.csv', sep=';')

# # Seleccionar la columna 
# precio_por_metro_cuadradp = ds["pps"]

# # Filtrar la población por ubicación
# precios_region = precio_por_metro_cuadradp[ds["level5"] == "Getafe"]
# precios_region_2 =precio_por_metro_cuadradp[ds["level5"] == "Alcorcón"]
# precios_region_3 =precio_por_metro_cuadradp[ds["level5"] == "Fuenlabrada"]
# precios_region_4 =precio_por_metro_cuadradp[ds["level5"] == "Leganés"]


# # Calcular la media de precios para la región
# precio_medio_region = precios_region.mean()
# precio_medio_region_2 = precios_region_2.mean()
# precio_medio_region_3 = precios_region_3.mean()
# precio_medio_region_4 = precios_region_4.mean()

# # Seleccionar el precio medio
# precio_medio_seleccionado = precio_medio_region
# precio_medio_seleccionado_2 = precio_medio_region_2
# precio_medio_seleccionado_3 = precio_medio_region_3
# precio_medio_seleccionado_4= precio_medio_region_4

# # Imprimir el precio medio seleccionado
# print(precio_medio_seleccionado)
# print(precio_medio_seleccionado_2)
# print(precio_medio_seleccionado_3)
# print(precio_medio_seleccionado_4)

# Los precios de Galapagar son mas altos que los de Valdemorillo

# Ejercicio 20
# Crear un histograma con 4 subplots
plt.subplot(121)
plt.hist(ds["price"])
plt.title("data1")

plt.subplot(122)
plt.hist(ds["price"])
plt.title("data2")

plt.show()
plt.savefig("histograma.png")
