import os  # verifica si el archivo existe antes de intentar leerlo

CONTINENTES_VALIDOS = {
    "américa", "america", "europa", "asia", "áfrica", "africa", "oceania", "antártida", "antartida"
}

def normalizar_continente(c):
    #Devuelve el nombre del continente capitalizado y con tildes coherentes.
    #Acepta variantes con/sin tilde y similares para evitar rechazos por acento.
    c = (c or "").strip().lower()
    mapa = {
        "america": "América", "américa": "América",
        "europa": "Europa",
        "asia": "Asia",
        "africa": "África", "áfrica": "África",
        "oceania": "Oceanía", "oceanía": "Oceanía",
        "antartida": "Antártida", "antártida": "Antártida",
    }
    return mapa.get(c, c.title())


def es_entero_positivo(s):
    """True si s representa un entero >= 0."""
    return s.isdigit() and int(s) >= 0

# CARGA DE DATOS 


def cargar_datos(nombre_archivo):
    paises = []
    if os.path.exists(nombre_archivo):  # Si el archivo existe: lo abrimos y lo cargamos. Sino, lista vacía
        with open(nombre_archivo, "r", encoding="utf-8-sig") as archivo:  # lo abrimos en modo lectura
            encabezado = archivo.readline()  # salta la primera línea (encabezado)
            linea_nro = 1
            for linea in archivo:  # recorre cada línea de países
                linea_nro += 1
                partes = linea.strip().split(",")  # separa cada línea por coma
                if len(partes) == 4:
                    nombre = partes[0].strip()  # primera parte: el nombre del país
                    poblacion_str = partes[1].strip()  # segunda parte: la población (string)
                    superficie_str = partes[2].strip()  # tercera parte: la superficie (string)
                    continente = partes[3].strip()  # cuarta parte: el continente

                    # verificamos que los valores sean números válidos
                    if es_entero_positivo(poblacion_str) and es_entero_positivo(superficie_str):
                        poblacion = int(poblacion_str)
                        superficie = int(superficie_str)
                        continente_norm = normalizar_continente(continente)
                        paises.append({
                            "NOMBRE": nombre,
                            "POBLACION": poblacion,
                            "SUPERFICIE": superficie,
                            "CONTINENTE": continente_norm or continente
                        })  # agrega el diccionario a la lista paises
                    else:
                        # aviso no bloqueante si hay números inválidos en una fila
                        print(f"Aviso: línea {linea_nro} con números inválidos. Se omite.")
                else:
                    # aviso no bloqueante si hay columnas de más/menos
                    print(f"Aviso: línea {linea_nro} con formato inválido (se esperan 4 columnas). Se omite.")
    return paises  # muestra la lista


# Guardar los países en el archivo CSV 

def guardar_datos(nombre_archivo, paises):  # función que recibe dónde guardar y la lista de países
    with open(nombre_archivo, "w", encoding="utf-8", newline="") as archivo:  # abrimos en modo escritura
        archivo.write("NOMBRE,POBLACION,SUPERFICIE,CONTINENTE\n")  # escribe la primera línea (encabezado del CSV)
        for pais in paises:  # recorremos la lista
            # construimos formato CSV
            linea = (
                pais["NOMBRE"]
                + "," + str(pais["POBLACION"])
                + "," + str(pais["SUPERFICIE"])
                + "," + pais["CONTINENTE"]
                + "\n"
            )
            archivo.write(linea)


# FUNCIONES PRINCIPALES DEL MENÚ

# opcion 1 

