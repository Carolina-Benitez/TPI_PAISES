#Desarrollar una aplicación que permita gestionar información sobre países,
#aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas. 
#El sistema debe ser capaz de leer datos desde un archivo CSV,
#realizar consultas y generar indicadores clave a partir del dataset. 

#DOMINIO (dataset de países)
#Cada país estará representado con los siguientes datos:

#• Nombre (string)
#• Población (int)
#• Superficie en km² (int)
#• Continente (string)

#Ejemplo de REGISTRO CSV:

#nombre,poblacion,superficie,continente:

#Argentina,45376763,2780400,América
#Japón,125800000,377975,Asia
#Brasil,213993437,8515767,América
#Alemania,83149300,357022,Europa 

#El programa debe ofrecer un MENU DE OPCIONES en consola que permita:

#• Agregar un país con todos los datos necesarios para almacenarse (No se permiten campos vacios).
#• Actualizar los datos de Población y Superfice de un Pais.
#• Buscar un país por nombre (coincidencia parcial o exacta).

#• FILTRAR PAISES POR:
# Continente
# Rango de población
# Rango de superficie

#• ORDENAR PAISES POR:
# Nombre
# Población
# Superficie (ascendente o descendente)

#• MOSTRAR ESTADISTICAS:
# País con mayor y menor población
# Promedio de población
# Promedio de superficie
# Cantidad de países por continente

#3. VALIDACIONES
#• Controlar errores de formato en el CSV.
#• Evitar fallos al ingresar filtros inválidos o búsquedas sin resultados.
#• Mensajes claros de éxito/error. 


import os #verifica si el arhivo existe antes de intentar leerlo

def cargar_datos(nombre_archivo):
    paises= [] 
    if os.path.exists(nombre_archivo): #Si el archivo existe: lo abrimos y lo cargamos. Sino, lista vacia
        with open(nombre_archivo, "r", encoding="utf-8") as archivo: #lo abrimos en modo lectura
            encabezado= archivo.readline() #salta la primera línea (encabezado: NOMBRE, POBLACION, SUPERFICIE, CONTINENTE) y la descarta porque no es dato de un pais
            for linea in archivo: #recorre cada linea de paises
                partes = linea.strip().split(",") #separa cada linea con coma
                if len(partes) == 4:
                    nombre = partes[0] #primera parte: el nombre del pais
                    poblacion_str = (partes[1]) #segunda parte: la poblacion (convertida a numero)
                    superficie_str = (partes[2]) #tercera parte: la superficie
                    continente = partes[3] #cuarta parte: el continente 
                    #verificamos que los valores sean numeros validos
                    if poblacion_str.isdigit() and superficie_str.isdigit():
                        poblacion = int(poblacion_str) 
                        superficie = int(superficie_str)
                        paises.append({"NOMBRE": nombre, "POBLACION": poblacion, "SUPERFICIE": superficie, "CONTINENTE": continente}) #agrega el diccionario a la lista paises
    return paises #muestra la lista

# Guardar los paises en el archivo CSV

def guardar_datos(nombre_archivo, paises): #función que recibe dónde guardar y la lista de países
    with open(nombre_archivo, "w", encoding="utf-8") as archivo: #abrimos en modo escritura (si existe lo sobreescribe)
        archivo.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n") #escribe la primera linea (encabezado del CSV)
        for pais in paises: #recorremos la lista 
            #construimos formato CSV
            linea = pais["NOMBRE"] + "," + str(pais["POBLACION"]) + "," + str(pais["SUPERFICIE"]) + "," + pais["CONTINENTE"] + "\n"
            archivo.write(linea)

#FUNCIONES PRINCIPALES DEL MENU

