"""
Necesito hacer un programa que me haga un diccionario de datos en un
archivo .txt que guarde todas las posibles combinaciones de datos con
4 caracteres usando las 27 letras del abecedario incluyendo la ñ
y los 10 dígitos numéricos
"""

import itertools
import string
import time


def main():
    # Crear un archivo de texto
    with open("diccionario.txt", "w") as file:
        # Iniciamos el contador de tiempo
        start_time = time.time()

        # Crear una lista con las letras del abecedario y los dígitos numéricos
        letters = list(string.ascii_lowercase + "ñ" + string.digits)
        letters = [letter.encode('utf-8').decode('latin-1') for letter in letters]

        # Crear un generador de todas las posibles combinaciones de 4 caracteres
        combinations = itertools.product(letters, repeat=4)

        # Iterar sobre todas las combinaciones
        for combination in combinations:
            # Convertir la combinación en una cadena
            result = "".join(combination)
            # Escribir la cadena en el archivo
            file.write(result + "\n")

        # Sacamos el contador final del tiempo
        end_time = time.time()

        # Obtenemos el tiempo empleado
        elapsed_time = end_time - start_time

        print(f"El tiempo usado fue de: {elapsed_time} segundos")

if __name__ == "__main__":
    main()
