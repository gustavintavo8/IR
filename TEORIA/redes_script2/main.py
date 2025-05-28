import json
import os
import random
from colorama import Fore, Style
import os
import time

ACIERTOS = 0
FALLOS = 0


def cargar_jsons():
    archivos_json = [f for f in os.listdir() if f.endswith(".json")]
    archivos_json = {i + 1: f for i, f in enumerate(archivos_json)}
    print("Selecciona los JSONS que quieres incluir:")
    for id, nombre in archivos_json.items():
        print(f"{id}) {nombre}")
    print(
        "Escribe el identificador de cada test, por Ej.(1,2,3) para seleccionar los 3 primeros. Escribe 0 para seleccionarlos todos."
    )
    seleccion = input()
    if seleccion == "0":
        seleccion = archivos_json.keys()
    else:
        seleccion = map(int, seleccion.split(","))
    preguntas = []
    for id in seleccion:
        if id in archivos_json:
            with open(archivos_json[id], "r") as f:
                preguntas.extend(json.load(f))
        else:
            print(f"Identificador {id} no válido.")
            return
    return preguntas


def limpiar_pantalla():
    os.system("clear")


def obtener_orden():
    return input("¿Mostrar preguntas en orden (o) o aleatorio(a)? ")


def mezclar_preguntas(preguntas, orden):
    if orden.lower() == "a":
        random.shuffle(preguntas)


def mostrar_pregunta(pregunta, numero_pregunta, aciertos, fallos, total_preguntas):
    print(f"Pregunta número: {numero_pregunta}/{total_preguntas}")
    print(f"Aciertos: {aciertos} Fallos: {fallos}\n Puntuación(sobre 10):" + Fore.GREEN + Style.BRIGHT + " {:.2f}".format(calcular_nota_sobre_10(aciertos, fallos, total_preguntas)) + Style.RESET_ALL + Fore.RESET)
    print()
    print(pregunta["pregunta"])
    for opcion in pregunta["opciones"]:
        print(opcion)


def obtener_respuesta_usuario():
    return input("Tu respuesta: ").lower()


def comprobar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_usuario == respuesta_correcta[0].lower():
        print(Fore.GREEN + "Correcto!" + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + "Incorrecto!" + Style.RESET_ALL)
        print(f"La respuesta correcta es: {respuesta_correcta}")
        return False


def calcular_nota_sobre_10(aciertos, fallos, total_preguntas):
    return aciertos * 10 / total_preguntas

def mostrar_preguntas(preguntas):
    aciertos = 0
    fallos = 0
    total_preguntas = len(preguntas)
    n_preguntas_invalidas = 0

    orden = obtener_orden()
    mezclar_preguntas(preguntas, orden)

    limpiar_pantalla()

    for i, pregunta in enumerate(preguntas, start=1):
        if (
            "pregunta" in pregunta
            and "opciones" in pregunta
            and "respuesta_correcta" in pregunta
        ):
            mostrar_pregunta(pregunta, i, aciertos, fallos, total_preguntas)
            print("")
            respuesta_usuario = obtener_respuesta_usuario()
            if comprobar_respuesta(respuesta_usuario, pregunta["respuesta_correcta"]):
                aciertos += 1
            else:
                fallos += 1
            input("Presiona Enter para continuar...")
            limpiar_pantalla()
        else:
            print("Error: La pregunta no tiene el formato correcto.")
            n_preguntas_invalidas += 1

    print(
        f"Se encontraron {n_preguntas_invalidas} preguntas inválidas de un total de {total_preguntas}."
    )


if __name__ == "__main__":
    preguntas = cargar_jsons()
    if preguntas:
        mostrar_preguntas(preguntas)