#opcion 1 
def agregar_pais(paises): 
    print("\nAGREGAR PAÍS")
    nombre = input("Nombre del pais a agregar: ")
    #VALIDACIONES
    if nombre == "":
        print("No se permiten campos vacios")
        return paises
    if nombre.isdigit():
        print("No se ingresan numeros")
        return paises
    for pais in paises:
        if pais["NOMBRE"].lower() == nombre.lower(): 
            print("Ese pais ya existe")
            return paises
        
    poblacion = input("Población: ")
    #VALIDACIONES
    if poblacion == "":
        print("No se permiten campos vacíos.")
        return paises
    if not poblacion.isdigit():
        print("Población debe ser un número entero válido.")
        return paises

    superficie = input("Superficie: ")
    #VALIDACIONES
    if superficie == "":
        print("No se permiten campos vacíos.")
        return paises
    if not superficie.isdigit():
        print("Superficie debe ser un número entero válido.")
        return paises

    continente = input("Continente (américa, asia, áfrica, europa): ")
    #VALIDACIONES
    if continente == "":
        print("No se permiten campos vacíos.")
        return paises
    if continente.isdigit():
        print("No se ingresan numeros")
        return paises

    #agregar pais (nuevo diccionario a la lista paises)
    pais_agregado= {"NOMBRE": nombre,"POBLACION": int(poblacion), "SUPERFICIE": int(superficie), "CONTINENTE": continente}
    paises.append(pais_agregado)
    print(f"País '{nombre}' agregado correctamente.")
    return paises

#opcion 2
def actualizar_poblacion(paises):
    print("\nACTUALIZAR POBLACIÓN")
    nombre = input("Nombre del país a actualizar: ")
    #VALIDACIONES
    if nombre == "":
        print("No se permiten campos vacíos.")
        return paises

    for pais in paises:
        if pais["NOMBRE"].lower() == nombre.lower():
            nueva_poblacion = input("Nueva población del pais: ")
            #VALIDACIONES
            if nueva_poblacion == "":
                print("No se permiten campos vacíos.")
                return paises
            if not nueva_poblacion.isdigit():
                print("Debe ser un número entero válido.")
                return paises
            pais["POBLACION"] = int(nueva_poblacion)
            print("Población actualizada.")
            return paises

    print("País no encontrado.")
    return paises

#opcion 3
def actualizar_superficie(paises):
    print("\nACTUALIZAR SUPERFICIE")
    nombre = input("Nombre del país a actualizar: ")
    #VALIDACIONES
    if nombre == "":
        print("No se permiten campos vacíos.")
        return paises

    for pais in paises:
        if pais["NOMBRE"].lower() == nombre.lower():
            nueva_superficie = input("Nueva superficie: ")
            if nueva_superficie == "":
                print("No se permiten campos vacíos.")
                return paises
            if not nueva_superficie.isdigit():
                print("Debe ser un número entero válido.")
                return paises
            pais["SUPERFICIE"] = int(nueva_superficie)
            print("Superficie actualizada.")
            return paises

    print("País no encontrado.")
    return paises

#opcion 4
def buscar_pais(paises):
    print("\nBUSCAR PAÍS")
    pais_buscado = input("Ingresa el nombre del pais: ").lower()

    #verificar que no este vacio
    if pais_buscado== "":
        print("\nPais buscado vacio")
        return
    

    #lista vacia para guardar el paises encontrado
    encontrado= []

    #recorremos todos los paises
    for pais in paises:
        if pais_buscado in pais["NOMBRE"].lower(): #si el pais buscado esta dentro de la lista
            encontrado.append(pais) #lo agregamos a la lista de encontrado

    #Si encontramos un pais, mostramos cual y sus datos
    if len(encontrado) > 0:
        print("\npais encontrado:")
        for pais in encontrado:
            print(f"{pais['NOMBRE']} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} | Continente: {pais['CONTINENTE']}")
    else:
        print("No se encontró el país.")
    return

#opcion 5

def listar_paises(paises):
    print("\nLISTAR PAÍSES")
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    for pais in paises:
        print(f"{pais['NOMBRE']} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} | Continente: {pais['CONTINENTE']}")

#opcion 6

def eliminar_pais(paises):
    print("\nELIMINAR PAÍS")
    nombre = input("Nombre del país a eliminar: ").strip()
    if nombre == "":
        print("No se permiten campos vacíos.")
        return paises

    for pais in paises:
        if pais["NOMBRE"].lower() == nombre.lower():
            paises.remove(pais)
            print(f"País '{nombre}' eliminado correctamente.")
            return paises

    print("País no encontrado.")
    return paises

