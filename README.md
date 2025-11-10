# 🐍 Gestor de Países – Trabajo Práctico Integrador
### Materia: Programación I  
### Tecnicatura Universitaria en Programación a Distancia  

---

## 🧩 Descripción del programa
El **Gestor de Países** es una aplicación desarrollada en Python que permite **administrar información sobre países** utilizando un archivo CSV como base de datos.  
El sistema integra los principales conceptos aprendidos durante la cursada: **listas, diccionarios, funciones, estructuras condicionales, bucles, validaciones, ordenamientos y cálculos estadísticos**.

El usuario puede agregar, modificar, eliminar y buscar países, además de aplicar filtros, ordenar registros y generar indicadores generales como promedios y conteos por continente.

---

## ⚙️ Instrucciones de uso
1. Guardar los archivos `TPI_con_correccion.py` y `paises.csv` en la misma carpeta.  
2. Ejecutar el programa desde la terminal o Visual Studio Code con el comando:
   ```bash
   python TPI.py
   ```
3. Elegir una de las opciones del menú:
   - Agregar país  
   - Actualizar población y superficie  
   - Buscar o listar países  
   - Eliminar registros  
   - Filtrar y ordenar  
   - Mostrar estadísticas  
   - Salir y guardar cambios  

Los datos se guardan automáticamente en el archivo `paises.csv` al salir del programa.

---

## 💻 Ejemplos de entradas y salidas

**Entrada – Agregar país:**
```
Nombre: Argentina
Población: 45376763
Superficie: 2780400
Continente: América
```

**Salida:**
```
País 'Argentina' agregado correctamente.
```

**Entrada – Filtrar países por población:**
```
Población mínima: 50000000
Población máxima: 150000000
```

**Salida:**
```
Brasil | 213993437 habitantes | 8515767 km² | América
Japón  | 125800000 habitantes | 377975 km²  | Asia
```

---

## 👩‍💻 Participación de los integrantes

- **Carolina Benítez (Comisión 8):** desarrollo inicial del código, estructura del menú y documentación del programa, grabación del video presentativo del TPI.

- **Lorena Romina Soto Aravena (Comisión 13):** validaciones, depuración final, grabación del video presentativo del TPI y documentación complementaria (marco teórico y conclusiones).

