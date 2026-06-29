
"""
Historial:
"""

from datetime import datetime

nombre_de_archivo = "historial.txt"

def obtener_fecha_hora_actual():
    instante = datetime.now()
    return instante.strftime("%Y-%m-%d %H:M")



def guardar_partida(nombre, nivel, movs, tipo, resultado):
    # Guarda en historial.txt una línea con los datos
    fecha_hora = obtener_fecha_hora_actual()

    linea = f"{nombre.strip()},{fecha_hora},{nivel},{tipo},{resultado},{movs}\n"

    archivo = open(nombre_archivo, "a")
    archivo.write(linea)
    archivo.close()

def ver_historial():
    # Lee historial.txt y lo muestra en formato tabla
    partidas = []

    try:
        archivo = open(nombre_archivo, "r")
    except FileNotFoundError:
        return partidas

    for linea in archivo:
        linea = linea.strip()
        if linea == "":
            continue

        datos = linea.split(",")
        partidas.append(datos)
    archuvo.close()
    return partidas

def mostrar_historial():
    pass