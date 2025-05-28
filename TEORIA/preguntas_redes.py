import random

def leer_preguntas(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read().split('\n\n')
    
    preguntas = []
    for bloque in contenido:
        lineas = [linea for linea in bloque.split('\n') if linea.strip()]  # Filtra las líneas vacías
        if len(lineas) < 3:
            print("Bloque de preguntas vacío o incompleto. Ignorando.")
            continue  # Si no hay suficientes líneas para una pregunta, la ignoramos
        pregunta = lineas[0].split(': ', 1)[1]
        opciones = {}
        for linea in lineas[1:]:
            if '.' in linea:
                clave, opcion = linea.split('. ', 1)
                opciones[clave.strip()] = opcion.strip()
            elif 'Respuesta correcta' in linea:
                respuesta_correcta = linea.split(': ')[1].strip()
        preguntas.append((pregunta, opciones, respuesta_correcta))
    
    return preguntas

def realizar_test(preguntas, aleatorio=False):
    if aleatorio:
        random.shuffle(preguntas)
        preguntas = preguntas[:25]  # Tomar solo las primeras 25 preguntas en modo aleatorio
    
    num_preguntas = len(preguntas)  # Obtener el número total de preguntas
    
    correctas = 0
    incorrectas = 0
    for i, (pregunta, opciones, respuesta_correcta) in enumerate(preguntas, start=1):
        print(f"Pregunta {i}: {pregunta}")
        for clave, opcion in opciones.items():
            print(f"{clave}) {opcion}")
        
        respuesta_usuario = input("Tu respuesta: ").strip().lower()
        if respuesta_usuario == respuesta_correcta.lower():
            correctas += 1
            print("¡Correcto!\n")
        else:
            incorrectas += 1
            print(f"Incorrecto. La respuesta correcta era: {respuesta_correcta}\n")
    
    #Calcular puntuacion sobre 10, aciertos valen 1, fallos valen -0.25
    print(f"Test finalizado. Respuestas correctas: {correctas}, Respuestas incorrectas: {incorrectas}")
    puntuacion = ((correctas - (incorrectas * 0.25)) / num_preguntas) * 10
    print(f"Puntuación: {puntuacion:.2f}")

if __name__ == "__main__":
    archivo_preguntas = 'preguntas.txt'  # Reemplaza con el nombre de tu archivo
    preguntas = leer_preguntas(archivo_preguntas)
    
    if not preguntas:
        print("No se encontraron preguntas en el archivo o el archivo está mal formateado.")
    else:
        print("Bienvenido al test de redes.")
        modo = input("¿Quieres realizar el test en orden (o) o aleatoriamente (a)? \n").strip().lower()
        realizar_test(preguntas, aleatorio=(modo == 'a'))
