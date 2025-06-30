import numpy as np
from random import randint, sample


def crear_matriz(rows: int, cols: int, total_leg: int) -> np.ndarray:
    # sample retorna una lista de legajos unicos a partir de una secuencia
    # range de 1 a total de alumnos matriculados en la escuela (total_leg)
    # y la lista devuelta tiene un length acorde a cantidad de alumnos evaluados (rows)
    legajos = sample(range(1, total_leg), rows)
    matriz = np.zeros(shape=(rows, cols), dtype=np.int8)
    for row in range(rows):
        for col in range(cols):
            matriz[row][col] = legajos[row] if col == 0 else randint(1, 10)

    return matriz


def filtrar_por_alumno(row: np.ndarray) -> int:
    # return sum(1 for _ in filter(lambda x: x >= 4, row[1:]))
    acum = 0
    for nota in row[1:]:
        acum += 1 if nota >= 4 else 0
    return acum


def definir_situacion(aprobadas: int) -> str:
    if aprobadas < 3:
        return "A recursar"
    elif aprobadas == 3:
        return "A recuperatorio"
    else:
        return "Regular"


def imprimir_condiciones(
    cant_alumnos: int, alumnos_examinados: int, cant_columnas: int
) -> None:
    matriz = crear_matriz(alumnos_examinados, cant_columnas, cant_alumnos)
    print("/" * 15)
    print(matriz)
    print("/" * 15)

    for alumno in matriz:
        cant_aprobadas = filtrar_por_alumno(alumno)
        situacion = definir_situacion(cant_aprobadas)
        print(f'La situacion del alumno {alumno[0]} es: "{situacion}"')


if __name__ == "__main__":
    total_alumnos = 100
    alumn_examinados = 5
    cant_parciales = 5  # pasa +1 para columna de alumno

    imprimir_condiciones(total_alumnos, alumn_examinados, cant_parciales + 1)
