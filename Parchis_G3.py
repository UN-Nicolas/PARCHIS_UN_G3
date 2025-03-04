# -*- coding: utf-8 -*-
"""Parchis_G3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pZPjg_7wmF4ey_3s-AdoLF0MTDdNtBl5
"""

import random

# Inicialización del tablero y fichas
tablero = {i: [] for i in range(1, 69)}#El tablero consta de 69 casillas usamos un bucle para tener esa totaidad en listas sin tener que hacer cada lista
llegadas = {color: [None] * 8 for color in ["rojo", "azul", "verde", "amarillo"]}#Cada color tiene 8 lugares de llegada
seguros_por_color = {
    "azul": [6, 13, 18],
    "amarillo": [23, 30, 35],
    "verde": [40, 47, 52],
    "rojo": [57, 54, 1]
}#cada seguro que tiene cada color
salidas = {"azul": 6, "amarillo": 23, "verde": 40, "rojo": 57}#Casilla donde sale cada color
primer_seguro_oponente = {"azul": [23, 40, 57], "amarillo": [6, 40, 57], "verde": [6, 13, 57], "rojo": [6, 13, 23]}#Aqui definimos las casillas donde si cae la ficha de ese color y el equipo contrario saca una ficha se regresa a la carcel

# Fichas por color
colores_disponibles = ["azul", "amarillo", "verde", "rojo"]#Colores disponibles en nuestro tablero
fichas = {
    "azul": {f"Z{i}": 0 for i in range(1, 5)},
    "amarillo": {f"A{i}": 0 for i in range(1, 5)},
    "verde": {f"V{i}": 0 for i in range(1, 5)},
    "rojo": {f"R{i}": 0 for i in range(1, 5)}
}#Ciclos para asignar a cada color una ficha ejemplo rojo tiene 4 fichas R1,R2,R3,R4

# Selección de jugadores
num_jugadores = int(input("Ingrese el número de jugadores (1-4): "))#Se ingresa cuantos jugadores participaran
jugadores = {}#Diccionario vacio para llenarlo despúes
# Se recorre el número de jugadores para que cada uno elija un color
for i in range(1, num_jugadores + 1):
    print(f"Jugador {i}, elige un color de los disponibles: {colores_disponibles}")  # Se muestran los colores disponibles
    color_elegido = input("Color: ").strip().lower()  # Se solicita al jugador que ingrese un color y se normaliza el texto

    # Se valida que el color elegido esté en la lista de colores disponibles
    while color_elegido not in colores_disponibles:
        print("Color no válido. Elige uno de los disponibles.")  # Mensaje de error si el color no es válido
        color_elegido = input("Color: ").strip().lower()  # Se vuelve a pedir un color válido

    # Se asigna el color elegido al jugador en el diccionario
    jugadores[f"Jugador {i}"] = color_elegido

    # Se elimina el color elegido de la lista para que no pueda ser seleccionado nuevamente
    colores_disponibles.remove(color_elegido)