def agregar_pais(paises):
    print("\nAGREGAR PAÍS")
    nombre = input("Nombre del pais a agregar: ").strip()
    # VALIDACIONES
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

    poblacion = input("Población: ").strip()
    # VALIDACIONES
    if not es_entero_positivo(poblacion):
        print("Población debe ser un número entero válido (>= 0).")
        return paises

    superficie = input("Superficie: ").strip()
    # VALIDACIONES
    if not es_entero_positivo(superficie):
        print("Superficie debe ser un número entero válido (>= 0).")
        return paises

    continente = input("Continente (américa, asia, áfrica, europa, oceania, antártida): ").strip()
    # VALIDACIONES
    if continente == "":
        print("No se permiten campos vacíos.")
        return paises
    if continente.isdigit():
        print("No se ingresan numeros")
        return paises
    if continente.lower() not in CONTINENTES_VALIDOS:
        print("Continente no reconocido. Intenta: América/Europa/Asia/África/Oceanía/Antártida.")
        return paises

    continente = normalizar_continente(continente)

    # agregar pais (nuevo diccionario a la lista paises)
    pais_agregado = {
        "NOMBRE": nombre,
        "POBLACION": int(poblacion),
        "SUPERFICIE": int(superficie),
        "CONTINENTE": continente
    }
    paises.append(pais_agregado)
    print(f"País '{nombre}' agregado correctamente.")
    return paises


# opcion 2 

def actualizar_poblacion_y_superficie(paises):
    print("\nACTUALIZAR POBLACIÓN/SUPERFICIE")
    nombre = input("Nombre del país a actualizar: ").strip()
    # VALIDACIONES
    if nombre == "":
        print("No se permiten campos vacíos.")
        return paises

    for pais in paises:
        if pais["NOMBRE"].lower() == nombre.lower():
            nueva_poblacion = input("Nueva población (Enter para dejar igual): ").strip()
            if nueva_poblacion:
                if not es_entero_positivo(nueva_poblacion):
                    print("Debe ser un número entero válido (>= 0).")
                    return paises
                pais["POBLACION"] = int(nueva_poblacion)

            nueva_superficie = input("Nueva superficie (Enter para dejar igual): ").strip()
            if nueva_superficie:
                if not es_entero_positivo(nueva_superficie):
                    print("Debe ser un número entero válido (>= 0).")
                    return paises
                pais["SUPERFICIE"] = int(nueva_superficie)

            print("Datos actualizados.")
            return paises

    print("País no encontrado.")
    return paises


# opcion 3 

def buscar_pais(paises):
    print("\nBUSCAR PAÍS")
    pais_buscado = input("Ingresa el nombre del pais: ").strip().lower()

    # verificar que no este vacio
    if pais_buscado == "":
        print("\nPais buscado vacío")
        return

    # lista vacía para guardar el/los países encontrados
    encontrado = []

    # recorremos todos los países
    for pais in paises:
        if pais_buscado in pais["NOMBRE"].lower():  # coincidencia parcial
            encontrado.append(pais)

    # Si encontramos, mostramos cuales y sus datos
    if len(encontrado) > 0:
        print("\nPaís(es) encontrado(s):")
        for pais in encontrado:
            print(f"{pais['NOMBRE']} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} | Continente: {pais['CONTINENTE']}")
    else:
        print("No se encontró el país.")
    return


# opcion 4

def listar_paises(paises):
    print("\nLISTAR PAÍSES")
    if len(paises) == 0:
        print("No hay países cargados.")
        return
    for pais in paises:
        print(f"{pais['NOMBRE']} | Población: {pais['POBLACION']} | Superficie: {pais['SUPERFICIE']} | Continente: {pais['CONTINENTE']}")


# opcion 5

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


# opcion 6 