#opcion 7
def filtrar_paises(paises):
    print("\nFILTRAR PAÍSES")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")

    opcion_str = input("Elegí una opción (1-3): ")
    if opcion_str == "":
        print("Opción vacía.")
        return
    if not opcion_str.isdigit():
        print("Solo se permiten números (1, 2 o 3).")
        return

    tipo_filtro = int(opcion_str)
    if tipo_filtro < 1 or tipo_filtro > 3:
        print("Opción fuera de rango (1 a 3).")
        return

    #lista donde guardamos los paises filtrados
    filtrados= []

    #FILTRO POR CONTINENTE

    if tipo_filtro == 1:
        continent = input("\nIngresa un continente: ").lower()
        if continent =="":
            print("Continente vacio.")
            return
        #recorremos los paises
        for pais in paises:
            if continent in pais["CONTINENTE"].lower():
                filtrados.append(pais)

    #POR RANGO DE POBLACION            

    elif tipo_filtro == 2:
        minima_poblacion = input("Población mínima: ")
        if minima_poblacion == "":
            print("No se permiten campos vacios")
            return
        maxima_poblacion = input("Población máxima: ")
        if maxima_poblacion == "":
            print("No se permiten campos vacios")
            return

        if not (minima_poblacion.isdigit() and maxima_poblacion.isdigit()):
            print("Debés ingresar solo números.")
            return

        min_pobl = int(minima_poblacion)
        max_pobl = int(maxima_poblacion)

        if min_pobl > max_pobl:
            print("El mínimo no puede ser mayor que el máximo.")
            return

        for pais in paises:
            if pais["POBLACION"] >= min_pobl and pais["POBLACION"] <= max_pobl:
                filtrados.append(pais)

    #POR RANGO DE SUPERFICIE

    elif tipo_filtro == 3:
        minima_superficie = input("Superficie mínima: ")
        if minima_superficie == "":
            print("No se permiten campos vacios")
            return
        maxima_superficie = input("Superficie máxima: ")
        if maxima_superficie == "":
            print("No se permiten campos vacios")

        if not (minima_superficie.isdigit() and maxima_superficie.isdigit()):
            print("Debés ingresar solo números.")
            return

        min_sup = int(minima_superficie)
        max_sup = int(maxima_superficie)

        if min_sup > max_sup:
            print("El mínimo no puede ser mayor que el máximo.")
            return

        for pais in paises:
            if pais["SUPERFICIE"] >= min_sup and pais["SUPERFICIE"] <= max_sup:
                filtrados.append(pais)

    #MOSTRAR RESULTADOS
    if len(filtrados) > 0: #si encontramos paises filtrados
        print("\nResultados del filtro:\n")
        for pais in filtrados:
            print(f"{pais['NOMBRE']} | {pais['POBLACION']} habitantes. | {pais['SUPERFICIE']} km² | {pais['CONTINENTE']}")
    else:
        print("No se encontraron países con esos datos.")

#opcion 8
def ordenar_paises(paises):
    print("\nORDENAR PAÍSES")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    opcion_orden = input("Elegí una opción: ")

    #verificar que no este vacio
    if opcion_orden == "":
        print("Opcion vacia")
        return paises
    
    
    #verificar que sea un numero entero valido
    if not opcion_orden.isdigit():
        print("\nIngresa un numero entero valido")
        return paises

    #verificar rango correcto de opciones
    opcion = int(opcion_orden)
    if opcion < 1 or opcion > 3:
        print("Opcion invalida. Las opciones son del 1 al 3.")
        return paises

    orden = input("¿Ascendente (A) o descendente (D)?: ").upper()
    if orden not in ["A", "D"]:
        print("Debe ingresar A o D.")
        return paises

    cantidad= len(paises)
    if cantidad <= 1:
        print("No hay suficientes países para ordenar.")
        return paises

    if opcion == 1: #ORDENAR POR NOMBRE
        for i in range(cantidad - 1):
            for j in range(cantidad - i - 1):
                nombre1 = paises[j]["NOMBRE"].lower()
                nombre2 = paises[j + 1]["NOMBRE"].lower()
                if (orden == "A" and nombre1 > nombre2) or (orden == "D" and nombre1 < nombre2):
                    temp = paises[j]
                    paises[j] = paises[j + 1]
                    paises[j + 1] = temp

    elif opcion == 2: # ORDENAR POR POBLACIÓN
        for i in range(cantidad - 1): 
            for j in range(cantidad - i - 1):
                p1 = paises[j]["POBLACION"]
                p2 = paises[j + 1]["POBLACION"]
                if (orden == "A" and p1 > p2) or (orden == "D" and p1 < p2):
                    temp = paises[j]
                    paises[j] = paises[j + 1]
                    paises[j + 1] = temp

    elif opcion == 3:  # ORDENAR POR SUPERFICIE
        for i in range(cantidad - 1):
            for j in range(cantidad - i - 1):
                s1 = paises[j]["SUPERFICIE"]
                s2 = paises[j + 1]["SUPERFICIE"]
                if (orden == "A" and s1 > s2) or (orden == "D" and s1 < s2):
                    temp = paises[j]
                    paises[j] = paises[j + 1]
                    paises[j + 1] = temp

    else:
        print("Opción inválida.")
        return paises

    print("\nPaíses ordenados correctamente.")
    for pais in paises:
        print(pais["NOMBRE"], "| Población:", pais["POBLACION"], "| Superficie:", pais["SUPERFICIE"], "| Continente:", pais["CONTINENTE"])
    return paises