def IMPtablero():
    print("+" + ("-"*95) + "+")
    x = 50
    for i in range(1, 14):
        if i%2 == 0:
            print("|" + ("\t" * 4) + "|" + ("-"*31) + "|" +("\t" * 4) + "|")
        else:
            if i == 1:
                print("|" + ("\t" * 4) + f"|\t[{', '.join(tablero[53])}]\tS{','.join(tablero[52])}S\t[{', '.join(tablero[51])}]\t|" + ("\t" * 4) + "|")
            else:
                roj = i + x + 1
                llegroj = x - 44
                if i == 9:
                    print("|" + ("\t" * 4) + "|" + f"\tS{','.join(tablero[roj])}S\t[{llegadas['rojo'][llegroj]}]\tS{', '.join(tablero[x])}S\t|" + ("\t" * 4) + "|")
                else:
                    print("|" + ("\t" * 4) + "|" + f"\t[{', '.join(tablero[roj])}]\t[{llegadas['rojo'][llegroj]}]\t[{', '.join(tablero[x])}]\t|" + ("\t" * 4) + "|")
                x -= 1
    print("+" + ("-"*95) + "+")
    for m in range(1,12):
        if m == 4 or m == 8:
            print("+" + ("-"*43) + (" " *9) + ("-"*43) + "+")
        elif m == 1:
            print(f"| [{', '.join(tablero[67])}]\t [{', '.join(tablero[65])}]\t [{', '.join(tablero[63])}]\t\t|\t[{', '.join(tablero[60])}]\t[{llegadas['rojo'][llegroj]}]\t[{', '.join(tablero[44])}]\t| [{', '.join(tablero[41])}]\t [{', '.join(tablero[39])}]\t [{', '.join(tablero[37])}]\t\t|")
        elif m == 3:
            print(f"|[{', '.join(tablero[68])}]\t[{', '.join(tablero[66])}]\tS{', '.join(tablero[64])}S\t[{','.join(tablero[62])}]\t|\t[{', '.join(tablero[61])}]\t\t[{', '.join(tablero[43])}]\t|[{', '.join(tablero[42])}]\tS{','.join(tablero[40])}S\t[{', '.join(tablero[38])}]\t[{', '.join(tablero[36])}]\t|")
        elif m == 5:
            print(f"|S{','.join(tablero[1])}S\t[{llegadas['azul'][6]}]\t[{llegadas['azul'][4]}]\t{llegadas['azul'][2]}\t|\t{llegadas['azul'][0]}\t|Meta|\t\t|  {llegadas['verde'][1]}\t  {llegadas['verde'][3]}\t   {llegadas['verde'][5]}\t\t|")
        elif m == 7:
            print(f"|  {llegadas['azul'][5]}\t   {llegadas['azul'][3]}\t   {llegadas['azul'][1]}\t\t|\t\t|Meta|\t{llegadas['verde'][0]}\t|{llegadas['verde'][2]}\t{llegadas['verde'][4]}\t{llegadas['verde'][6]}\tS{','.join(tablero[35])}S\t|")
        elif m == 9:
            print(f"|[{', '.join(tablero[2])}]\t[{', '.join(tablero[4])}]\tS{','.join(tablero[6])}S\t[{', '.join(tablero[8])}]\t|\t[{', '.join(tablero[9])}]\t\t[{', '.join(tablero[27])}]\t|[{', '.join(tablero[28])}]\tS{','.join(tablero[30])}S\t[{', '.join(tablero[32])}]\t[{', '.join(tablero[34])}]\t|")
        elif m == 11:
            print(f"| [{', '.join(tablero[3])}]\t [{', '.join(tablero[5])}]\t [{', '.join(tablero[7])}]\t\t|\t[{', '.join(tablero[10])}]\t{llegadas['amarillo'][0]}\t[{', '.join(tablero[26])}]\t| [{', '.join(tablero[29])}]\t [{', '.join(tablero[31])}]\t [{', '.join(tablero[33])}]\t\t|")
        else:
            print("|\t\t\t\t|" + (" "*31) + "|" + "\t\t\t\t|")
    print("+" + ("-"*95) + "+")
    x = 10
    lle = 1
    for f in range(1, 14):
        if f%2 == 0:
            print("|" + ("\t" * 4) + "|" + ("-"*31) + "|" +("\t" * 4) + "|")
        else:
            if f == 13:
                print("|" + ("\t" * 4) + f"|\t[{', '.join(tablero[17])}]\tS{','.join(tablero[18])}S\t[{', '.join(tablero[19])}]\t|" + ("\t" * 4) + "|")
            else:
                am = f + x
                llegam = x + 15
                if f == 5:
                    print("|" + ("\t" * 4) + "|" + f"\tS{','.join(tablero[am])}S\t{llegadas['amarillo'][lle]}\tS{','.join(tablero[llegam])}S\t|" + ("\t" * 4) + "|")
                else:
                    print("|" + ("\t" * 4) + "|" + f"\t[{', '.join(tablero[am])}]\t{llegadas['amarillo'][lle]}\t[{', '.join(tablero[llegam])}]\t|" + ("\t" * 4) + "|")
                lle += 1
                x -= 1
    print("+" + ("-"*95) + "+")

def mover_ficha(ficha, pasos, color):
      #Función que mueve una ficha en el tablero de juego.Parámetros:ficha: Nombre o identificador de la ficha a mover.pasos: Número de casillas a avanzar.
      # color: Color del jugador que mueve la ficha.
      #Retorno:
      #No retorna nada, pero actualiza la posición de la ficha en el tablero.
      # Verifica si la ficha pertenece al color del jugador
    if ficha not in fichas[color]:
        print("Ficha no válida.")  # Mensaje de error si la ficha no es del jugador
        return

    # Verifica si la ficha está en la "cárcel" (posición 0)
    if fichas[color][ficha] == 0:
        if pasos == 5:  # Solo puede salir si saca un 5
            salida = salidas[color]  # Se obtiene la casilla de salida del color
            if len(tablero[salida]) < 2:  # Verifica si hay espacio en la salida
                tablero[salida].append(ficha)  # Mueve la ficha a la salida
                fichas[color][ficha] = salida  # Actualiza la posición de la ficha
                print(f"{ficha} salió a la casilla {salida}")
            else:
                print(f"{ficha} no puede salir, la salida está llena. Debes mover las fichas en la salida.")
        else:
            print(f"{ficha} no puede salir, necesitas un 5.")  # Mensaje si no sacó un 5
    else:
        # Si la ficha ya está en el tablero, se calcula su nueva posición
        casilla_actual = fichas[color][ficha]  # Obtiene la casilla actual
        nueva_casilla = (casilla_actual + pasos - 1) % 68 + 1  # Movimiento con reinicio en 68

        # Verifica si la casilla está disponible o si es una casilla segura
        if len(tablero[nueva_casilla]) < 2 or nueva_casilla in seguros_por_color[color]:
            if ficha in tablero[casilla_actual]:  # Elimina la ficha de la casilla actual
                tablero[casilla_actual].remove(ficha)
            tablero[nueva_casilla].append(ficha)  # Mueve la ficha a la nueva casilla
            fichas[color][ficha] = nueva_casilla  # Actualiza la posición en el diccionario
            print(f"{ficha} se movió a la casilla {nueva_casilla}")
        else:
            print(f"No puedes mover {ficha} a {nueva_casilla}, hay un bloqueo.")  # Mensaje de bloqueo