def filtrar_paises(paises):
    print("\nFILTRAR PAÍSES")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")

    opcion_str = input("Elegí una opción (1-3): ").strip()
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

    # lista donde guardamos los países filtrados
    filtrados = []

    # FILTRO POR CONTINENTE
    if tipo_filtro == 1:
        continent = input("\nIngresa un continente: ").strip().lower()
        if continent == "":
            print("Continente vacío.")
            return
        for pais in paises:
            if continent in pais["CONTINENTE"].lower():
                filtrados.append(pais)

    # POR RANGO DE POBLACIÓN
    elif tipo_filtro == 2:
        minima_poblacion = input("Población mínima: ").strip()
        if minima_poblacion == "":
            print("No se permiten campos vacios")
            return
        maxima_poblacion = input("Población máxima: ").strip()
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

    # POR RANGO DE SUPERFICIE
    elif tipo_filtro == 3:
        minima_superficie = input("Superficie mínima: ").strip()
        if minima_superficie == "":
            print("No se permiten campos vacios")
            return
        maxima_superficie = input("Superficie máxima: ").strip()
        if maxima_superficie == "":
            print("No se permiten campos vacios")
            return  # <-- faltaba este return para cortar el flujo si está vacía

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

    # MOSTRAR RESULTADOS
    if len(filtrados) > 0:  # si encontramos países filtrados
        print("\nResultados del filtro:\n")
        for pais in filtrados:
            print(f"{pais['NOMBRE']} | {pais['POBLACION']} habitantes. | {pais['SUPERFICIE']} km² | {pais['CONTINENTE']}")
    else:
        print("No se encontraron países con esos datos.")


# opcion 7

def ordenar_paises(paises):
    print("\nORDENAR PAÍSES")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")

    opcion_orden = input("Elegí una opción: ").strip()

    # verificar que no este vacio
    if opcion_orden == "":
        print("Opcion vacia")
        return paises

    # verificar que sea un número entero válido
    if not opcion_orden.isdigit():
        print("\nIngresa un numero entero valido")
        return paises

    # verificar rango correcto de opciones
    opcion = int(opcion_orden)
    if opcion < 1 or opcion > 3:
        print("Opcion invalida. Las opciones son del 1 al 3.")
        return paises

    orden = input("¿Ascendente (A) o descendente (D)?: ").strip().upper()
    if orden not in ["A", "D"]:
        print("Debe ingresar A o D.")
        return paises

    cantidad = len(paises)
    if cantidad <= 1:
        print("No hay suficientes países para ordenar.")
        return paises

    if opcion == 1:  # ORDENAR POR NOMBRE
        for i in range(cantidad - 1):
            for j in range(cantidad - i - 1):
                nombre1 = paises[j]["NOMBRE"].lower()
                nombre2 = paises[j + 1]["NOMBRE"].lower()
                if (orden == "A" and nombre1 > nombre2) or (orden == "D" and nombre1 < nombre2):
                    temp = paises[j]
                    paises[j] = paises[j + 1]
                    paises[j + 1] = temp

    elif opcion == 2:  # ORDENAR POR POBLACIÓN
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


# opcion 8

def mostrar_estadisticas(paises):
    print("\nESTADÍSTICAS")
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    # país con mayor y menor población
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


def menu():

    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    archivo = os.path.join(ruta_actual, "paises.csv")
    paises = cargar_datos(archivo)

    while True:
        print("\nMENU\n")
        print("1. Agregar pais")
        print("2. Actualizar poblacion/superficie")
        print("3. Buscar pais")
        print("4. Listar países")
        print("5. Eliminar país")
        print("6. Filtrar países")
        print("7. Ordenar países")
        print("8. Mostrar estadísticas")
        print("9. Salir")

        opcion_str = input("Elegi una opcion: ").strip()

        # verificar que no este vacio
        if opcion_str == "":
            print("No se permiten campos vacios.")
            continue

        # verificar que solo sean numeros
        if not opcion_str.isdigit():
            print("Debe ingresar un numero del 1 al 9.")
            continue

        opcion = int(opcion_str)

        if opcion == 1:
            paises = agregar_pais(paises)
        elif opcion == 2:
            paises = actualizar_poblacion_y_superficie(paises)
        elif opcion == 3:
            buscar_pais(paises)
        elif opcion == 4:
            listar_paises(paises)
        elif opcion == 5:
            paises = eliminar_pais(paises)
        elif opcion == 6:
            filtrar_paises(paises)
        elif opcion == 7:
            paises = ordenar_paises(paises)
        elif opcion == 8:
            mostrar_estadisticas(paises)
        elif opcion == 9:
            guardar_datos(archivo, paises)
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Ingrese las opciones del 1 al 9")


# EJECUCIÓN
menu()
