
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
    partidas = leer_historial()

    print("\==== HISTORIAL DE JUEGOS ====")

    if len(partidas) == 0:
        print("No hay Partidas registradas por ahora.")
        return

    print(f"| {'Nombre': <10} | {'Fecha y hora': <16} | {'Nivel':<5} | {'Tipo':<10} | {'Resultado':<9} | {'Mov.'´: <4} |")

    print(f"|{"-"*12}|{"-"*18}|{"-"*7}|{"-"*12}|{"-"*11}|{"-"*6}|")

    for partida in partidas:
        nombre = partida[0]
        fecha_hora = partida[1]
        nivel = partida[2]
        tipo_juego = partida[3]
        resultado = partida[4]
        movs = partida[5]

        print(f"| {nombre:<10} | {fecha_hora:<16} | {nivel:<5} | {tipo_juego:<10} | {resultado:<9} | {movs: <4} |")