while True:  # Bucle infinito para el turno de los jugadores
    for jugador, color in jugadores.items():  # Itera sobre cada jugador y su color asignado
        print(f"\nTurno de {jugador} ({color.capitalize()})")  # Muestra de quién es el turno

        # Se lanzan dos dados y se calcula su suma
        dado1, dado2 = random.randint(1, 6), random.randint(1, 6)
        suma_dados = dado1 + dado2
        print(f"Lanzaste: {dado1} y {dado2}")

        # Obtiene las fichas que están en la cárcel (posición 0)
        fichas_disponibles = [f for f in fichas[color] if fichas[color][f] == 0]

        # Obtiene las fichas que ya están en el tablero
        fichas_movibles = [f for f in fichas[color] if fichas[color][f] != 0]

        # Si la suma de los dados es 5, el jugador puede sacar una ficha de la cárcel
        if suma_dados == 5:
            if fichas_disponibles:  # Verifica si hay fichas en la cárcel
                print("Puedes sacar una ficha de la cárcel.")
                print("Fichas disponibles para sacar:", fichas_disponibles)

                # Se pide al jugador elegir qué ficha quiere sacar
                ficha_salida = input("Elige una ficha para sacar de la cárcel: ")
                while ficha_salida not in fichas_disponibles:  # Valida la entrada
                    print("Ficha no válida. Elige otra.")
                    ficha_salida = input("Elige una ficha para sacar de la cárcel: ")

                # Se mueve la ficha elegida a la salida
                mover_ficha(ficha_salida, 5, color)
                IMPtablero()  # Se actualiza el tablero
            continue  # Pasa al siguiente jugador sin permitir más movimientos

        # Si los dos dados son 5, el jugador puede sacar dos fichas de la cárcel
        if dado1 == 5 and dado2 == 5:
            if len(tablero[salidas[color]]) == 0:  # Verifica si la salida está vacía
                print("Puedes sacar dos fichas.")
                print("Fichas disponibles para sacar:", fichas_disponibles)

                # Se pide al jugador que elija dos fichas para sacar
                ficha_mover1 = input("Elige una ficha para sacar: ")
                ficha_mover2 = input("Elige otra ficha para sacar: ")

                # Se mueven ambas fichas a la salida
                mover_ficha(ficha_mover1, 5, color)
                mover_ficha(ficha_mover2, 5, color)

                IMPtablero()  # Se actualiza el tablero
            # Verifica si la casilla de salida ya tiene dos fichas y si hay fichas en movimiento
            if len(tablero[salidas[color]]) == 2 and fichas_movibles:
                print("Puedes sacar dos fichas.")# Indica que puede liberar dos fichas de la cárcel
                print("Fichas disponibles para sacar:", fichas_disponibles)
                # Se pide al jugador que elija dos fichas para sacar de la cárcel
                ficha_mover = input("Elige una ficha para sacar: ")
                ficha_mover = input("Elige otra ficha para sacar: ")
                # Se mueven ambas fichas a la salida con un avance determinado
                mover_ficha(ficha_mover, dado1 if dado2 == 5 else dado2, color)
                # Se actualiza el tablero con los cambios
                IMPtablero()
            # Si hay fichas en la cárcel, se permite sacar una y moverla o mover otra ficha
            if fichas_disponibles:
                print("Puedes sacar una ficha de la cárcel y moverla o mover otra.")
                print("Fichas disponibles para sacar:", fichas_disponibles)
                ficha_salida = input("Elige una ficha para sacar de la cárcel: ")# Se solicita al jugador que elija una ficha para sacar de la cárcel
                 # Validación: Verifica que la ficha elegida está en la lista de fichas disponibles
                while ficha_salida not in fichas_disponibles:# Bucle para validar que la ficha seleccionada para salir de la cárcel sea válida
                    print("Ficha no válida. Elige otra.")
                    ficha_salida = input("Elige una ficha para sacar de la cárcel: ")
                mover_ficha(ficha_salida, 5, color)# Mueve la ficha seleccionada fuera de la cárcel con un avance de 5 casillas
                if len(fichas_movibles) == 0:# Si no hay más fichas en juego, la única opción es mover la ficha que se acaba de sacar
                    ficha_mover = ficha_salida
                else:
                    ficha_mover = input("Elige otra ficha para mover: ") # Se permite elegir otra ficha para mover si hay fichas disponibles en el tablero
                    while ficha_mover not in fichas_disponibles: # Bucle para validar que la ficha seleccionada sea válida y esté en juego
                        print("Ficha no válida. Elige otra.")
                        ficha_mover = input("Elige otra ficha para mover: ")
                mover_ficha(ficha_mover, 5, color)# Mueve la ficha elegida con un avance de 5 casillas
                IMPtablero()# Se actualiza el tablero con los cambio
            continue# Se pasa al siguiente turno sin permitir más movimientos en este turno
        # Verifica si al menos uno de los dados sacó un 5
        if dado1 == 5 or dado2 == 5:
            # Si la salida está llena (tiene dos fichas) y hay fichas en movimiento, se permite mover una antes de sacar otra
            if len(tablero[salidas[color]]) == 2 and fichas_movibles:
                print("Puedes mover una ficha antes de sacar otra.")
                print(fichas_disponibles)
                ficha_mover = input("Elige una ficha para mover: ")# Se solicita la ficha a mover y se valida que sea una ficha en juego
                while ficha_mover not in fichas_movibles:
                    print("Ficha no válida. Elige otra.")
                    ficha_mover = input("Elige una ficha para mover: ", fichas_disponibles)
                # Mueve la ficha seleccionada utilizando el dado adecuado
                mover_ficha(ficha_mover, dado1 if dado2 != 5 else dado2, color)
                IMPtablero()  # Muestra el tablero actualizado

            if fichas_disponibles:    # Si hay fichas disponibles para sacar de la cárcel
                print("Puedes sacar una ficha de la cárcel y moverla o mover otra.")
                print("Fichas disponibles para sacar:", fichas_disponibles)
                ficha_salida = input("Elige una ficha para sacar de la cárcel: ")# Solicita al usuario que elija una ficha para sacar de la cárcel y valida la entrada
                while ficha_salida not in fichas_disponibles:
                    print("Ficha no válida. Elige otra.")
                    ficha_salida = input("Elige una ficha para sacar de la cárcel: ")
                mover_ficha(ficha_salida, 5, color)# Mueve la ficha fuera de la cárcel con un movimiento de 5 casillas
                if len(fichas_movibles) == 0:# Si no hay más fichas en movimiento, la ficha salida se convierte en la ficha a mover
                    ficha_mover = ficha_salida
                else:# Solicita al usuario elegir otra ficha para mover y valida la entrada
                    ficha_mover = input("Elige una ficha para mover: ")
                    while ficha_mover not in fichas_movibles:
                        print("Ficha no válida. Elige otra.")
                        ficha_mover = input("Elige una ficha para mover: ")
                # Mueve la ficha seleccionada con el dado adecuado
                mover_ficha(ficha_mover, dado1 if dado2 == 5 else dado2, color)
                IMPtablero()# Continúa con la siguiente iteración del juego
            continue
        else:
            # Si no se obtuvo un 5 en los dados, verifica si hay fichas en movimiento
            if len(fichas_movibles) > 0:
                print("Puedes mover las fichas.")
                print(fichas_movibles)
                # Solicita al usuario que elija una ficha para mover
                ficha_mover = input("Elige la ficha para mover: ")
                mover_ficha(ficha_mover, dado1, color)
                # Verifica si aún quedan fichas para mover
                if len(fichas_movibles) == 0:
                    ficha_mover = ficha_mover# No hay fichas adicionales para mover
                else:
                    # Solicita otra ficha para mover y valida la entrada
                    ficha_mover = input("Elige otra ficha para mover: ")
                    while ficha_mover not in fichas_movibles:
                        print("Ficha no válida. Elige otra.")
                        ficha_mover = input("Elige otra ficha para mover: ")
                # Mueve la ficha seleccionada con el segundo dado
                mover_ficha(ficha_mover, dado2, color)
                IMPtablero()# Muestra el tablero actualizado
            else:
                continue # No hay más movimientos disponibles, continuar con la siguiente iteración