#opcion 9
def mostrar_estadisticas(paises):
    print("\nESTADÍSTICAS")
    if len(paises)==0:
        print("No hay datos cargados.")
        return

    #pais con mayor y menor poblacion
    mayor = paises[0]
    menor = paises[0]

    for pais in paises:
        if pais["POBLACION"] > mayor["POBLACION"]:
            mayor = pais
        if pais["POBLACION"] < menor["POBLACION"]:
            menor = pais

    suma_pob = 0
    suma_sup = 0
    for pais in paises:
        suma_pob += pais["POBLACION"]
        suma_sup += pais["SUPERFICIE"]

    promedio_pob = suma_pob / len(paises)
    promedio_sup = suma_sup / len(paises)

    # cantidad por continente
    continentes = {}
    for pais in paises:
        c = pais["CONTINENTE"]
        if c in continentes:
            continentes[c] += 1
        else:
            continentes[c] = 1

    print("País con mayor población:", mayor["NOMBRE"], "(", mayor["POBLACION"], ")")
    print("País con menor población:", menor["NOMBRE"], "(", menor["POBLACION"], ")")
    print("Promedio de población:", round(promedio_pob, 2))
    print("Promedio de superficie:", round(promedio_sup, 2))
    print("Cantidad de países por continente:")
    for c in continentes:
        print(" -", c + ":", continentes[c])
    return

#MENU PRINCIPAL

def menu():
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(ruta_actual, "paises.csv")
    paises = cargar_datos(archivo)

    while True:
        print("\nMENU\n")
        print("1. Agregar pais")
        print("2. Actualizar poblacion")
        print("3. Actualizar superficie")
        print("4. Buscar pais")
        print("5. Listar países")
        print("6. Eliminar país")
        print("7. Filtrar países")
        print("8. Ordenar países")
        print("9. Mostrar estadísticas")
        print("10. Salir")

        opcion_str= input("Elegi una opcion: ")

        #verificar que no este vacio
        if opcion_str == "":
            print("No se permiten campos vacios.")
            continue

        #verificar que solo sean numeros
        if not opcion_str.isdigit():
            print("debe ingresar un numero del 1 al 8.")
            continue

        opcion= int(opcion_str)

        if opcion == 1:
            paises = agregar_pais(paises)
        elif opcion == 2:
            paises = actualizar_poblacion(paises)
        elif opcion == 3:
            paises = actualizar_superficie(paises)
        elif opcion == 4:
            buscar_pais(paises)
        elif opcion == 5:
            listar_paises(paises)
        elif opcion == 6:
            paises = eliminar_pais(paises)
        elif opcion == 7:
            filtrar_paises(paises)
        elif opcion == 8:
            paises = ordenar_paises(paises)
        elif opcion == 9:
            mostrar_estadisticas(paises)
        elif opcion == 10:
            guardar_datos(archivo, paises)
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Ingrese las opciones del 1 al 10")

# EJECUCIÓN
menu()









